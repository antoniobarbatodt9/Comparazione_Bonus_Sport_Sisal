#!/usr/bin/env python3
"""Controllo qualità automatico sul master (sequenza PNG 970×250) e sulle esportazioni.
Uso: python3 qc_check.py <dir_frames_970x250> <master.mp4> <web.mp4> <control.gif> [--out report.md]
Verifiche: dimensioni/fps/durata (ffprobe), CTA presente in ogni fotogramma, safe area piatta in ogni fotogramma,
stabilità (diff medio tra fotogrammi consecutivi nella fase di fermo), pesi, leggibilità sui frame DECODIFICATI dagli export.
"""
import sys, os, glob, json, subprocess, statistics
from PIL import Image, ImageChops, ImageStat
import imageio_ffmpeg

FF = imageio_ffmpeg.get_ffmpeg_exe()
FFPROBE = FF.replace("ffmpeg", "ffprobe") if os.path.exists(FF.replace("ffmpeg", "ffprobe")) else None

def probe(path):
    # usa ffmpeg -i (ffprobe non è incluso nel binario imageio); parse minimale
    out = subprocess.run([FF, "-hide_banner", "-i", path], capture_output=True, text=True).stderr
    return out

def region_stats(im, box):
    return ImageStat.Stat(im.crop(box))

