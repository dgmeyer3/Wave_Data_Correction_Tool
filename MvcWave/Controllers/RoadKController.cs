using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using MvcMovie.Data;
using MvcWave.Models;

namespace MvcWave.Controllers
{
    public class RoadKController : Controller
    {
        private readonly MvcRoadKContext _context;

        public RoadKController(MvcRoadKContext context)
        {
            _context = context;
        }

        // GET: RoadK
        public async Task<IActionResult> Index(string searchString)
        {
            if(_context.RoadK == null)
            {
                return Problem("Entity set 'MvcWaveContext.Wave is null.");
            }
            var RoadKWaves = from w in _context.RoadK
                select w;

            if(!string.IsNullOrEmpty(searchString)){
               RoadKWaves = RoadKWaves.Where(q => q.timestamp.ToString()!.ToUpper().Contains(searchString.ToUpper()));
            }

            return View(await RoadKWaves.ToListAsync());
        }

        // GET: RoadK/Details/5
        public async Task<IActionResult> Details(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var roadK = await _context.RoadK
                .FirstOrDefaultAsync(m => m.id == id);
            if (roadK == null)
            {
                return NotFound();
            }

            return View(roadK);
        }

        // GET: RoadK/Create
        public IActionResult Create()
        {
            return View();
        }

        // POST: RoadK/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("id,timestamp,min,max,humanRelation,raw,optimalScore,accurateRating,realMin,realMax,comments")] RoadK roadK)
        {
            if (ModelState.IsValid)
            {
                _context.Add(roadK);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Index));
            }
            return View(roadK);
        }

        // GET: RoadK/Edit/5
        public async Task<IActionResult> Edit(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var roadK = await _context.RoadK.FindAsync(id);
            if (roadK == null)
            {
                return NotFound();
            }
            return View(roadK);
        }

        // POST: RoadK/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("id,timestamp,min,max,humanRelation,raw,optimalScore,accurateRating,realMin,realMax,comments")] RoadK roadK)
        {
            if (id != roadK.id)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Update(roadK);
                    await _context.SaveChangesAsync();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!RoadKExists(roadK.id))
                    {
                        return NotFound();
                    }
                    else
                    {
                        throw;
                    }
                }
                return RedirectToAction(nameof(Index));
            }
            return View(roadK);
        }

        // GET: RoadK/Delete/5
        public async Task<IActionResult> Delete(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var roadK = await _context.RoadK
                .FirstOrDefaultAsync(m => m.id == id);
            if (roadK == null)
            {
                return NotFound();
            }

            return View(roadK);
        }

        // POST: RoadK/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            var roadK = await _context.RoadK.FindAsync(id);
            if (roadK != null)
            {
                _context.RoadK.Remove(roadK);
            }

            await _context.SaveChangesAsync();
            return RedirectToAction(nameof(Index));
        }

        private bool RoadKExists(int id)
        {
            return _context.RoadK.Any(e => e.id == id);
        }
    }
}
