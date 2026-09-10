#!/usr/bin/env python3
"""Traccia audio del concept M — sintesi procedurale deterministica (nessuna voce, nessun campione di terzi).
Genera: bed 'stadio lontano', accensione riflettori, soffi d'ingresso, whoosh sulle 4 transizioni, tick di 'lock' sui valori,
soffio card S5, ping CTA S6. Output: WAV 48 kHz stereo 24 bit normalizzato a -20 LUFS (true-peak <= -1 dBTP).
Uso: python3 make_audio.py <out.wav> [--ambience <file>] [--dry]   (seme fisso: risultato identico a ogni esecuzione)
Revisione 2 (2026-09-10): il bed non è più rumore sintetico ma la traccia AMBIENTE STADIO estratta da una clip generata con Higgsfield
(video con audio nativo, job 4daed520…); gli effetti (whoosh, tick, ping) sono più corti e discreti. Nessuna voce, nessun modello TTS.
"""
import sys, os, subprocess, json, re
import numpy as np
import imageio_ffmpeg
SR = 48000; DUR = 12.0; N = int(SR*DUR)
rng = np.random.default_rng(20260910)
FF = imageio_ffmpeg.get_ffmpeg_exe()
t = np.arange(N)/SR
mix = np.zeros((N,2), dtype=np.float64)

def fft_bandnoise(n, lo, hi, slope=-0.5, seed=None):
    """rumore con spettro |f|^slope limitato a [lo,hi] Hz (via FFT), normalizzato RMS=1"""
    r = rng if seed is None else np.random.default_rng(seed)
    w = r.standard_normal(n); F = np.fft.rfft(w); f = np.fft.rfftfreq(n, 1/SR)
    shape = np.zeros_like(f); m = (f>=lo)&(f<=hi); shape[m] = (f[m]/lo)**slope
    # bordi morbidi
    edge = np.clip((f-lo*0.7)/(lo*0.3),0,1)*np.clip((hi*1.3-f)/(hi*0.3),0,1); shape *= edge
    x = np.fft.irfft(F*shape, n); return x/ (np.sqrt(np.mean(x**2))+1e-12)

def add(sig, t0, gain_db, pan=0.0):
    """aggiunge sig (mono) al mix a partire da t0 s; pan -1..1"""
    g = 10**(gain_db/20); i0 = int(round(t0*SR)); n = min(len(sig), N-i0)
    gl = np.cos((pan+1)*np.pi/4); gr = np.sin((pan+1)*np.pi/4)
    mix[i0:i0+n,0] += sig[:n]*g*gl; mix[i0:i0+n,1] += sig[:n]*g*gr

def env_bell(n, p=1.0):
    x = np.linspace(0,1,n); return np.sin(np.pi*x)**p

def whoosh(dur=0.36, f0=300, f1=2600, level=1.0):
    """rumore passa-banda con centro che sale f0→f1, inviluppo a campana, pan L→R applicato dal chiamante per blocchi"""
    n = int(dur*SR); x = fft_bandnoise(n, 150, 9000, -0.3)
    # filtro tempo-variante: STFT a blocchi con banda mobile (Q≈1.6)
    hop=256; win=1024; out=np.zeros(n+win); w=np.hanning(win)
    for i in range(0, n, hop):
        seg = np.zeros(win); s = x[i:i+win]; seg[:len(s)] = s; seg*=w
        F = np.fft.rfft(seg); f = np.fft.rfftfreq(win,1/SR)
        u = min(i/n,1.0); fc = f0*(f1/f0)**(u**0.8); bw = fc/1.6
        H = np.exp(-0.5*((f-fc)/(bw/2))**2); out[i:i+win] += np.fft.irfft(F*H, win)*w
    y = out[:n]; y = y/(np.max(np.abs(y))+1e-12) * env_bell(n, 1.4) * level
    return y

def tick(level=1.0):
    n = int(0.12*SR); tt = np.arange(n)/SR
    click = fft_bandnoise(n, 1500, 8000, 0)*np.exp(-tt/0.004)*0.8
    tone = np.sin(2*np.pi*1180*tt)*np.exp(-tt/0.028)*0.9 + np.sin(2*np.pi*2360*tt)*np.exp(-tt/0.012)*0.3
    y = click+tone; return y/(np.max(np.abs(y))+1e-12)*level

def ping():
    n = int(0.6*SR); tt = np.arange(n)/SR
    y = (np.sin(2*np.pi*880*tt)*np.exp(-tt/0.16) + 0.35*np.sin(2*np.pi*1760*tt)*np.exp(-tt/0.09) + 0.15*np.sin(2*np.pi*2640*tt)*np.exp(-tt/0.05))
    y *= np.minimum(1, tt/0.004); return y/(np.max(np.abs(y))+1e-12)

def soffio(dur=0.35, level=1.0):
    n=int(dur*SR); y = fft_bandnoise(n, 300, 5000, -0.6)*env_bell(n,2.0); return y/(np.max(np.abs(y))+1e-12)*level

