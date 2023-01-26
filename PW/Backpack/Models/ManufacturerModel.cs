namespace Backpack.Models;

using Microsoft.EntityFrameworkCore;

[Index(nameof(Name), IsUnique = true)]
public class ManufacturerModel {
    public int Id { get; set; }
    public String Name { get; set; } = "";
    public String Origin { get; set; } = "";
}
