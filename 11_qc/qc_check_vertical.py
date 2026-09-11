#!/usr/bin/env python3
"""QC automatico della famiglia verticale (10,0 s = 250 fotogrammi, 25 fps, senza audio).
Uso: python3 qc_check_vertical.py <size> <dir_frames_1x> <master.mp4> <web.mp4> <control.gif> [--out report.md]
"""
import sys, os, glob, re, subprocess
from PIL import Image, ImageStat
import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
L = {
 '300x600': dict(W=300,H=600,safe=60,m=24, s1cta=(40,316,220,52), midcta=(50,350,200,48), smallcta=(50,444,200,48),
                 hero=(24,140,252,176), hlogo=(20,64), hlogow=(150,142,175), hval=(114,40), cards=(24,[84,200,316],252,104), cval=(66,30)),
 '320x480': dict(W=320,H=480,safe=50,m=20, s1cta=(60,254,200,46), midcta=(70,284,180,44), smallcta=(70,360,180,44),
                 hero=(20,96,280,160), hlogo=(16,56), hlogow=(150,142,175), hval=(100,38), cards=(20,[70,164,258],280,84), cval=(56,26)),
 '160x600': dict(W=160,H=600,safe=56,m=12, s1cta=(12,300,136,40), midcta=(12,330,136,40), smallcta=(12,456,136,40),
                 hero=(12,150,136,150), hlogo=(16,48), hlogow=(104,99,122), hval=(90,32), cards=(12,[92,208,324],136,108), cval=(66,26)),
}
S = dict(s2=2.30, s3=4.10, s4=5.90)
def probe(p): return subprocess.run([FF,"-hide_banner","-i",p],capture_output=True,text=True).stderr
def lime_pts(im):
    px=im.load(); w,h=im.size; pts=[]
    for y in range(h):
        for x in range(w):
            r,g,b=px[x,y]
            if 140<=r<=215 and 185<=g<=240 and b<120: pts.append((x,y))
    return pts
def bright_bbox(img_l, thr=200):
    px=img_l.load(); w,h=img_l.size; xs=[]; ys=[]
    for y in range(h):
        for x in range(w):
            if px[x,y]>thr: xs.append(x); ys.append(y)
    return (min(xs),min(ys),max(xs),max(ys)) if xs else None
