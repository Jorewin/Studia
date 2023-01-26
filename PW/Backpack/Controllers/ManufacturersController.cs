using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Backpack.Data;
using Backpack.Models;

namespace Backpack.Controllers
{
    public class ManufacturersController : Controller
    {
        private readonly DataContext _context;

        public ManufacturersController(DataContext context)
        {
            _context = context;
        }

        // GET: Manufacturers
        public async Task<IActionResult> Index(string searchString)
        {
            var manufacturers = _context.ManufacturerModel.AsQueryable();

            if (!String.IsNullOrEmpty(searchString))
            {
                ViewData["searchString"] = searchString;
                manufacturers = manufacturers.Where((m) => m.Name.Contains(searchString) || m.Origin.Contains(searchString));
            }

            return View(await manufacturers.ToListAsync());
        }

        // GET: Manufacturers/Details/5
        public async Task<IActionResult> Details(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var manufacturerModel = await _context.ManufacturerModel
                .FirstOrDefaultAsync(m => m.Id == id);
            if (manufacturerModel == null)
            {
                return NotFound();
            }

            return View(manufacturerModel);
        }

        // GET: Manufacturers/Create
        public IActionResult Create()
        {
            return View();
        }

        // POST: Manufacturers/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Id,Name,Origin")] ManufacturerModel manufacturerModel)
        {
            if (ModelState.IsValid)
            {
                _context.Add(manufacturerModel);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Index));
            }
            return View(manufacturerModel);
        }

        // GET: Manufacturers/Edit/5
        public async Task<IActionResult> Edit(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var manufacturerModel = await _context.ManufacturerModel.FindAsync(id);
            if (manufacturerModel == null)
            {
                return NotFound();
            }
            return View(manufacturerModel);
        }

        // POST: Manufacturers/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("Id,Name,Origin")] ManufacturerModel manufacturerModel)
        {
            if (id != manufacturerModel.Id)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Update(manufacturerModel);
                    await _context.SaveChangesAsync();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!ManufacturerModelExists(manufacturerModel.Id))
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
            return View(manufacturerModel);
        }

        // GET: Manufacturers/Delete/5
        public async Task<IActionResult> Delete(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var manufacturerModel = await _context.ManufacturerModel
                .FirstOrDefaultAsync(m => m.Id == id);
            if (manufacturerModel == null)
            {
                return NotFound();
            }

            return View(manufacturerModel);
        }

        // POST: Manufacturers/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            var manufacturerModel = await _context.ManufacturerModel.FindAsync(id);
            if (manufacturerModel != null)
            {
                _context.ManufacturerModel.Remove(manufacturerModel);
            }

            await _context.SaveChangesAsync();
            return RedirectToAction(nameof(Index));
        }

        private bool ManufacturerModelExists(int id)
        {
          return (_context.ManufacturerModel?.Any(e => e.Id == id)).GetValueOrDefault();
        }
    }
}
