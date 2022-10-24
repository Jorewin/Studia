namespace lab_02 {
    public class Worker {
        public string Name { get; }
        public string Surname { get; }
        public Guid Id { get; }
        public int Birthday { get; }

        public Worker(string name, string surname, int birthday)
        {
            this.Name = name;
            this.Surname = surname;
            this.Id = System.Guid.NewGuid();
            this.Birthday = birthday;
        }

        new public string ToString()
        {
            return $"Worker({this.Name}, {this.Surname}, {this.Id}, {this.Birthday}";
        }
    }
}
