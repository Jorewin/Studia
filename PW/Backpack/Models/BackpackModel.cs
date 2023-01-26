namespace Backpack.Models;

using Microsoft.EntityFrameworkCore;

[Index(nameof(Name), IsUnique = true)]
public class BackpackModel {
    public int Id { get; set; }
    public String Name { get; set; } = "";
    public String Description { get; set; } = "";
    public float Capacity { get; set; }
    public BackpackType Type { get; set; }
    public int ManufacturerId { get; set; }
    public ManufacturerModel Manufacturer { get; set; } = new();
}