using Microsoft.EntityFrameworkCore;

namespace TaskShare.Models;

[Index(nameof(Label), IsUnique = true)]
public class Task {
    public int Id { get; set; }
    public string Label { get; set; }
    public string Description { get; set; }
    public int TimeCost { get; set; }
    public int Priority { get; set; }
    public User User { get; set; }
    public Issue Issue { get; set; }
    public ICollection<Status> Statuses { get; set; } = new List<Status>();
}
