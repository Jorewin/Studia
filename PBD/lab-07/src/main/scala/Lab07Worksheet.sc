def power(x: Double, n: Int, m: Double=1.0): Double =
{
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

println("power 2,3 z : " + power(2, 3))
