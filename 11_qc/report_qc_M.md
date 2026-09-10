# Report QC — Concept M "Montaggio a scene" · 970×250 · 25 fps · 12,0 s (300 fotogrammi) · con audio SFX

Data: 2026-09-10 · Sorgente: `08_progetto/banner_scene.html` (ambiente `assets/env/env_M_pitch_topdown_FINAL_2036x596.jpg`, md5 `ea1d842587991411dbbb9bc7673308fa`) · Pipeline: `08_progetto/make_master_M.sh` (render 2× → Lanczos → x264 / GIF) · Audio: `08_progetto/audio/make_audio.py` (seme 20260910).

## Esportazioni (10_export/)

| File | Peso | Specifiche |
|---|---|---|
| `BonusSport_970x250_25fps_12s_M_MASTER.mp4` | 1,58 MB | H.264 CRF 12 yuv420p, 25 fps, 12,00 s, AAC 192 kbps 48 kHz stereo |
| `…_MASTER_444_archivio.mov` | 5,25 MB | H.264 CRF 10 yuv444p + PCM 24 bit (archivio) |
| `…_WEB.mp4` | 0,73 MB (≤ 3,5 MB) | H.264 High 4.0 CRF 17 yuv420p, faststart, AAC 128 kbps |
| `…_WEB_MUTO.mp4` | 0,53 MB (≤ 3,5 MB) | come WEB, senza stream audio (circuiti che non ammettono audio / autoplay muto) |
| `…_CONTROL.gif` | 3,11 MB (≤ 3,5 MB) | **12,5 fps** (a 25 fps pesava 5,19 MB: 300 fotogrammi con 5 cambi di scena), 256 colori, dithering sierra2_4a, ambiente fermo, muta, loop |
| `…_ENDFRAME_fallback_statico.png` | 0,27 MB | ultimo fotogramma (f299) |
| `audio/…_audio_48k24.wav` · `audio/…_audio_misura.json` | 3,46 MB | traccia separata 48 kHz 24 bit; misure loudness/true-peak |

## Correzioni emerse dal QC (prima della consegna)
1. **Enfasi CTA in S6**: nella prima passata l'anello in espansione e l'alone superavano x=950 (margine di 20 px dal bordo destro). Corretto: scala, anello e alone dell'enfasi sono ora ancorati al bordo destro della pill (x=950 fisso) e crescono verso sinistra/verticale; alone ridotto a 300 px e spostato a sinistra. Ri-renderizzati f266–f299 (entrambe le passate) e ri-codificate tutte le esportazioni.
2. Il rilevatore della CTA del QC usava una finestra troppo ampia e includeva la parola "SPORT" (lime) del titolo: corretto con finestre di ricerca per fase. Nessun impatto sul banner.

## Controlli visivi (fotogrammi decodificati dal WEB.mp4 e dalla GIF: `decodificati_M/contact_decodificati.png`)
- S1: "BONUS SPORT" + CTA grande centrati, senza due punti; ingresso BONUS → SPORT → CTA; campo visto dall'alto leggibile ma non invasivo. ✅
- T1–T4: wipe di luce confinati sopra la safe area; la CTA resta continua durante il morph. ✅
- S2–S4: hero card + CTA media come gruppo centrato; loghi ufficiali nitidi, non deformati, senza patch; nessun indice "n/3"; valori 5.200€ · 1.000€ · 255€ esatti; stessa coreografia. ✅
- S5/S6: tre card identiche, valori allineati, CTA in risalto entro il margine destro; nessun accento sulla card Sisal (scelta cliente). ✅
- Safe area 0,210 970×40: vuota e piatta in tutti i fotogrammi. ✅
- Ambiente: nessun elemento IP (nessun pallone, bandierina, persona, spalti, cartelloni, scritte); linee del campo sottili sotto i testi. ✅
- Audio (ascolto dei cue e misure): bed stadio tenue, whoosh sulle 4 transizioni, tick identico sui tre valori, ping sulla CTA finale; nessuna voce. ✅

