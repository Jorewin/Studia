import scala.io.Source

def power(x: Double, n: Int, m: Double=1.0): Double = {
  n match {
    case _ if n > 0 => n match {
      case _ if n % 2 == 0 => {
        val y = power(x, n / 2)
        y * y
      }
      case _ => x * power(x, n - 1)
    }
    case 0 => 1
    case _ => power(1 / x, -n)
  }
}

def australiaZones(): Array[String] = {
  val regex = "^Australia/(.*)$".r
  java.util.TimeZone.getAvailableIDs()
    .flatMap[String]({
      case regex(x) => Vector(x)
      case _ => Vector()
    })
    .sorted
}

def funTab1(tab: Seq[Int]): Seq[Int] = {
  tab.sorted
}

def funTab2(tab: Seq[Int]): Seq[Int] = {
  val (even, odd) = tab.partition(_ % 2 == 0)
  even.sorted concat odd.sorted(Ordering.Int.reverse)
}

def funTab3(tab: Seq[Int]): Seq[Int] = {
  tab.sortWith(_.abs < _.abs)
}

def myScalaApp(): Unit = {
  val file = "http://www.textfiles.com/etext/AUTHORS/DOYLE/doyle-hound-383.txt"
  val html = Source.fromURL(file)
  val s = html.mkString.replaceAll("""[\p{Punct}]""", "").toLowerCase()
  val tokens = s.split("\\W+").toList

  val words = tokens.groupMapReduce[String, Int]((value) => value)(_ => 1)(_ + _)

  println(words.toSeq.sortBy((value) => value._2)(Ordering.Int.reverse).take(3).mkString("\n"))
  println(s"${words.get("murder")}\n${words.get("scream")}\n${words.get("watson")}")
}

//myScalaApp()

def howManyZonesInRegions() = {
  val regex = "^([^/]+)/(.+)$".r
  java.util.TimeZone.getAvailableIDs()
    .groupBy {
      case regex(region, _) => region
      case _ => "invalid region"
    }
    .view
    .mapValues(_.length)
}

//println(funTab3(Seq.fill(100)(util.Random.nextInt(200)-100)))
println(howManyZonesInRegions().toSeq.mkString("\n"))