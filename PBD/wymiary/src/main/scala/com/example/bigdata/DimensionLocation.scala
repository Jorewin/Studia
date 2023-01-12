package com.example.bigdata

import org.apache.spark.sql._
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
    // TODO: decide what should we do with null values in `quality`, `income` and `closness_to_station`
    // TODO: decide on id method generation ex. LSOA and date hash
    // Remember to delete `master` when not running locally
    val spark = SparkSession.builder.master("local").appName("DimensionLocation").getOrCreate()
    import spark.implicits._

    val londonCrimesFilepath = args(0)
    val londonPostcodesFilepath = args(1)

    val londonCrimes = (spark
      .read
      .format("org.apache.spark.csv")
      .option("header", value = true)
      .option("inferSchema", value = true)
      .load(londonCrimesFilepath))

    val londonPostcodes = (spark
      .read
      .format("org.apache.spark.csv")
      .option("header", value = true)
      .option("inferSchema", value = true)
      .load(londonPostcodesFilepath))

    val incomeClassifierUDF = udf(incomeClassifier)
    val distanceClassifierUDF = udf(distanceClassifier)

    val londonPostcodesUniqueLsoa = (londonPostcodes
      .withColumnRenamed("LSOA Code", "lsoa_code")
      .withColumnRenamed("County", "county")
      .withColumnRenamed("District", "district")
      .withColumnRenamed("Rural/urban", "rural/urban")
      .withColumnRenamed("Water company", "water_company")
      .withColumnRenamed("Quality", "quality")
      .withColumnRenamed("Income", "income_numerical")
      .withColumnRenamed("Distance to station", "closness_to_station_numerical")
      .select(
        $"lsoa_code",
        $"county",
        $"district",
        $"rural/urban",
        $"water_company",
        $"quality",
        $"income_numerical",
        $"closness_to_station_numerical"
      )
      .groupBy($"lsoa_code")
      .agg(
        first($"county", ignoreNulls = true),
        first($"district", ignoreNulls = true),
        first($"rural/urban", ignoreNulls = true),
        first($"water_company", ignoreNulls = true),
        first($"quality", ignoreNulls = true),
        avg($"income_numerical"),
        avg($"closness_to_station_numerical")
      )
      .withColumn("income", incomeClassifierUDF($"income_numerical"))
      .withColumn("closness_to_station", distanceClassifierUDF($"closness_to_station_numerical"))
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
        londonPostcodesUniqueLsoa("closness_to_station")
      )
    )

    locations.show()
  }
}
