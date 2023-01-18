package com.example.bigdata

import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.types.IntegerType
import org.apache.spark.sql.functions.udf

object DimensionDate {
  private def convertDate(monthNum: Int, year: Int): Long = {
    year * 100 + monthNum
  }

  def main(args: Array[String]): Unit = {
    // Remember to delete `master` when not running locally
    val spark = SparkSession.builder.appName("DimensionDate").getOrCreate()
    import spark.implicits._

    val filepath1 = args(0)
    val filepath2 = args(1)
    val convertDateUdf = udf((month, year) => convertDate(month, year))

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

    val londonCrimes = londonCrimes1.union(londonCrimes2)

    val dates = (londonCrimes
      .where($"lsoa_code".isNotNull)
      .select($"year".cast(IntegerType).as("year"), $"month".cast(IntegerType).as("month"))
      .distinct()
      .withColumn("id", convertDateUdf($"month", $"year")))

//    dates.show()
    dates.write.mode("overwrite").format("delta").saveAsTable("date")
  }
}