# ---------- 1. bed: ambiente stadio reale (clip Higgsfield con audio nativo), decodificato via ffmpeg, 12 s, fade in/out, passa-alto 90 Hz
amb = sys.argv[sys.argv.index('--ambience')+1] if '--ambience' in sys.argv else os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ambience_stadio_higgsfield_veo_8s.m4a')
if os.path.exists(amb):
    raw = subprocess.run([FF,'-loglevel','error','-i',amb,'-t',str(DUR),'-f','f32le','-ac','2','-ar',str(SR),'-af','highpass=f=90,lowpass=f=9000','pipe:1'], capture_output=True, check=True).stdout
    a = np.frombuffer(raw, dtype=np.float32).reshape(-1,2).astype(np.float64)
    if len(a) < N:  # clip più corta di 12 s: loop con crossfade di 0,5 s
        xf=int(0.5*SR); parts=[a]; total=len(a)
        while total < N+xf:
            nxt=a.copy(); w=np.linspace(0,1,xf)[:,None]; parts[-1][-xf:]=parts[-1][-xf:]*(1-w)+nxt[:xf]*w; parts.append(nxt[xf:]); total+=len(nxt)-xf
        a=np.concatenate(parts)
    a=a[:N]; a=a/(np.sqrt(np.mean(a**2))+1e-12)
    fade_in=np.clip(t/0.9,0,1)**1.2; fade_out=np.clip((11.90-t)/0.7,0,1)
    bed_env=fade_in*fade_out
    mix += a*bed_env[:,None]*10**(-31/20)*1.0
    BED_SRC='ambiente Higgsfield: '+os.path.basename(amb)
else:
    bedL = fft_bandnoise(N, 180, 3200, -0.9, seed=1); bedR = fft_bandnoise(N, 180, 3200, -0.9, seed=2); common = fft_bandnoise(N, 180, 3200, -0.9, seed=3)
    slow = 0.78 + 0.12*np.sin(2*np.pi*0.23*t+0.4) + 0.07*np.sin(2*np.pi*0.61*t+2.1) + 0.05*np.sin(2*np.pi*1.7*t)
    fade_in = np.clip(t/0.7,0,1)**1.5; fade_out = np.clip((11.90-t)/0.6,0,1); bed_env = slow*fade_in*fade_out; bedg = 10**(-30/20)*3.0
    mix[:,0] += (0.6*bedL+0.7*common)*bed_env*bedg; mix[:,1] += (0.6*bedR+0.7*common)*bed_env*bedg; BED_SRC='sintetico (fallback)'
# ---------- 2. accensione riflettori 0,10–1,60: swell passa-basso
n=int(1.5*SR); sw = fft_bandnoise(n, 60, 900, -1.2, seed=4); e = (np.linspace(0,1,n)**2)*np.concatenate([np.ones(n-int(0.5*SR)), np.linspace(1,0,int(0.5*SR))])
add(sw*e/ (np.max(np.abs(sw*e))+1e-12), 0.10, -32)
# ---------- 3. ingressi titolo e CTA (S1)
add(soffio(0.35), 0.25, -26, -0.3); add(soffio(0.35), 0.45, -26, 0.0); add(soffio(0.30), 1.10, -25, 0.5)
# ---------- 4. whoosh transizioni (stesso campione, pan L→R per blocchi)
wh = whoosh()
def add_pan_sweep(sig, t0, gain_db):
    n=len(sig); blk=int(0.02*SR)
    for i in range(0,n,blk):
        u=min(i/n,1.0); pan=-0.8+1.6*u; add(sig[i:i+blk], t0+i/SR, gain_db, pan)
for t0 in (2.58, 4.80, 6.95, 9.10): add_pan_sweep(wh, t0, -19)
# ---------- 5. 'lock' valori: stesso suono, stesso livello per i tre operatori
for t0 in (4.10, 6.25, 8.40): add(tick(), t0, -22, 0.0)
# ---------- 6. card S5 (soffio unico) e CTA S6 (ping + soffio anello)
add(soffio(0.60, 1.0), 9.50, -24, 0.0)
add(ping(), 10.70, -19, 0.6); add(ping(), 11.30, -23, 0.6)

# ---------- normalizzazione loudness (-20 LUFS) e true-peak (<= -1 dBTP) via ffmpeg ebur128
def measure(x):
    raw = (x.astype(np.float32)).tobytes()
    p = subprocess.run([FF,'-hide_banner','-f','f32le','-ar',str(SR),'-ac','2','-i','pipe:0','-af','ebur128=peak=true','-f','null','-'], input=raw, capture_output=True)
    s = p.stderr.decode(errors='ignore'); I = float(re.findall(r'I:\s+(-?[\d.]+) LUFS', s)[-1]); tp = float(re.findall(r'Peak:\s+(-?[\d.]+) dBFS', s)[-1])
    return I, tp
I, tp = measure(mix); g = 10**((-20.0 - I)/20); mix *= g; I2, tp2 = measure(mix)
if tp2 > -1.0: mix *= 10**((-1.0 - tp2)/20); I2, tp2 = measure(mix)
last = np.max(np.nonzero(np.max(np.abs(mix),axis=1) > 1e-4))/SR
out = sys.argv[1]
if '--dry' not in sys.argv:
    subprocess.run([FF,'-y','-loglevel','error','-f','f32le','-ar',str(SR),'-ac','2','-i','pipe:0','-c:a','pcm_s24le',out], input=mix.astype(np.float32).tobytes(), check=True)
print(json.dumps({"bed":BED_SRC,"lufs_prima":round(I,2),"gain_db":round(20*np.log10(g),2),"lufs":round(I2,2),"true_peak_dbtp":round(tp2,2),"ultimo_evento_s":round(float(last),3),"out":out}))
