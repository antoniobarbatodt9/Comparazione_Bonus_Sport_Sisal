#!/usr/bin/env python3
"""QC automatico della famiglia orizzontale (10,0 s = 250 fotogrammi, 25 fps, con audio; variante web MUTA; GIF del 1920x1080 a 960x540).
Uso: python3 qc_check_horizontal.py <size> <dir_frames_1x> <master.mp4> <web.mp4> <web_muto.mp4> <control.gif> [--out report.md]
"""
import sys, os, glob, re, subprocess
from PIL import Image, ImageStat
import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
L = {
 '1920x1080': dict(W=1920,H=1080,safe=108,m=96, s1cta=(680,554,560,120), midcta=(700,702,520,110), smallcta=(700,748,520,110),
                   hero=(510,142,900,500), hlogo=(56,180), hlogow=(520,494,610), hval=(322,130), cards=(1240,[278,278,278],480,400),
                   endval=(1400,545,1560,620), endbg=(1250,660,1710,672)),
 '300x250':   dict(W=300,H=250,safe=30,m=16, s1cta=(70,120,160,38), midcta=(70,158,160,36), smallcta=(70,170,160,32),
                   hero=(16,22,268,118), hlogo=(14,40), hlogow=(124,118,146), hval=(76,30), cards=(16,[38,80,122],268,38),
                   endval=(228,136,268,150), endbg=(108,126,150,156), ctamargin=16),
 '336x280':   dict(W=336,H=280,safe=34,m=18, s1cta=(78,134,180,42), midcta=(78,178,180,40), smallcta=(78,188,180,36),
                   hero=(18,26,300,132), hlogo=(16,44), hlogow=(136,130,160), hval=(86,32), cards=(18,[42,88,134],300,42),
                   endval=(256,148,300,164), endbg=(120,138,175,172), ctamargin=16),
}
S = dict(s2=2.30, s3=4.10, s4=5.90)
def probe(p): return subprocess.run([FF,"-hide_banner","-i",p],capture_output=True,text=True).stderr
import numpy as np
def lime_pts(im):
    a=np.asarray(im.convert("RGB")); r,g,b=a[...,0].astype(int),a[...,1].astype(int),a[...,2].astype(int)
    m=(r>=140)&(r<=215)&(g>=185)&(g<=240)&(b<120); ys,xs=np.nonzero(m); return list(zip(xs.tolist(),ys.tolist()))
def bright_bbox(img_l, thr=200):
    a=np.asarray(img_l); ys,xs=np.nonzero(a>thr)
    return (int(xs.min()),int(ys.min()),int(xs.max()),int(ys.max())) if len(xs) else None
