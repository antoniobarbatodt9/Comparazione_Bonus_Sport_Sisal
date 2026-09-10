// Renderer deterministico: fotogrammi PNG 970×250 dal template banner_scene.html
// Uso:
//   node render.mjs --times 0,0.4,1.2 --out ../06_storyboard/frames [--safe 1] [--bg <path>] [--scale 1] [--prefix scena]
//   node render.mjs --fps 25 --duration 9 --out ../09_preview/frames   (sequenza completa, solo dopo approvazione)
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import { mkdirSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const args = Object.fromEntries(process.argv.slice(2).reduce((a, x, i, arr) => { if (x.startsWith('--')) a.push([x.slice(2), arr[i + 1]]); return a; }, []));
const out = resolve(args.out || '../09_preview/frames');
mkdirSync(out, { recursive: true });
const scale = parseFloat(args.scale || '1');
let times = [];
if (args.times) times = args.times.split(',').map(Number);
else { const fps = parseFloat(args.fps || '25'), dur = parseFloat(args.duration || '9'); const n = Math.round(fps * dur); for (let i = 0; i < n; i++) times.push(i / fps); }

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 970, height: 250 }, deviceScaleFactor: scale });
const base = pathToFileURL(resolve(here, 'banner_scene.html')).href;
let i = 0;
for (const t of times) {
  const p = new URLSearchParams({ t: String(t) });
  if (args.safe) p.set('safe', args.safe);
  if (args.guide) p.set('guide', args.guide);
  if (args.bg) p.set('bg', args.bg);
  if (args.bgmode) p.set("bgmode", args.bgmode);
  if (args.theme) p.set("theme", args.theme);
  await page.goto(`${base}?${p.toString()}`);
  await page.waitForFunction(() => window.__ready === true);
  await page.evaluate(() => document.fonts.ready);
  const name = args.times ? `${args.prefix || 'frame'}_${String(i + 1).padStart(2, '0')}_t${t.toFixed(2)}s.png` : `f${String(i).padStart(4, '0')}.png`;
  await page.screenshot({ path: `${out}/${name}`, clip: { x: 0, y: 0, width: 970, height: 250 } });
  i++;
}
await browser.close();
console.log(`rendered ${times.length} frames → ${out}`);
