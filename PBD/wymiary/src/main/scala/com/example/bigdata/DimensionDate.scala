package com.example.bigdata

import org.apache.spark.sql._

object DimensionDate {
  def main(args: Array[String]): Unit = {
    // Remember to delete `master` when not running locally
    val spark = SparkSession.builder.master("local").appName("DimensionDate").getOrCreate()
    import spark.implicits._

    val filepath = args(0)

    val londonCrimes = (spark
      .read
      .format("org.apache.spark.csv")
      .option("header", value = true)
      .option("inferSchema", value = true)
      .load(filepath))

    londonCrimes
      .select($"year", $"month")
      .show()
  }
}
