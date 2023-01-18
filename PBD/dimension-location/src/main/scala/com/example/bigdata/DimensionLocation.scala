package com.example.bigdata

import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions.{avg, first, udf}
object DimensionLocation {

  def incomeClassifier(incomeString: String): String = {
    try {
      val income = incomeString.toInt

      if (income > 59000) return "high"
      if (income > 48000) return "medium"
      "low"
    } catch {
      case e: Exception => return "medium"
    }
  }

  def distanceClassifier(distanceString: String): String = {
    try {
      val distance = distanceString.toDouble

      if (distance > 0.75) return "long"
      if (distance > 0.27) return "medium"
      "short"
    } catch {
      case e: Exception => return "medium"
    }
  }

  def main (args: Array[String]): Unit = {
    // Remember to delete `master` when not running locally
    val spark = SparkSession.builder.appName("DimensionLocation").getOrCreate()
    import spark.implicits._

    val londonCrimesFilepath1 = args(0)
    val londonCrimesFilepath2 = args(1)
    val londonPostcodesFilepath = args(2)
    val incomeClassifierUDF = udf(x => incomeClassifier(x))
    val distanceClassifierUDF = udf(x => distanceClassifier(x))

    val londonCrimes1 = (spark
      .read
      .format("csv")
      .option("header", value = true)
      .option("inferSchema", value = true)
      .load(londonCrimesFilepath1))

    val londonCrimes2 = (spark
      .read
      .format("csv")
      .option("header", value = true)
      .option("inferSchema", value = true)
      .load(londonCrimesFilepath2))

    val londonCrimes = londonCrimes1.union(londonCrimes2).dropDuplicates("lsoa_code")

    val londonPostcodes = (spark
      .read
      .format("csv")
      .option("header", value = true)
      .option("inferSchema", value = true)
      .load(londonPostcodesFilepath))

    val londonPostcodesUniqueLsoa = (londonPostcodes
      .withColumnRenamed("LSOA Code", "lsoa_code")
      .withColumnRenamed("County", "county")
      .withColumnRenamed("District", "district")
      .withColumnRenamed("Rural/urban", "rural/urban")
      .withColumnRenamed("Water company", "water_company")
      .withColumnRenamed("Quality", "quality")
      .withColumnRenamed("Average Income", "income_numerical")
      .withColumnRenamed("Distance to station", "closeness_to_station_numerical")
      .select(
        $"lsoa_code",
        $"county",
        $"district",
        $"rural/urban",
        $"water_company",
        $"quality",
        $"income_numerical",
        $"closeness_to_station_numerical"
      )
      .groupBy($"lsoa_code")
      .agg(
        first($"county", ignoreNulls = true).as("county"),
        first($"district", ignoreNulls = true).as("district"),
        first($"rural/urban", ignoreNulls = true).as("rural/urban"),
        first($"water_company", ignoreNulls = true).as("water_company"),
        first($"quality", ignoreNulls = true).as("quality"),
        avg($"income_numerical").as("income_numerical"),
        avg($"closeness_to_station_numerical").as("closeness_to_station_numerical")
      )
      .withColumn("income", incomeClassifierUDF($"income_numerical"))
      .withColumn("closeness_to_station", distanceClassifierUDF($"closeness_to_station_numerical"))
    )

    val locations = (londonCrimes
      .join(londonPostcodesUniqueLsoa, londonCrimes("lsoa_code") === londonPostcodesUniqueLsoa("lsoa_code"))
      .select(
        londonCrimes("lsoa_code"),
        londonCrimes("borough"),
        londonPostcodesUniqueLsoa("county"),
        londonPostcodesUniqueLsoa("district"),
        londonPostcodesUniqueLsoa("rural/urban"),
        londonPostcodesUniqueLsoa("water_company"),
        londonPostcodesUniqueLsoa("quality"),
        londonPostcodesUniqueLsoa("income"),
        londonPostcodesUniqueLsoa("closeness_to_station")
      ))

//    locations.show()
    locations.write.mode("overwrite").format("delta").saveAsTable("location")
  }
}
