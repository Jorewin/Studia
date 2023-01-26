namespace Backpack.Data;

using Microsoft.EntityFrameworkCore;
using Models;

public class DataContext : DbContext {
    public DataContext(DbContextOptions<DataContext> options): base(options) {}

    public DbSet<BackpackModel> BackpackModel => Set<BackpackModel>();

    public DbSet<ManufacturerModel> ManufacturerModel => Set<ManufacturerModel>();
}
