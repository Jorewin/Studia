TestDelegate testDelegate = new TestDelegate() {_s="new", printIt = TestDelegate.StaticPrintIt};
Console.WriteLine(testDelegate.printIt("Hello"));

TestDelegate testDelegate2 = new TestDelegate() {_s="new2", printIt = testDelegate.MethodPrintIt};
Console.WriteLine(testDelegate2.printIt("Hi"));

TestDelegate testDelegate3 = new TestDelegate() {_s="new3", printIt = TestDelegate.StaticPrintIt};
testDelegate3.printIt += testDelegate.MethodPrintIt;
Console.WriteLine(testDelegate3.printIt("Bonjour"));

TestDelegate testDelegate4 = new TestDelegate() {_s="new4"};
Console.WriteLine(testDelegate4.printIt("Hola"));

public delegate string PrintIt(string s);
public delegate string PrintItAnonymous(string s);

public class TestDelegate
{
    public TestDelegate()
    {
        this.printIt = delegate(string s)
        {
            Console.WriteLine($"AnonymousPrintIt prints {s} {this._s} {this._t}");
            return "AnonymousPrintIt return value";
        };
    }

    public string _s = "";
    private string _t = "secret";

    public PrintIt printIt;
    public static string StaticPrintIt(string s)
    {
        Console.WriteLine($"StaticPrintIt prints {s}");
        return "StaticPrintIt return value";
    }


    public string MethodPrintIt(string s)
    {
        Console.WriteLine($"MethodPrintIt prints {s} {this._s}");
        return "MethodPrintIt return value";
    }

//    public PrintIt AnonymousPrintIt = new TestDelegate.PrintIt { return ""; };
}
