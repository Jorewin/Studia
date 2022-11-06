TestDelegate testDelegate = new TestDelegate() {_s="new"};
TestDelegate.PrintIt printIt = new TestDelegate.PrintIt(TestDelegate.StaticPrintIt);
Console.WriteLine(printIt("Hello"));

TestDelegate.PrintIt printIt2 = new TestDelegate.PrintIt(testDelegate.MethodPrintIt);
Console.WriteLine(printIt2("Hi"));

public class TestDelegate
{
    public string _s = "";

    public static string StaticPrintIt(string s)
    {
        Console.WriteLine($"StaticPrintIt prints {s}");
        return "StaticPrintIt return value";
    }

    public delegate string PrintIt(string s);

    public string MethodPrintIt(string s)
    {
        Console.WriteLine($"MethodPrintIt prints {s} {this._s}");
        return "MethodPrintIt return value";
    }

    public PrintIt AnonymousPrintIt = new TestDelegate.PrintIt { return ""; };
}
