OfficeWorker officeWorker = new OfficeWorker("Stefan", "Kowalski", 1887) {
    Name = "Rafał",
    Surname = "Rafał",
    BirthYear = 1923,
};
((IPrintable)officeWorker).Print();

interface IPrintable
{
    public Guid Id { get; set; }

    public void Print()
    {
        Console.WriteLine("IPrintable prints");
    }
}

interface IPublicPrintable
{
    public void Print()
    {
        Console.WriteLine("IPublicPrintable prints");
    }
}

public abstract class Worker: IPrintable
{
    public string Name { get; set; }
    public string Surname { get; set; }
    public Guid Id { get; set; } = Guid.NewGuid();
    public int BirthYear { get; set; }

    public override string ToString()
    {
        return $"Worker(name: {this.Name}, surname: {this.Surname}, id: {this.Id}, birthyear: {this.BirthYear}";
    }

    public void GenerateNewId()
    {
        this.Id = Guid.NewGuid();
    }

    protected Worker(string name, string surname, int birthYear)
    {
        this.Name = name;
        this.Surname = surname;
        this.BirthYear = birthYear;
    }
}

public sealed class OfficeWorker: Worker
{
    public OfficeWorker(string name, string surname, int birthYear): base(name, surname, birthYear) {}

    public void Print()
    {
//        ((IPrintable)this).Print();
        Console.WriteLine("OfficeWorker prints");
    }
}

public class Manager: Worker
{
    public Manager(string name, string surname, int birthYear): base(name, surname, birthYear) {}

    public override string ToString()
    {
        return $"Manager(name: {this.Name}, surname: {this.Surname}, id: {this.Id}, birthyear: {this.BirthYear}";
    }
}

public class Supervisor: Manager
{
    public Supervisor(string name, string surname, int birthYear): base(name, surname, birthYear) {}

    public override string ToString()
    {
        return $"Supervisor(name: {this.Name}, surname: {this.Surname}, id: {this.Id}, birthyear: {this.BirthYear}";
    }
}