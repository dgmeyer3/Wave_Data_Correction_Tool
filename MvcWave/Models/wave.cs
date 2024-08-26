using System.ComponentModel.DataAnnotations;
using NetTopologySuite;
using NetTopologySuite.Geometries;

namespace MvcWave.Models;

public class Wave
{
    public int id { get; set; }
    public int timestamp { get; set; }
    public int min { get; set; }
    public int max { get; set; }
    public string? humanRelation { get; set; }
    public string? raw { get; set; }
    //in db, raw is of type string[]. setting up DBContext to accept string[] is very complex,
    //and i dont fully understand how it works. until i figure this out,
    //type was changed in db to string so edits on web work.
    public int optimalScore { get; set; }

    public bool? accurateRating { get; set; }
    public int? realMin { get; set; }
    public int? realMax { get; set; }
    public string? comments { get; set;}
}