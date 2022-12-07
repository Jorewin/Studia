using Microsoft.EntityFrameworkCore;

namespace TaskShare.Models;

[Index(nameof(Label), IsUnique = true)]
public class Issue
{
    public int Id { get; set; }
    public string Label { get; set; }
    public string Description { get; set; }
    public ICollection<User> Users { get; set; } = new List<User>();
    public ICollection<Task> Tasks { get; set; } = new List<Task>();
}