def main():
    size, frames_dir, master, web, gif = sys.argv[1:6]; out_md = sys.argv[sys.argv.index("--out")+1] if "--out" in sys.argv else None
    K=L[size]; W,H,safe=K['W'],K['H'],K['safe']; usable=H-safe
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
        if bb[0]<3 or bb[2]>W-4 or bb[3]>usable-20: cta_fail.append((os.path.basename(f),'margine',bb))
    line(f"CTA presente e integra (pill lime + testo scuro, x ≥ 3, fondo ≤ {usable-20}) dal f33 al f249: {'tutti' if not cta_fail else 'FALLITI '+str(cta_fail[:4])}", not cta_fail)
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
    src=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','adaptations','vertical_family','src')
    times=",".join(f"{S[k]+1.45:.2f}" for k in ('s2','s3','s4'))
    outm=subprocess.run(["node","render_vertical.mjs","--size",size,"--times",times,"--out","/tmp/qc_measure_"+size,"--prefix","m","--measure","1"],cwd=src,capture_output=True,text=True).stdout.strip().splitlines()[-1]
    det=[]; ok=True
    for row,(nm,key) in zip(json.loads(outm),(('Sisal','s2'),('NetBet','s3'),('William Hill','s4'))):
        card=[v for kk,v in row.items() if kk.startswith('card')][0]; lw,lhh=card['logo'][2],card['logo'][3]; png=Image.open(os.path.join(logodir,files[nm])); fr=png.size[0]/png.size[1]; r=lw/lhh; d=abs(r-fr)/fr
        det.append(f"{nm} elemento {lw:.1f}×{lhh:.1f} = {r:.3f} vs file {fr:.3f} ({d*100:.2f} %)"); ok=ok and d<0.005
    line("Box <img> dei loghi nel DOM non deformati (rapporto elemento = rapporto file PNG, tolleranza 0,5 %): "+" · ".join(det), ok)
    # 5. testi nel template
    html=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','adaptations','vertical_family','src','banner_vertical.html'),encoding='utf-8').read()
    body=html.split('<body')[1].split('</body')[0]
    cnt={v:body.count('>'+v+'<') for v in ('5.200€','1.000€','255€')}
    forb=[s for s in ('Importo massimo','/ 3<','miglior','1/3','2/3','3/3') if s in body]
    line(f"Valori nel template esattamente come da brief, 2 occorrenze ciascuno (hero + card): {cnt} · testi vietati: {forb or 'nessuno'}", all(c==2 for c in cnt.values()) and not forb)
    # 6. export
    for name,path,limit in (("Master MP4",master,None),("Web MP4",web,3_500_000),("GIF di controllo",gif,3_500_000)):
        sz=os.path.getsize(path); info=probe(path); dur=re.search(r'Duration: (\d+:\d+:[\d.]+)',info); has_audio='Audio:' in info
        okp=(limit is None or sz<=limit) and (not has_audio) and dur is not None and dur.group(1).startswith('00:00:10.0')
        line(f"{name}: {sz/1e6:.2f} MB"+(" (limite 3,5 MB)" if limit else "")+f" · durata {dur.group(1) if dur else '?'} · audio {'sì' if has_audio else 'no'} (atteso no)", okp)
    # 7. fascia disclaimer sui fotogrammi DECODIFICATI (web mp4 e gif, 10 campioni)
    dd=f"/tmp/qc_dec_v_{size}"; os.makedirs(dd,exist_ok=True)
    for name,path in (("web",web),("gif",gif)):
        for fn in glob.glob(f"{dd}/{name}_*.png"): os.remove(fn)
        subprocess.run([FF,"-y","-loglevel","error","-i",path,"-vf","fps=1","-frames:v","10",f"{dd}/{name}_%02d.png"])
        worst=0
        for fn in sorted(glob.glob(f"{dd}/{name}_*.png")):
            st=ImageStat.Stat(Image.open(fn).convert("RGB").crop((0,usable+2,W,H)))
            worst=max(worst,max(st.stddev),abs(st.mean[0]-6),abs(st.mean[1]-26),abs(st.mean[2]-18))
        line(f"Fascia disclaimer nei fotogrammi decodificati ({name}, 10 campioni): deviazione max {worst:.1f} (≤ 6)", worst<=6)
    # 8. end frame decodificato: leggibilità valore terza card
    cx,cys,cw,ch=K['cards']; vt,vl=K['cval']
    for name,path in (("web",web),("gif",gif)):
        subprocess.run([FF,"-y","-loglevel","error","-sseof","-0.2","-i",path,"-frames:v","1",f"{dd}/end_{name}.png"])
        if os.path.exists(f"{dd}/end_{name}.png"):
            im=Image.open(f"{dd}/end_{name}.png").convert("RGB")
            lv=ImageStat.Stat(im.crop((cx+cw//2-30,cys[2]+vt+4,cx+cw//2+30,cys[2]+vt+vl-4)).convert("L")).mean[0]
            lb=ImageStat.Stat(im.crop((cx+8,cys[2]+ch-9,cx+cw-8,cys[2]+ch-3)).convert("L")).mean[0]
            line(f"End frame decodificato ({name}): luminanza fascia valore 255€ {lv:.0f} vs fondo card {lb:.0f} (≥ 40 di differenza)", lv>lb+40)
    rep.append(""); rep.append("**ESITO COMPLESSIVO "+size+": "+("TUTTI I CONTROLLI AUTOMATICI SUPERATI**" if ok_all else "CONTROLLI FALLITI, vedi sopra**"))
    txt="\n".join("- "+r if r else "" for r in rep); print(txt)
    if out_md:
        with open(out_md,"a") as fh: fh.write(f"\n\n## Controlli automatici {size} (qc_check_vertical.py)\n\n"+txt+"\n")
    sys.exit(0 if ok_all else 1)
if __name__=="__main__": main()
