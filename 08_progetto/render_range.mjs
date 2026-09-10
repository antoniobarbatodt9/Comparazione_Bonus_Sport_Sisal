// Re-render di un intervallo di fotogrammi (f<from>..f<to>) nella cartella sequenza esistente, stessi nomi f%04d.png
// Uso: node render_range.mjs --from 268 --to 299 --out ../09_preview/M_master_frames_2x --scale 2 --bgmode drift [--fps 25]
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import { resolve, dirname } from 'node:path'; import { fileURLToPath, pathToFileURL } from 'node:url';
const here = dirname(fileURLToPath(import.meta.url));
const args = Object.fromEntries(process.argv.slice(2).reduce((a, x, i, arr) => { if (x.startsWith('--')) a.push([x.slice(2), arr[i + 1]]); return a; }, []));
const out = resolve(args.out); const scale = parseFloat(args.scale || '1'); const fps = parseFloat(args.fps || '25');
const browser = await chromium.launch(); const page = await browser.newPage({ viewport: { width: 970, height: 250 }, deviceScaleFactor: scale });
const base = pathToFileURL(resolve(here, 'banner_scene.html')).href;
for (let i = parseInt(args.from); i <= parseInt(args.to); i++) {
  const p = new URLSearchParams({ t: String(i / fps) }); if (args.bgmode) p.set('bgmode', args.bgmode); if (args.bg) p.set('bg', args.bg);
  await page.goto(`${base}?${p.toString()}`); await page.waitForFunction(() => window.__ready === true); await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: `${out}/f${String(i).padStart(4, '0')}.png`, clip: { x: 0, y: 0, width: 970, height: 250 } });
}
await browser.close(); console.log(`re-rendered f${args.from}..f${args.to} → ${out}`);
