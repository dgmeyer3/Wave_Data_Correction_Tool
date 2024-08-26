using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using MvcWave.Data;
using MvcWave.Models;

namespace MvcWave.Controllers
{
    public class WaveController : Controller
    {
        private readonly MvcWaveContext _context;

        public WaveController(MvcWaveContext context)
        {
            _context = context;
        }

        // GET: Wave
        public async Task<IActionResult> Index(string searchString){
            if(_context.Wave == null){
                return Problem("Entity set 'MvcWaveContext.Wave is null.");
            }

            var waves = from w in _context.Wave
                select w;

            if(!string.IsNullOrEmpty(searchString)){
               waves = waves.Where(q => q.timestamp.ToString()!.ToUpper().Contains(searchString.ToUpper()));
            }

            return View(await waves.ToListAsync());
        }

        // GET: Wave/Details/5
        public async Task<IActionResult> Details(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var wave = await _context.Wave
                .FirstOrDefaultAsync(m => m.id == id);
            if (wave == null)
            {
                return NotFound();
            }

            return View(wave);
        }

        // GET: Wave/Create
        public IActionResult Create()
        {
            return View();
        }

        // POST: Wave/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("timestamp,min,max,humanRelation,raw,optimalScore,id,accurateRating,realMin,realMax,comments")] Wave wave)
        {
            if (ModelState.IsValid)
            {
                _context.Add(wave);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Index));
            }
            return View(wave);
        }

        // GET: Wave/Edit/5
        public async Task<IActionResult> Edit(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var wave = await _context.Wave.FindAsync(id);
            if (wave == null)
            {
                return NotFound();
            }
            return View(wave);
        }

        // POST: Wave/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("timestamp,min,max,humanRelation,raw,optimalScore,id,accurateRating,realMin,realMax,comments")] Wave wave)
        {
            if (id != wave.id)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Update(wave);
                    await _context.SaveChangesAsync();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!WaveExists(wave.id))
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
            return View(wave);
        }

        // GET: Wave/Delete/5
        public async Task<IActionResult> Delete(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var wave = await _context.Wave
                .FirstOrDefaultAsync(m => m.id == id);
            if (wave == null)
            {
                return NotFound();
            }

            return View(wave);
        }

        // POST: Wave/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            var wave = await _context.Wave.FindAsync(id);
            if (wave != null)
            {
                _context.Wave.Remove(wave);
            }

            await _context.SaveChangesAsync();
            return RedirectToAction(nameof(Index));
        }

        private bool WaveExists(int id)
        {
            return _context.Wave.Any(e => e.id == id);
        }
    }
}
