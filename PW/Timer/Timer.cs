public class Timer {
  public static int main()
  {
    Console.Clear();

    Timer.Timer timer = new Timer(System.DateTime.Parse("2022-10-13T18:20:00"))

    while (true)
    {
      Console.SetCursorPosition(Console.WindowWidth - 8, 0);
      Console.WriteLine(timer.);
      System.Threading.Thread.Sleep(1000);
    }
    return 0;
  }
}