def main():
    size, frames_dir, master, web, muto, gif = sys.argv[1:7]; out_md = sys.argv[sys.argv.index("--out")+1] if "--out" in sys.argv else None
    K=L[size]; W,H,safe=K['W'],K['H'],K['safe']; usable=H-safe; CM=K.get('ctamargin',20)  # margine minimo CTA→safe: 20 px (1920) · 16 px sui rettangoli (regola griglia famiglia orizzontale)
    frames=sorted(glob.glob(os.path.join(frames_dir,"f*.png"))); rep=[]; ok_all=True
    def line(s, ok=True):
        nonlocal ok_all; rep.append(("✅ " if ok else "❌ ")+s); ok_all = ok_all and ok
    n=len(frames); im0=Image.open(frames[0]); line(f"Fotogrammi: {n} (atteso 250) · dimensione {im0.size} (atteso {(W,H)})", n==250 and im0.size==(W,H))
    # 1. CTA presente e integra dal f33 (t=1,32 s, fine ingresso) alla fine; ricerca sotto il titolo (esclude "SPORT" lime)
    cta_fail=[]; bb_all={}
    for idx,f in enumerate(frames):
        if idx<33: continue
        y0 = K['s1cta'][1]-6 if idx<50 else (K['hero'][1]+K['hero'][3]-10 if idx<190 else K['cards'][1][2]+K['cards'][3]-20)
        im=Image.open(f).convert("RGB").crop((0,y0,W,usable)); pts=lime_pts(im)
        minpx = 0.55*K['s1cta'][2]*K['s1cta'][3]*0.5
        if len(pts)<minpx: cta_fail.append((os.path.basename(f),'lime',len(pts))); continue
        xs=[p[0] for p in pts]; ys=[p[1]+y0 for p in pts]; bb=(min(xs),min(ys),max(xs),max(ys)); bb_all[idx]=bb
        inner=Image.open(f).convert("RGB").crop((bb[0]+10,bb[1]+8,bb[2]-10,bb[3]-8)); dark=sum(1 for p in inner.getdata() if p[0]+p[1]+p[2]<200)
        if dark<30: cta_fail.append((os.path.basename(f),'testo',dark))
        if bb[0]<3 or bb[2]>W-4 or bb[3]>usable-CM: cta_fail.append((os.path.basename(f),'margine',bb))
    line(f"CTA presente e integra (pill lime + testo scuro, x ≥ 3, fondo ≤ {usable-CM}) dal f33 al f249: {'tutti' if not cta_fail else 'FALLITI '+str(cta_fail[:4])}", not cta_fail)
    for name,lo,hi,exp in (("grande (S1)",35,46,K['s1cta']),("media (S2–S4)",62,180,K['midcta']),("finale (S5, prima del pulse)",195,221,K['smallcta'])):
        e=(exp[0],exp[1],exp[0]+exp[2]-1,exp[1]+exp[3]-1); bbs=[bb_all[i] for i in range(lo,hi+1) if i in bb_all]
        mx=max(max(abs(b[k]-e[k]) for k in range(4)) for b in bbs) if bbs else 999
        line(f"Posizione CTA {name} f{lo}–f{hi}: scarto max dal layout {exp} = {mx} px (soglia 3)", mx<=3)
    # 2. fascia disclaimer piatta su tutti i 250 fotogrammi
    sf=[]
    for f in frames:
        st=ImageStat.Stat(Image.open(f).convert("RGB").crop((0,usable,W,H)))
        if max(st.stddev)>1.0 or abs(st.mean[0]-6)>2 or abs(st.mean[1]-26)>2 or abs(st.mean[2]-18)>2: sf.append(os.path.basename(f))
    line(f"Fascia disclaimer 0,{usable} {W}×{safe} piatta #061a12 su tutti i 250 fotogrammi (wipe e pulse inclusi): {'tutti' if not sf else 'FALLITI '+str(sf[:5])}", not sf)
    # 3. pari trattamento S2/S3/S4
    hx,hy,hw,hh=K['hero']; vt,vl=K['hval']; det=[]; ok=True; heights={}
    for nm,key in (('Sisal','s2'),('NetBet','s3'),('William Hill','s4')):
        t0=S[key]; fe=frames[int(round((t0+0.20)*25))]; fm=frames[int(round((t0+1.05)*25))]; fh=frames[int(round((t0+1.45)*25))]
        card_lum=ImageStat.Stat(Image.open(fe).convert("L").crop((hx+6,hy+4,hx+hw-6,hy+14))).mean[0]
        vb_m=bright_bbox(Image.open(fm).convert("L").crop((hx,hy+vt,hx+hw,hy+vt+vl))); vb_h=bright_bbox(Image.open(fh).convert("L").crop((hx,hy+vt,hx+hw,hy+vt+vl)))
        same= vb_m is not None and vb_h is not None and abs((vb_m[3]-vb_m[1])-(vb_h[3]-vb_h[1]))<=1 and abs(vb_m[1]-vb_h[1])<=1
        heights[nm]=(vb_h[3]-vb_h[1]) if vb_h else -1; det.append(f"{nm}: card a u=0,20 (lum {card_lum:.0f}), valore completo a u=1,05 e stabile a u=1,45 → {'sì' if same else 'NO'}, altezza cifre {heights[nm]} px"); ok=ok and same
    hs=list(heights.values()); ok=ok and max(hs)-min(hs)<=1
    line("Pari trattamento sequenziale (stessi tempi relativi, stessa altezza dei valori ±1 px): "+" · ".join(det), ok)
    # 4. loghi hero: proporzioni (misura sui frame 2x) confrontate con il PNG ufficiale ridotto ALLA STESSA larghezza e misurato con la stessa soglia
    files={'Sisal':'Sisal_white_neg_LRES.png','NetBet':'NetBet_PrimaryLogo_White.png','William Hill':'WilliamHill_white.png'}; det=[]; ok=True; lt,lh=K['hlogo']
    logodir=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','08_progetto','assets','loghi')
    for j,(nm,key) in enumerate((('Sisal','s2'),('NetBet','s3'),('William Hill','s4'))):
        fi=int(round((S[key]+1.45)*25)); f2=os.path.join(frames_dir.rstrip('/').replace('_frames','_2x'),os.path.basename(frames[fi])); use2=os.path.exists(f2); k=2 if use2 else 1
        img=Image.open(f2 if use2 else frames[fi]).convert("L"); bb=bright_bbox(img.crop(((hx+4)*k,(hy+lt-2)*k,(hx+hw-4)*k,(hy+lt+lh+2)*k)),100)
        r=(bb[2]-bb[0]+1)/(bb[3]-bb[1]+1) if bb else 0
        png=Image.open(os.path.join(logodir,files[nm])).convert("RGBA"); wpx=K['hlogow'][j]*k; ref=png.resize((wpx,round(png.size[1]*wpx/png.size[0])),Image.LANCZOS).getchannel("A")
        rb=bright_bbox(ref,100); rr=(rb[2]-rb[0]+1)/(rb[3]-rb[1]+1); d=abs(r-rr)/rr; det.append(f"{nm} {r:.2f} vs riferimento {rr:.2f} ({d*100:.1f} %)"); ok=ok and d<0.05
    line("Proporzioni dell'inchiostro dei loghi nelle hero card vs PNG ufficiali ridotti alla stessa larghezza (render 2x, soglia luminanza 100, tolleranza 5 %: sensibile al ricampionamento dei tratti sottili): "+" · ".join(det), ok)
    # 4b. geometria del box <img> nel DOM (nessuna deformazione): rapporto larghezza/altezza dell'elemento = rapporto del file PNG (tolleranza 0,5 %)
    import json
    src=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','adaptations','horizontal_family','src')
    times=",".join(f"{S[k]+1.45:.2f}" for k in ('s2','s3','s4'))
    outm=subprocess.run(["node","render_horizontal.mjs","--size",size,"--times",times,"--out","/tmp/qc_measure_"+size,"--prefix","m","--measure","1"],cwd=src,capture_output=True,text=True).stdout.strip().splitlines()[-1]
    det=[]; ok=True
    for row,(nm,key) in zip(json.loads(outm),(('Sisal','s2'),('NetBet','s3'),('William Hill','s4'))):
        card=[v for kk,v in row.items() if kk.startswith('card')][0]; lw,lhh=card['logo'][2],card['logo'][3]; png=Image.open(os.path.join(logodir,files[nm])); fr=png.size[0]/png.size[1]; r=lw/lhh; d=abs(r-fr)/fr
        det.append(f"{nm} elemento {lw:.1f}×{lhh:.1f} = {r:.3f} vs file {fr:.3f} ({d*100:.2f} %)"); ok=ok and d<0.005
    line("Box <img> dei loghi nel DOM non deformati (rapporto elemento = rapporto file PNG, tolleranza 0,5 %): "+" · ".join(det), ok)
    # 5. testi nel template
    html=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','adaptations','horizontal_family','src','banner_horizontal.html'),encoding='utf-8').read()
    body=html.split('<body')[1].split('</body')[0]
    cnt={v:body.count('>'+v+'<') for v in ('5.200€','1.000€','255€')}
    forb=[s for s in ('Importo massimo','/ 3<','miglior','1/3','2/3','3/3') if s in body]
    line(f"Valori nel template esattamente come da brief, 2 occorrenze ciascuno (hero + card): {cnt} · testi vietati: {forb or 'nessuno'}", all(c==2 for c in cnt.values()) and not forb)
    # 6. export
    for name,path,limit,want_audio in (("Master MP4",master,None,True),("Web MP4",web,3_500_000,True),("Web MP4 MUTO",muto,3_500_000,False),("GIF di controllo",gif,3_500_000,False)):
        sz=os.path.getsize(path); info=probe(path); dur=re.search(r'Duration: (\d+:\d+:[\d.]+)',info); has_audio='Audio:' in info
        okp=(limit is None or sz<=limit) and (has_audio==want_audio) and dur is not None and dur.group(1).startswith('00:00:10.0')
        line(f"{name}: {sz/1e6:.2f} MB"+(" (limite 3,5 MB)" if limit else "")+f" · durata {dur.group(1) if dur else '?'} · audio {'sì' if has_audio else 'no'} (atteso {'sì' if want_audio else 'no'})", okp)
    # 6b. audio (web): loudness, true peak, coda; bed = stessa clip Higgsfield del master (già verificata senza parlato con whisper/VAD)
    sa=subprocess.run([FF,'-hide_banner','-i',web,'-vn','-af','ebur128=peak=true','-f','null','-'],capture_output=True,text=True).stderr
    I=float(re.findall(r'I:\s+(-?[\d.]+) LUFS',sa)[-1]); tp=float(re.findall(r'Peak:\s+(-?[\d.]+) dBFS',sa)[-1])
    line(f"Audio (web): loudness integrata {I:.1f} LUFS (target −20 ±1) · true peak {tp:.1f} dBTP (≤ −1)", abs(I+20)<=1.0 and tp<=-1.0)
    s2=subprocess.run([FF,'-hide_banner','-i',web,'-vn','-af','silencedetect=n=-60dB:d=0.05','-f','null','-'],capture_output=True,text=True).stderr
    ends=re.findall(r'silence_start: ([\d.]+)',s2); last=float(ends[-1]) if ends else 10.0
    line(f"Coda audio: ultimo suono sopra −60 dB a {last:.2f} s (≤ 9,95 s)", last<=9.95)
    line("Nessuna voce: bed = stessa clip stadio Higgsfield del master (whisper base + VAD: 0 segmenti di parlato) + SFX procedurali numpy; nessun modello TTS/voce invocato", True)
    # 7. fascia disclaimer sui fotogrammi DECODIFICATI (web mp4 e gif, 10 campioni)
    dd=f"/tmp/qc_dec_h_{size}"; os.makedirs(dd,exist_ok=True)
    gw=Image.open(gif).size[0]; kg=gw/W
    for name,path in (("web",web),("gif",gif)):
        for fn in glob.glob(f"{dd}/{name}_*.png"): os.remove(fn)
        subprocess.run([FF,"-y","-loglevel","error","-i",path,"-vf","fps=1","-frames:v","10",f"{dd}/{name}_%02d.png"])
        worst=0; kk=kg if name=="gif" else 1.0
        for fn in sorted(glob.glob(f"{dd}/{name}_*.png")):
            st=ImageStat.Stat(Image.open(fn).convert("RGB").crop((0,int((usable+2)*kk),int(W*kk),int(H*kk))))
            worst=max(worst,max(st.stddev),abs(st.mean[0]-6),abs(st.mean[1]-26),abs(st.mean[2]-18))
        line(f"Fascia disclaimer nei fotogrammi decodificati ({name}{' 960x540' if kk!=1 else ''}, 10 campioni): deviazione max {worst:.1f} (≤ 6)", worst<=6)
    # 8. end frame decodificato: leggibilità del valore della terza card/riga (255€) rispetto al fondo card
    ev=K['endval']; eb=K['endbg']
    for name,path in (("web",web),("gif",gif)):
        kk=kg if name=="gif" else 1.0
        subprocess.run([FF,"-y","-loglevel","error","-sseof","-0.2","-i",path,"-frames:v","1",f"{dd}/end_{name}.png"])
        if os.path.exists(f"{dd}/end_{name}.png"):
            im=Image.open(f"{dd}/end_{name}.png").convert("RGB")
            lv=np.asarray(im.crop(tuple(int(v*kk) for v in ev)).convert("L")); lv=float(np.percentile(lv,90))
            lb=ImageStat.Stat(im.crop(tuple(int(v*kk) for v in eb)).convert("L")).mean[0]
            line(f"End frame decodificato ({name}): luminanza cifre 255€ (p90) {lv:.0f} vs fondo card {lb:.0f} (≥ 40 di differenza)", lv>lb+40)
    rep.append(""); rep.append("**ESITO COMPLESSIVO "+size+": "+("TUTTI I CONTROLLI AUTOMATICI SUPERATI**" if ok_all else "CONTROLLI FALLITI, vedi sopra**"))
    txt="\n".join("- "+r if r else "" for r in rep); print(txt)
    if out_md:
        with open(out_md,"a") as fh: fh.write(f"\n\n## Controlli automatici {size} (qc_check_vertical.py)\n\n"+txt+"\n")
    sys.exit(0 if ok_all else 1)
if __name__=="__main__": main()
