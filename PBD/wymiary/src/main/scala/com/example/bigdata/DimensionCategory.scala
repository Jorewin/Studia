package com.example.bigdata

import org.apache.spark.sql._

object DimensionCategory {
  def main(args: Array[String]): Unit = {
    // Remember to delete `master` when not running locally
    val spark = SparkSession.builder.master("local").appName("DimensionCategory").getOrCreate()
    import spark.implicits._

    val filepath1 = args(0)
    val filepath2 = args(1)

    val londonCrimes1 = (spark
      .read
      .format("csv")
      .option("header", value = true)
      .option("inferSchema", value = true)
      .load(filepath1))

    val londonCrimes2 = (spark
      .read
      .format("csv")
      .option("header", value = true)
      .option("inferSchema", value = true)
      .load(filepath2))

    val londonCrimes = londonCrimes1.union(londonCrimes2).dropDuplicates()

    val categories = (londonCrimes
      .where($"lsoa_code".isNotNull)
      .withColumnRenamed("major_category", "major")
      .withColumnRenamed("minor_category", "minor")
      .select($"major", $"minor"))

    categories.show()
  }
}