## Checklist del brief
- Formato 970×250, 25 fps, durata 12,0 s (entro il limite di 13 s indicato; 12 s confermati dal cliente). ✅
- Titolo "BONUS SPORT", tre loghi ufficiali, tre valori "FINO A …" invariati, CTA "SCOPRI DI PIÙ" presente in ogni scena (da 1,10 s, dopo l'ingresso BONUS → SPORT richiesto, fino alla fine). ✅
- Pari dignità: stessa card, stesso logo-box, stesso corpo dei valori, stessa coreografia e durata per i tre operatori; nessuna claim di superiorità. ✅
- Nessun disclaimer aggiunto; safe area libera. ✅ · Nessun elemento IP. ✅ · Loghi non ricostruiti/deformati. ✅
- Higgsfield usato solo per l'ambiente; mai per testi, loghi, importi, €, CTA, disclaimer, voci. ✅
- Audio: SFX + ambiente, **mai voiceover** (richiesta cliente); versioni mute disponibili. ✅


## Controlli automatici (qc_check_M.py)

- ✅ Fotogrammi: 300 (atteso 300) · dimensione (970, 250) (atteso (970, 250))
- ✅ CTA presente e integra (pill lime ≥ 3000 px + testo scuro, dentro i margini) dal f40 al f299: tutti
- ✅ Posizione CTA grande (S1), fuori dal riflesso f56–f62: scarto max dal layout atteso (599, 79, 829, 131) = 1 px (soglia 3)
- ✅ Posizione CTA media (S2–S4) f77–f226: scarto max dal layout atteso (565, 80, 775, 134) = 1 px (soglia 3)
- ✅ Posizione CTA piccola (S5) f239–f267: scarto max dal layout atteso (800, 83, 950, 127) = 1 px (soglia 3)
- ✅ Safe area 0,210 970×40 piatta in tutti i 300 fotogrammi (wipe inclusi): tutti
- ✅ Pari trattamento sequenziale (stessi tempi relativi, stessa altezza dei valori ±1 px): Sisal: card a u=0,25 (lum 51), valore completo a u=1,20 e stabile a u=1,80 → sì, altezza cifre 26 px · NetBet: card a u=0,25 (lum 50), valore completo a u=1,20 e stabile a u=1,80 → sì, altezza cifre 26 px · William Hill: card a u=0,25 (lum 51), valore completo a u=1,20 e stabile a u=1,80 → sì, altezza cifre 26 px
- ✅ Proporzioni dei loghi nelle hero card uguali ai file ufficiali (misura sui render 2x, soglia 4 %; nel DOM i loghi hanno solo width, height auto): Sisal 3.16 vs 3.11 (1.9 %) · NetBet 5.62 vs 5.51 (2.0 %) · William Hill 4.79 vs 4.83 (0.7 %)
- ✅ Valori nel template esattamente come da brief, 2 occorrenze ciascuno (hero + card): {'5.200€': 2, '1.000€': 2, '255€': 2}
- ✅ Indici '1 / 3' rimossi dal template: sì
- ✅ Master MP4: 1.58 MB · durata 00:00:12.00 · audio sì (atteso sì)
- ✅ Web MP4: 0.73 MB (limite 3,5 MB) · durata 00:00:12.00 · audio sì (atteso sì)
- ✅ Web MP4 MUTO: 0.53 MB (limite 3,5 MB) · durata 00:00:12.00 · audio no (atteso no)
- ✅ GIF di controllo: 3.11 MB (limite 3,5 MB) · durata 00:00:12.00 · audio no
- ✅ Audio (web): loudness integrata -20.1 LUFS (target −20 ±1) · true peak -8.4 dBTP (≤ −1)
- ✅ Coda audio: ultimo suono sopra −60 dB a 11.89 s (≤ 11,95 s)
- ✅ Nessuna voce: traccia generata solo da sintesi procedurale (numpy), nessun modello text-to-speech o voce invocato; verificato all'ascolto dei singoli cue
- ✅ End frame decodificato (web): luminanza fascia valori 149 vs fondo card 37 (≥ 40 di differenza)
- ✅ End frame decodificato (gif): luminanza fascia valori 150 vs fondo card 37 (≥ 40 di differenza)

- **ESITO COMPLESSIVO: TUTTI I CONTROLLI AUTOMATICI SUPERATI**
