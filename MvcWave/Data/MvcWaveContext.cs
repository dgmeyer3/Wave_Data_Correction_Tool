using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using MvcWave.Models;

namespace MvcWave.Data
{
    public class MvcWaveContext : DbContext
    {
        public MvcWaveContext (DbContextOptions<MvcWaveContext> options)
            : base(options)
        {
        }

        public DbSet<MvcWave.Models.Wave> Wave { get; set; } = default!;
    }
}
