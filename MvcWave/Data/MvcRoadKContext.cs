using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using MvcWave.Models;

namespace MvcMovie.Data
{
    public class MvcRoadKContext : DbContext
    {
        public MvcRoadKContext (DbContextOptions<MvcRoadKContext> options)
            : base(options)
        {
        }

        public DbSet<MvcWave.Models.RoadK> RoadK { get; set; } = default!;
    }
}
