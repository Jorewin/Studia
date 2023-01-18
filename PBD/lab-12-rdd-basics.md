8. 1891715
11.
    - numberOK: Int = 1701534
    - numberISE: Int = 62
    - numberNF: Int = 10845
12. numberISE (500) / numberOK (200) = 3.643771E-5
13. 237
    def getHost(line: String): String = {
        val pattern = """^([^.]+\.pl) .*$""".r
        line match {
            case pattern(host) => host
            case _ => ""
        }
    }
14. 3714
    def getPLOK(line: String): String = {
        val pattern = """^[^.]+\.pl .+ 200 \S+$""".r
        line match {
            case pattern() => line
            case _ => ""
        }
    }
    def getBytesPLOK(line: String): Int = {
        val pattern = """^[^.]+\.pl .+ 200 (\d+)$""".r
        line match {
            case pattern(bytes) => bytes.toInt
            case _ => -1
        }
    }

17. Array(GameInfo(Bad,Polaris SnoCross,/games/polaris-snocross/n64-11479,Nintendo 64,4.3,Racing,N,2001,1,25))
18. 7.495238095238094
