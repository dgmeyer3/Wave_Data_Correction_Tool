using Microsoft.AspNetCore.Mvc.Rendering;
using System.Collections.Generic;

namespace MvcWave.Models;

//use this model to filter sort rows by optimal score
public class WaveScoreModel
{
    public List<Wave>? Waves { get; set; }
    public SelectList? OptimalScores { get; set; }
    public string? WaveScore { get; set; }
    public string? SearchString { get; set; }
}