package com.example.bigdata

import org.apache.spark.sql.
_
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
    val spark = SparkSession.builder.master("local").appName("DimensionLocation").getOrCreate()
    import spark.implicits._

    val londonPostcodesFilepath = args(0)
    val londonCrimesFilepath = args(1)

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

    val incomeClassifierUDF = functions.udf(incomeClassifier)
    val distanceClassifierUDF = functions.udf(distanceClassifier)

    londonPostcodes
      .withColumnRenamed("LSOA Code", "lsoa_code")
      .withColumnRenamed("County", "county")
      .withColumnRenamed("District", "district")
      .withColumnRenamed("Rural/urban", "rural/urban")
      .withColumnRenamed("Water company", "water_company")
      .withColumnRenamed("Quality", "quality")
      .withColumn("income", incomeClassifierUDF($"Income"))
      .withColumn("closness_to_station", distanceClassifierUDF($"Distance to station"))
      .join(londonCrimes, londonPostcodes("lsoa_code") === londonCrimes("lsoa_code"))
      .select(
        londonPostcodes("lsoa_code"),
        londonPostcodes("county"),
        londonPostcodes("district"),
        londonPostcodes("rural/urban"),
        londonPostcodes("water_company"),
        londonPostcodes("quality"),
        londonPostcodes("income"),
        londonPostcodes("closness_to_station")
      )
      .show()
  }
}
