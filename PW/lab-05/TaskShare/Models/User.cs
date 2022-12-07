using Microsoft.EntityFrameworkCore;

namespace TaskShare.Models;

[Index(nameof(Pseudonym), IsUnique = true)]
public class User
{
    public int Id { get; set; }
    public string FirstName { get; set; }
    public string LastName { get; set; }
    public string Pseudonym { get; set; }
    public ICollection<Issue> Issues { get; set; } = new List<Issue>();
    public ICollection<Task> Tasks { get; set; } = new List<Task>();
}
