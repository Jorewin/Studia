namespace TaskShare.Models;

public class Status
{
    public int Id { get; set; }
    public enum Type {}
    public Type StatusType { get; set; }
    public bool Occured { get; set; }
    public Task Task { get; set; }
}
