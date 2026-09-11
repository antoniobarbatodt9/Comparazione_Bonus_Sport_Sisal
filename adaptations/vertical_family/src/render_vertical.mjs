// Render deterministico della famiglia verticale. Uso:
//   node render_vertical.mjs --size 300x600 --times 0.6,1.5 --out ../300x600/storyboard --prefix sb [--mode wire|final] [--safe 1] [--grid 1] [--scale 1]
//   node render_vertical.mjs --size 160x600 --fps 25 --duration 10 --out <dir>     (sequenza completa: SOLO dopo approvazione)
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import { mkdirSync } from 'node:fs'; import { resolve, dirname } from 'node:path'; import { fileURLToPath, pathToFileURL } from 'node:url';
const here = dirname(fileURLToPath(import.meta.url));
const args = Object.fromEntries(process.argv.slice(2).reduce((a, x, i, arr) => { if (x.startsWith('--')) a.push([x.slice(2), arr[i + 1]]); return a; }, []));
const size = args.size || '300x600'; const [W, H] = size.split('x').map(Number); const out = resolve(args.out || '.'); mkdirSync(out, { recursive: true });
const scale = parseFloat(args.scale || '1');
let times = []; if (args.times) times = args.times.split(',').map(Number); else { const fps = parseFloat(args.fps || '25'), dur = parseFloat(args.duration || '10'); for (let i = 0; i < Math.round(fps * dur); i++) times.push(i / fps); }
const browser = await chromium.launch(); const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: scale });
const base = pathToFileURL(resolve(here, 'banner_vertical.html')).href; let i = 0; const boxes = [];
for (const t of times) { const p = new URLSearchParams({ size, t: String(t) }); for (const k of ['mode', 'safe', 'grid', 'bgmode']) if (args[k]) p.set(k, args[k]);
  await page.goto(`${base}?${p.toString()}`); await page.waitForFunction(() => window.__ready === true); await page.evaluate(() => document.fonts.ready);
  const name = args.times ? `${args.prefix || 'frame'}_${String(i + 1).padStart(2, '0')}_t${t.toFixed(2)}s.png` : `f${String(i).padStart(4, '0')}.png`;
  await page.screenshot({ path: `${out}/${name}`, clip: { x: 0, y: 0, width: W, height: H } });
  if (args.measure) boxes.push({ t, ...(await page.evaluate(() => { const r = e => { const b = e.getBoundingClientRect(); return [Math.round(b.left*10)/10, Math.round(b.top*10)/10, Math.round(b.width*10)/10, Math.round(b.height*10)/10]; };
    const vis = e => e && getComputedStyle(e).display !== 'none' && e.closest('.scene') ? getComputedStyle(e.closest('.scene')).display !== 'none' : true;
    const o = { cta: r(document.querySelector('#cta')), ctaOpacity: getComputedStyle(document.querySelector('#cta')).opacity };
    document.querySelectorAll('.card').forEach((c, k) => { if (vis(c)) o['card' + k] = { box: r(c), logo: r(c.querySelector('.logo img')), fino: r(c.querySelector('.fino')), val: r(c.querySelector('.val')), op: c.dataset.op, opacity: getComputedStyle(c).opacity }; });
    ['w1', 'w2', 't1', 't2', 'r1', 'r5'].forEach(id => { const e = document.getElementById(id); if (e && vis(e) && getComputedStyle(e).display !== 'none') o[id] = r(e); });
    return o; })) });
  i++; }
await browser.close(); if (args.measure) console.log(JSON.stringify(boxes)); else console.log(`rendered ${times.length} frames → ${out}`);
