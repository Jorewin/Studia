package com.example.bigdata

import org.apache.spark.sql.SparkSession

object DimensionAirQuality {
  private case class Air(
    id: Long,
    nitric_oxide_density: String,
    nitrogen_dioxide_density: String,
    oxides_of_nitrogen_density: String,
    ozone_density: String
  )

  private def convertDate(data: String): Long = {
    val dateRegex = "(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)-(\\d{2})".r
    val (month, year) = dateRegex.findFirstMatchIn(data) match {
      case Some(found) => (found.group(1), found.group(2))
      case _ => throw new Exception()
    }

    val monthNum = month match {
      case "Jan" => 1
      case "Feb" => 2
      case "Mar" => 3
      case "Apr" => 4
      case "May" => 5
      case "Jun" => 6
      case "Jul" => 7
      case "Aug" => 8
      case "Sep" => 9
      case "Oct" => 10
      case "Nov" => 11
      case "Dec" => 12
    }

    monthNum * 100 + year.toInt
  }

  private def stringToAir(line: String): Air = {
    val nitric_oxide_density_regex = "Nitric Oxide: (\\d+\\.\\d+)".r
    val nitrogen_dioxide_density_regex = "Nitrogen Dioxide: (\\d+\\.\\d+)".r
    val oxides_of_nitrogen_density_regex = "Oxides of Nitrogen: (\\d+\\.\\d+)".r
    val ozone_density_regex = "Ozone: (\\d+\\.\\d+)".r

    val id = convertDate(line)

    val nitric_oxide_density_numerical = nitric_oxide_density_regex.findFirstMatchIn(line) match {
      case Some(found) => found.group(1).toFloat
      case _ => 70.6f
    }

    val nitric_oxide_density = (
      if (nitric_oxide_density_numerical > 94.8) "bad" else
      if (nitric_oxide_density_numerical > 54.6) "neutral" else
      "good"
    )

    val nitrogen_dioxide_density_numerical = nitrogen_dioxide_density_regex.findFirstMatchIn(line) match {
      case Some(found) => found.group(1).toFloat
      case _ => 54.7f
    }

    val nitrogen_dioxide_density = (
      if (nitrogen_dioxide_density_numerical > 60.25) "bad" else
      if (nitrogen_dioxide_density_numerical > 48.6) "neutral" else
      "good"
    )

    val oxides_of_nitrogen_density_numerical = oxides_of_nitrogen_density_regex.findFirstMatchIn(line) match {
      case Some(found) => found.group(1).toFloat
      case _ => 129.3f
    }

    val oxides_of_nitrogen_density = (
      if (oxides_of_nitrogen_density_numerical > 156.6) "bad" else
      if (oxides_of_nitrogen_density_numerical > 114.1) "neutral" else
      "good"
    )

    val ozone_density_numerical = ozone_density_regex.findFirstMatchIn(line) match {
      case Some(found) => found.group(1).toFloat
      case _ => 26.4f
    }

    val ozone_density = (
      if (ozone_density_numerical > 33.7) "bad" else
      if (ozone_density_numerical > 21.0f) "neutral" else
      "good"
    )

    Air(id, nitric_oxide_density, nitrogen_dioxide_density, oxides_of_nitrogen_density, ozone_density)
  }

  def main(args: Array[String]): Unit = {
    // Remember to delete `master` when not running locally
    val spark = SparkSession.builder.appName("DimensionDate").getOrCreate()

    val filepath1 = args(0)

    val londonAirQuality = spark.sparkContext.textFile(filepath1)

    val airQualities = spark.createDataFrame(
      londonAirQuality.map(line => stringToAir(line))
    ).dropDuplicates("id")

//    airQualities.show()
    airQualities.write.mode("overwrite").format("delta").saveAsTable("air_quality")
  }
}