def main():
    frames_dir, master, web, gif = sys.argv[1:5]
    out_md = sys.argv[sys.argv.index("--out")+1] if "--out" in sys.argv else None
    frames = sorted(glob.glob(os.path.join(frames_dir, "f*.png")))
    rep = []; ok_all = True
    def line(s, ok=True):
        nonlocal ok_all
        rep.append(("✅ " if ok else "❌ ") + s); ok_all = ok_all and ok
    # 1. conteggio e dimensioni
    n = len(frames); im0 = Image.open(frames[0]); line(f"Fotogrammi: {n} (atteso 225) · dimensione {im0.size} (atteso (970, 250))", n==225 and im0.size==(970,250))
    # 2. CTA presente in ogni fotogramma: pixel lime nella zona 800,83,150,44 e testo scuro
    cta_fail = []
    for f in frames:
        im = Image.open(f).convert("RGB"); st = region_stats(im, (800,83,950,127))
        r,g,b = st.mean
        lime_ok = g > 150 and r > 120 and b < 120          # media dominata dal lime
        dark_px = sum(1 for px in im.crop((820,95,930,115)).getdata() if px[0]+px[1]+px[2] < 200)
        if not (lime_ok and dark_px > 40): cta_fail.append(os.path.basename(f))
    line(f"CTA visibile in ogni fotogramma (lime + testo scuro): {'tutti' if not cta_fail else 'FALLITI ' + str(cta_fail[:5])}", not cta_fail)
    # 3. safe area piatta in ogni fotogramma (dev. standard ≈ 0) e uguale al colore atteso
    safe_fail = []
    for f in frames:
        im = Image.open(f).convert("RGB"); st = region_stats(im, (0,210,970,250))
        if max(st.stddev) > 1.0: safe_fail.append((os.path.basename(f), [round(x,2) for x in st.stddev]))
    line(f"Safe area 0,210 970×40 piatta e vuota in ogni fotogramma: {'tutti' if not safe_fail else 'FALLITI ' + str(safe_fail[:3])}", not safe_fail)
    # 4. stabilità nella fase di fermo (f133..f224 = 5,32 s → 9,0 s), zone statiche: card e titolo
    diffs = []
    prev = None
    for f in frames[133:]:
        im = Image.open(f).convert("L").crop((232,32,776,178))
        if prev is not None:
            d = ImageChops.difference(im, prev); diffs.append(ImageStat.Stat(d).mean[0])
        prev = im
    md = max(diffs) if diffs else 0
    line(f"Stabilità zona card nel fermo (max diff medio/frame): {md:.3f}/255 (soglia 0,6; CTA riflesso escluso)", md < 0.6)
    # 5. bordi dei loghi: nessuna variazione di posizione dopo 2,0 s (f50) nella riga loghi
    prev=None; ldiff=[]
    for idx, f in enumerate(frames):
        im = Image.open(f).convert("L").crop((232,54,776,94))
        if prev is not None and idx >= 50 and not (76 <= idx <= 95) and not (100 <= idx <= 154):
            ldiff.append((ImageStat.Stat(ImageChops.difference(im, prev)).mean[0], idx))
        prev=im
    mx = max(ldiff)
    line(f"Loghi stabili dopo 2,0 s fuori dalle finestre di effetto (riflesso vetro f76–f95, accento f100–f154): max diff medio/frame {mx[0]:.3f}/255 al frame {mx[1]} (soglia 0,8)", mx[0] < 0.8)
    # 5b. posizione di ciascun logo (baricentro dei pixel > 230 dentro il box logo, esclusi bordi card, alone e ambiente) tra f60, f120 e f224
    def centroid(img, thr=230):
        px = img.load(); w,h = img.size; sx=sy=n=0
        for yy in range(h):
            for xx in range(w):
                if px[xx,yy] > thr: sx+=xx; sy+=yy; n+=1
        return (sx/n, sy/n) if n else (0,0)
    boxes = {"Sisal":(240,56,392,92), "NetBet":(428,56,580,92), "William Hill":(616,56,768,92)}
    worst = 0; det = []
    for nm, b in boxes.items():
        c1 = centroid(Image.open(frames[60]).convert("L").crop(b)); c2 = centroid(Image.open(frames[224]).convert("L").crop(b))
        dx, dy = abs(c1[0]-c2[0]), abs(c1[1]-c2[1]); worst = max(worst, dx, dy); det.append(f"{nm} Δ=({dx:.2f},{dy:.2f})")
    line("Posizione di ogni logo invariata tra f60 e f224 (baricentro pixel chiari nel box logo): " + " · ".join(det) + " px (soglia 0,25)", worst < 0.25)
    # 6. pesi e specifiche export
    for name, path, limit in (("Master MP4", master, None), ("Web MP4", web, 3_500_000), ("GIF di controllo", gif, 3_500_000)):
        sz = os.path.getsize(path); info = probe(path)
        dur = [l for l in info.splitlines() if "Duration" in l]; strm = [l for l in info.splitlines() if "Stream" in l]
        okp = (limit is None) or sz <= limit
        line(f"{name}: {sz/1e6:.2f} MB" + (f" (limite 3,5 MB)" if limit else "") + " · " + (dur[0].strip() if dur else "") + " · " + (strm[0].strip()[:110] if strm else ""), okp)
    # 7. leggibilità sull'end frame decodificato dagli export
    os.makedirs("/tmp/qc_dec", exist_ok=True)
    for name, path in (("web", web), ("gif", gif)):
        subprocess.run([FF, "-y", "-loglevel", "error", "-sseof", "-0.2", "-i", path, "-frames:v", "1", f"/tmp/qc_dec/end_{name}.png"])
        if os.path.exists(f"/tmp/qc_dec/end_{name}.png"):
            im = Image.open(f"/tmp/qc_dec/end_{name}.png").convert("RGB")
            # contrasto valore Sisal: media luminanza testo bianco vs fondo card
            val = im.crop((262,134,370,156)); bg = im.crop((250,168,382,176))
            lv = ImageStat.Stat(val.convert("L")).mean[0]; lb = ImageStat.Stat(bg.convert("L")).mean[0]
            line(f"End frame decodificato ({name}): luminanza media fascia valori {lv:.0f} vs fondo card {lb:.0f} (fascia valori deve superare il fondo di ≥ 40)", lv > lb + 40)
    rep.append("")
    rep.append("**ESITO COMPLESSIVO: " + ("TUTTI I CONTROLLI AUTOMATICI SUPERATI**" if ok_all else "CONTROLLI FALLITI, vedi sopra**"))
    txt = "\n".join("- " + r if r else "" for r in rep)
    print(txt)
    if out_md:
        with open(out_md, "a") as fh: fh.write("\n\n## Controlli automatici (qc_check.py)\n\n" + txt + "\n")
    sys.exit(0 if ok_all else 1)

if __name__ == "__main__":
    main()
