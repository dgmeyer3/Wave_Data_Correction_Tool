using System.ComponentModel.DataAnnotations;
 
namespace MvcWave.Models;

public class Wave
{
    public int timestamp { get; set; }
    public int min { get; set; }
    public int max { get; set; }
    public string? humanRelation { get; set; }
    public string? raw { get; set; }
    public int optimalScore { get; set; }
    public int id { get; set; }
    public bool? accurateRating { get; set; }
    public int? realMin { get; set; }
    public int? realMax { get; set; }
    public string? comments { get; set;}
}