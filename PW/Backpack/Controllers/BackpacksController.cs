
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Backpack.Data;
using Backpack.Models;
using Microsoft.AspNetCore.Mvc.Rendering;

namespace Backpack.Controllers
{
    public class BackpacksController : Controller
    {
        private readonly DataContext _context;

        public BackpacksController(DataContext context)
        {
            _context = context;
        }

        // GET: Backpacks
        public async Task<IActionResult> Index(string searchString)
        {
            var backpacks = _context.BackpackModel.AsQueryable();

            if (!String.IsNullOrEmpty(searchString))
            {
                ViewData["searchString"] = searchString;
                backpacks = backpacks.Where((b) => b.Name.Contains(searchString) || b.Description.Contains(searchString) || b.Type.Equals(searchString));
            }

            return View(await backpacks.ToListAsync());
        }

        // GET: Backpacks/Details/5
        public async Task<IActionResult> Details(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var backpackModel = await _context.BackpackModel
                .Include("Manufacturer")
                .FirstOrDefaultAsync(m => m.Id == id);
            if (backpackModel == null)
            {
                return NotFound();
            }

            return View(backpackModel);
        }

        // GET: Backpacks/Create
        public IActionResult Create()
        {
            ViewData["manufacturers"] = _context.ManufacturerModel.ToList().ConvertAll(m => new SelectListItem { Value = $"{m.Id}", Text = m.Name});
            return View();
        }

        // POST: Backpacks/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Id,Name,Description,Capacity,Type,ManufacturerId")] BackpackModel backpackModel)
        {
            if (ModelState.IsValid)
            {
                backpackModel.Manufacturer = (await _context.ManufacturerModel.FindAsync(backpackModel.ManufacturerId))!;
                _context.Add(backpackModel);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Index));
            }

            ViewData["manufacturers"] = new SelectList(_context.ManufacturerModel.ToList(), "Id", "Name", backpackModel!.Manufacturer);

            return View(backpackModel);
        }

        // GET: Backpacks/Edit/5
        public async Task<IActionResult> Edit(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var backpackModel = await _context.BackpackModel
                .Include("Manufacturer")
                .FirstOrDefaultAsync(m => m.Id == id);

            if (backpackModel == null)
            {
                return NotFound();
            }

            ViewData["manufacturers"] = new SelectList(_context.ManufacturerModel.ToList(), "Id", "Name", backpackModel!.Manufacturer);

            return View(backpackModel);
        }

        // POST: Backpacks/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("Id,Name,Description,Capacity,Type,ManufacturerId")] BackpackModel backpackModel)
        {
            if (id != backpackModel.Id)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    backpackModel.Manufacturer = (await _context.ManufacturerModel.FindAsync(backpackModel.ManufacturerId))!;
                    _context.Update(backpackModel);
                    await _context.SaveChangesAsync();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!BackpackModelExists(backpackModel.Id))
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

            ViewData["manufacturers"] = new SelectList(_context.ManufacturerModel.ToList(), "Id", "Name", backpackModel!.Manufacturer);

            return View(backpackModel);
        }

        // GET: Backpacks/Delete/5
        public async Task<IActionResult> Delete(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var backpackModel = await _context.BackpackModel
                .FirstOrDefaultAsync(m => m.Id == id);
            if (backpackModel == null)
            {
                return NotFound();
            }

            return View(backpackModel);
        }

        // POST: Backpacks/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            var backpackModel = await _context.BackpackModel.FindAsync(id);
            if (backpackModel != null)
            {
                _context.BackpackModel.Remove(backpackModel);
            }

            await _context.SaveChangesAsync();
            return RedirectToAction(nameof(Index));
        }

        private bool BackpackModelExists(int id)
        {
          return (_context.BackpackModel?.Any(e => e.Id == id)).GetValueOrDefault();
        }
    }
}
