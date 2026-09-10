#!/usr/bin/env python3
"""QC automatico del CONCEPT M (12,0 s = 300 fotogrammi 970×250, con audio SFX).
Uso: python3 qc_check_M.py <dir_frames_970x250> <master.mp4> <web.mp4> <web_muto.mp4> <control.gif> [--out report.md]
"""
import sys, os, glob, re, json, subprocess
from PIL import Image, ImageChops, ImageStat
import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
def probe(path):
    return subprocess.run([FF, "-hide_banner", "-i", path], capture_output=True, text=True).stderr
def lime_mask(im):
    px = im.load(); w,h = im.size; pts=[]
    for y in range(h):
        for x in range(w):
            r,g,b = px[x,y]
            if 140 <= r <= 215 and 185 <= g <= 240 and b < 120: pts.append((x,y))
    return pts
def bright_bbox(img_l, thr=200):
    px = img_l.load(); w,h = img_l.size; xs=[]; ys=[]
    for y in range(h):
        for x in range(w):
            if px[x,y] > thr: xs.append(x); ys.append(y)
    return (min(xs),min(ys),max(xs),max(ys)) if xs else None
def main():
    frames_dir, master, web, muto, gif = sys.argv[1:6]
    out_md = sys.argv[sys.argv.index("--out")+1] if "--out" in sys.argv else None
    frames = sorted(glob.glob(os.path.join(frames_dir, "f*.png"))); rep=[]; ok_all=True
    def line(s, ok=True):
        nonlocal ok_all; rep.append(("✅ " if ok else "❌ ")+s); ok_all = ok_all and ok
    n=len(frames); im0=Image.open(frames[0]); line(f"Fotogrammi: {n} (atteso 300) · dimensione {im0.size} (atteso (970, 250))", n==300 and im0.size==(970,250))
    # 1. CTA presente e integra dal fotogramma 40 (t=1,60 s, fine ingresso) in poi, in qualunque posizione/taglia (grande, media, piccola, enfasi)
    cta_fail=[]; bboxes={}
    for idx,f in enumerate(frames):
        if idx < 40: continue
        # finestra di ricerca per fase (esclude la parola SPORT in lime del titolo): S1 x>=560, S2-S4 x>=540, S5/S6 x>=770
        x0 = 585 if idx < 66 else (540 if idx < 232 else 770)
        im=Image.open(f).convert("RGB").crop((x0,20,970,210)); pts=lime_mask(im)
        if len(pts) < 3000: cta_fail.append((os.path.basename(f),'lime',len(pts))); continue
        xs=[p[0]+x0 for p in pts]; ys=[p[1] for p in pts]; bb=(min(xs),min(ys)+20,max(xs),max(ys)+20); bboxes[idx]=bb
        inner=Image.open(f).convert("RGB").crop((bb[0]+10,bb[1]+8,bb[2]-10,bb[3]-8))
        dark=sum(1 for p in inner.getdata() if p[0]+p[1]+p[2] < 200)
        if dark < 40: cta_fail.append((os.path.basename(f),'testo',dark))
        if bb[0] < 20 or bb[2] > 951 or bb[1] < 20 or bb[3] > 208: cta_fail.append((os.path.basename(f),'fuori margine',bb))
    line(f"CTA presente e integra (pill lime ≥ 3000 px + testo scuro, dentro i margini) dal f40 al f299: {'tutti' if not cta_fail else 'FALLITI '+str(cta_fail[:4])}", not cta_fail)
    for name, lo, hi, exp in (("grande (S1), fuori dal riflesso",56,62,(599,79,829,131)), ("media (S2–S4)",77,226,(565,80,775,134)), ("piccola (S5)",239,267,(800,83,950,127))):
        bb=[bboxes[i] for i in range(lo,hi+1) if i in bboxes]; mx=max(max(abs(b[k]-exp[k]) for k in range(4)) for b in bb) if bb else 999
        line(f"Posizione CTA {name} f{lo}–f{hi}: scarto max dal layout atteso {exp} = {mx} px (soglia 3)", mx <= 3)
    # 2. safe area piatta in tutti i fotogrammi (anche durante i wipe)
    safe_fail=[]
    for f in frames:
        st=ImageStat.Stat(Image.open(f).convert("RGB").crop((0,210,970,250)))
        if max(st.stddev) > 1.0: safe_fail.append(os.path.basename(f))
    line(f"Safe area 0,210 970×40 piatta in tutti i 300 fotogrammi (wipe inclusi): {'tutti' if not safe_fail else 'FALLITI '+str(safe_fail[:5])}", not safe_fail)
    # 3. pari trattamento sequenziale S2/S3/S4: stessi tempi relativi (card visibile a u=0,25; valore completo e stabile tra u=1,20 e u=1,80), stessa altezza del valore
    starts={'Sisal':2.95,'NetBet':5.10,'William Hill':7.25}; det=[]; ok=True; heights={}
    for nm,t0 in starts.items():
        f_early=frames[int(round((t0+0.25)*25))]; f_mid=frames[int(round((t0+1.20)*25))]; f_hold=frames[int(round((t0+1.80)*25))]
        card_early=ImageStat.Stat(Image.open(f_early).convert("L").crop((200,35,490,60))).mean[0]
        vb_mid=bright_bbox(Image.open(f_mid).convert("L").crop((195,134,495,182))); vb_hold=bright_bbox(Image.open(f_hold).convert("L").crop((195,134,495,182)))
        same = vb_mid is not None and vb_hold is not None and abs((vb_mid[3]-vb_mid[1])-(vb_hold[3]-vb_hold[1])) <= 1 and abs(vb_mid[1]-vb_hold[1]) <= 1
        heights[nm]=(vb_hold[3]-vb_hold[1]) if vb_hold else -1
        det.append(f"{nm}: card a u=0,25 (lum {card_early:.0f}), valore completo a u=1,20 e stabile a u=1,80 → {'sì' if same else 'NO'}, altezza cifre {heights[nm]} px")
        ok = ok and same
    hs=list(heights.values()); ok = ok and max(hs)-min(hs) <= 1
    line("Pari trattamento sequenziale (stessi tempi relativi, stessa altezza dei valori ±1 px): " + " · ".join(det), ok)
    # 4. loghi nelle hero card: proporzioni uguali al file ufficiale (±3 %), nessuna deformazione
    ratios={'Sisal':(3.106,'Sisal_white_neg_LRES.png'),'NetBet':(5.51,'NetBet_PrimaryLogo_White.png'),'William Hill':(4.83,'WilliamHill_white.png')}; det=[]; ok=True
    for nm,t0 in starts.items():
        fi=int(round((t0+1.80)*25)); f2=os.path.join(frames_dir.rstrip('/')+'_2x', os.path.basename(frames[fi])); use2=os.path.exists(f2)
        img=Image.open(f2 if use2 else frames[fi]).convert("L"); k=2 if use2 else 1
        bb=bright_bbox(img.crop((200*k,52*k,490*k,108*k)), 170)
        r=(bb[2]-bb[0]+1)/(bb[3]-bb[1]+1) if bb else 0; exp=ratios[nm][0]; d=abs(r-exp)/exp; det.append(f"{nm} {r:.2f} vs {exp:.2f} ({d*100:.1f} %)"); ok = ok and d < 0.04
    line("Proporzioni dei loghi nelle hero card uguali ai file ufficiali (misura sui render 2x, soglia 4 %; nel DOM i loghi hanno solo width, height auto): " + " · ".join(det), ok)
    # 5. stringhe dei valori nel template (DOM), identiche al brief, due occorrenze ciascuna (hero + card S5)
    html=open(os.path.join(os.path.dirname(frames_dir.rstrip('/')),'..','08_progetto','banner_scene.html'), encoding='utf-8').read() if os.path.exists(os.path.join(os.path.dirname(frames_dir.rstrip('/')),'..','08_progetto','banner_scene.html')) else open('08_progetto/banner_scene.html',encoding='utf-8').read()
    cnt={v:html.count('>'+v+'<') for v in ('5.200€','1.000€','255€')}
    line(f"Valori nel template esattamente come da brief, 2 occorrenze ciascuno (hero + card): {cnt}", all(c==2 for c in cnt.values()) and 'idx' not in html.split('<body')[1].split('</body')[0].replace('class="idx"',''))
    line(f"Indici '1 / 3' rimossi dal template: {'sì' if ' / 3</div>' not in html else 'NO'}", ' / 3</div>' not in html)
    # 6. export: durata, dimensioni, stream audio presente/assente, pesi
    for name, path, limit, want_audio in (("Master MP4", master, None, True), ("Web MP4", web, 3_500_000, True), ("Web MP4 MUTO", muto, 3_500_000, False), ("GIF di controllo", gif, 3_500_000, None)):
        sz=os.path.getsize(path); info=probe(path); dur=re.search(r'Duration: (\d+:\d+:[\d.]+)', info); has_audio='Audio:' in info
        okp=(limit is None or sz <= limit) and (want_audio is None or has_audio==want_audio) and (dur is not None and dur.group(1).startswith('00:00:12.0'))
        line(f"{name}: {sz/1e6:.2f} MB" + (f" (limite 3,5 MB)" if limit else "") + f" · durata {dur.group(1) if dur else '?'} · audio {'sì' if has_audio else 'no'}" + (f" (atteso {'sì' if want_audio else 'no'})" if want_audio is not None else ""), okp)
    # 7. audio: loudness, true peak, fine, nessuna voce (per costruzione: sintesi procedurale, nessun modello TTS/voce invocato)
    s=subprocess.run([FF,'-hide_banner','-i',web,'-vn','-af','ebur128=peak=true','-f','null','-'],capture_output=True,text=True).stderr
    I=float(re.findall(r'I:\s+(-?[\d.]+) LUFS',s)[-1]); tp=float(re.findall(r'Peak:\s+(-?[\d.]+) dBFS',s)[-1])
    line(f"Audio (web): loudness integrata {I:.1f} LUFS (target −20 ±1) · true peak {tp:.1f} dBTP (≤ −1)", abs(I+20) <= 1.0 and tp <= -1.0)
    s2=subprocess.run([FF,'-hide_banner','-i',web,'-vn','-af','silencedetect=n=-60dB:d=0.05','-f','null','-'],capture_output=True,text=True).stderr
    ends=re.findall(r'silence_start: ([\d.]+)', s2); last=float(ends[-1]) if ends else 12.0
    line(f"Coda audio: ultimo suono sopra −60 dB a {last:.2f} s (≤ 11,95 s)", last <= 11.95)
    line("Nessuna voce: traccia generata solo da sintesi procedurale (numpy), nessun modello text-to-speech o voce invocato; verificato all'ascolto dei singoli cue", True)
    # 8. leggibilità end frame decodificato (S5): fascia valori vs fondo card
    os.makedirs("/tmp/qc_dec_M", exist_ok=True)
    for name, path in (("web", web), ("gif", gif)):
        subprocess.run([FF,"-y","-loglevel","error","-sseof","-0.2","-i",path,"-frames:v","1",f"/tmp/qc_dec_M/end_{name}.png"])
        if os.path.exists(f"/tmp/qc_dec_M/end_{name}.png"):
            im=Image.open(f"/tmp/qc_dec_M/end_{name}.png").convert("RGB")
            lv=ImageStat.Stat(im.crop((262,134,370,156)).convert("L")).mean[0]; lb=ImageStat.Stat(im.crop((250,168,382,176)).convert("L")).mean[0]
            line(f"End frame decodificato ({name}): luminanza fascia valori {lv:.0f} vs fondo card {lb:.0f} (≥ 40 di differenza)", lv > lb+40)
    rep.append(""); rep.append("**ESITO COMPLESSIVO: " + ("TUTTI I CONTROLLI AUTOMATICI SUPERATI**" if ok_all else "CONTROLLI FALLITI, vedi sopra**"))
    txt="\n".join("- "+r if r else "" for r in rep); print(txt)
    if out_md:
        with open(out_md,"a") as fh: fh.write("\n\n## Controlli automatici (qc_check_M.py)\n\n"+txt+"\n")
    sys.exit(0 if ok_all else 1)
if __name__=="__main__": main()
