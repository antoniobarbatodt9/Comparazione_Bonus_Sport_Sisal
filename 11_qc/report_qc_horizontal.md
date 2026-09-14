# Report QC — famiglia orizzontale 1920×1080 · 300×250 · 336×280 (produzione 2026-09-14)

Master di riferimento: concept M rev 2 (970×250). Storyboard approvati dal cliente il 2026-09-14 ("approvo, passa alla creazione"). Durata 10,0 s · 25 fps · 250 fotogrammi · **con audio** (traccia del master ri-temporizzata a 10 s, profilo `horizontal` di `08_progetto/audio/make_audio.py`: come il profilo `vertical` ma con panoramica L→R sui whoosh perché il wipe è orizzontale come nel master; −20 LUFS, TP ≤ −1 dBTP); `10_export/horizontal/audio/` contiene WAV 48 kHz 24 bit e misura. Sfondo: ri-inquadratura 16:9 dello stesso still Higgsfield approvato (0 crediti). Pipeline: `adaptations/horizontal_family/src/make_horizontal.sh` (render 2× deterministico → Lanczos → x264 → GIF), QC: `11_qc/qc_check_horizontal.py`.

Il 1920×1080 è prodotto a 10 s come lo storyboard approvato (l'opzione 12 s con la timeline del master resta disponibile su richiesta).

## File consegnati (`10_export/horizontal/`)

| Size | MASTER.mp4 (CRF 12, AAC 192k) | MASTER_444_archivio.mov (PCM 24 bit) | WEB.mp4 (AAC 128k, ≤ 3,5 MB) | WEB_MUTO.mp4 | CONTROL.gif (≤ 3,5 MB) | ENDFRAME PNG |
|---|---|---|---|---|---|---|
| 1920x1080 | 9.32 MB | 16.86 MB | **2.61 MB** (CRF 19) · WEB_HQ.mp4 CRF 17: 3.55 MB (fuori soglia) | 2.45 MB | **3.35 MB** (720×405, 10 fps) | 1894 KB |
| 300x250 | 0.58 MB | 3.33 MB | **0.33 MB** (CRF 17) | 0.17 MB | **1.91 MB** (25 fps) | 77 KB |
| 336x280 | 0.67 MB | 3.45 MB | **0.37 MB** (CRF 17) | 0.20 MB | **2.30 MB** (25 fps) | 92 KB |

## Note sulla compressione
- **1920×1080 WEB.mp4**: a CRF 17 il file pesa 3,55 MB (appena oltre la soglia); la consegna entro soglia è a **CRF 19 (2,61 MB)**, con il CRF 17 conservato come `WEB_HQ.mp4` dichiarato fuori soglia. PSNR rispetto ai fotogrammi sorgente (t 1,50 / 3,30 / 9,96 s): CRF 19 = 40,1 / 41,5 / 35,9 dB, CRF 17 = 40,3 / 41,9 / 36,1 dB (differenza ≤ 0,3 dB): a 100 % i due file non sono distinguibili su testi e loghi (vedi contact sheet dei decodificati).
- **1920×1080 CONTROL.gif**: una GIF di 10 s a 1920×1080 non può stare in 3,5 MB; a 960×540 pesa 5,96 MB a 10 fps e 5,22 MB a 8 fps. La GIF di controllo è quindi a **720×405 (16:9 esatto), 10 fps, 256 colori: 3,35 MB**, resa dalla sequenza "fermo" a 1× (sfondo senza deriva, come le altre GIF). Non è un formato di distribuzione: per il 16:9 valgono i MP4.
- Rettangoli: WEB.mp4 a CRF 17 (0,33 / 0,37 MB), GIF a 25 fps piena (1,91 / 2,30 MB).
- GIF del 1920 dai frame 1× (nessun 2× → 1× perché il target è 720×405, Lanczos diretto); tutti gli MP4 dai frame 2× ricampionati Lanczos.
- Fascia disclaimer piatta su tutti i fotogrammi sorgente e nei decodificati (deviazione ≤ 3/255 in MP4, ≤ 2 in GIF).
- Contact sheet dei fotogrammi decodificati: `11_qc/decodificati_horizontal/contact_decodificati_horizontal.png`.


## Controlli automatici 300x250 (qc_check_vertical.py)

- ✅ Fotogrammi: 250 (atteso 250) · dimensione (300, 250) (atteso (300, 250))
- ✅ CTA presente e integra (pill lime + testo scuro, x ≥ 3, fondo ≤ 204) dal f33 al f249: tutti
- ✅ Posizione CTA grande (S1) f35–f46: scarto max dal layout (70, 120, 160, 38) = 0 px (soglia 3)
- ✅ Posizione CTA media (S2–S4) f62–f180: scarto max dal layout (70, 158, 160, 36) = 0 px (soglia 3)
- ✅ Posizione CTA finale (S5, prima del pulse) f195–f221: scarto max dal layout (70, 170, 160, 32) = 1 px (soglia 3)
- ✅ Fascia disclaimer 0,220 300×30 piatta #061a12 su tutti i 250 fotogrammi (wipe e pulse inclusi): tutti
- ✅ Pari trattamento sequenziale (stessi tempi relativi, stessa altezza dei valori ±1 px): Sisal: card a u=0,20 (lum 33), valore completo a u=1,05 e stabile a u=1,45 → sì, altezza cifre 17 px · NetBet: card a u=0,20 (lum 34), valore completo a u=1,05 e stabile a u=1,45 → sì, altezza cifre 17 px · William Hill: card a u=0,20 (lum 33), valore completo a u=1,05 e stabile a u=1,45 → sì, altezza cifre 17 px
- ✅ Proporzioni dell'inchiostro dei loghi nelle hero card vs PNG ufficiali ridotti alla stessa larghezza (render 2x, soglia luminanza 100, tolleranza 5 %: sensibile al ricampionamento dei tratti sottili): Sisal 3.03 vs riferimento 3.10 (2.4 %) · NetBet 5.51 vs riferimento 5.66 (2.6 %) · William Hill 4.84 vs riferimento 4.93 (1.8 %)
- ✅ Box <img> dei loghi nel DOM non deformati (rapporto elemento = rapporto file PNG, tolleranza 0,5 %): Sisal elemento 124.0×39.5 = 3.139 vs file 3.136 (0.11 %) · NetBet elemento 118.0×30.7 = 3.844 vs file 3.839 (0.11 %) · William Hill elemento 146.0×48.7 = 2.998 vs file 3.000 (0.07 %)
- ✅ Valori nel template esattamente come da brief, 2 occorrenze ciascuno (hero + card): {'5.200€': 2, '1.000€': 2, '255€': 2} · testi vietati: nessuno
- ✅ Master MP4: 0.58 MB · durata 00:00:10.00 · audio sì (atteso sì)
- ✅ Web MP4: 0.33 MB (limite 3,5 MB) · durata 00:00:10.00 · audio sì (atteso sì)
- ✅ Web MP4 MUTO: 0.17 MB (limite 3,5 MB) · durata 00:00:10.00 · audio no (atteso no)
- ✅ GIF di controllo: 1.91 MB (limite 3,5 MB) · durata 00:00:10.00 · audio no (atteso no)
- ✅ Audio (web): loudness integrata -20.1 LUFS (target −20 ±1) · true peak -5.8 dBTP (≤ −1)
- ✅ Coda audio: ultimo suono sopra −60 dB a 9.93 s (≤ 9,95 s)
- ✅ Nessuna voce: bed = stessa clip stadio Higgsfield del master (whisper base + VAD: 0 segmenti di parlato) + SFX procedurali numpy; nessun modello TTS/voce invocato
- ✅ Fascia disclaimer nei fotogrammi decodificati (web, 10 campioni): deviazione max 3.0 (≤ 6)
- ✅ Fascia disclaimer nei fotogrammi decodificati (gif, 10 campioni): deviazione max 2.0 (≤ 6)
- ✅ End frame decodificato (web): luminanza cifre 255€ (p90) 253 vs fondo card 28 (≥ 40 di differenza)
- ✅ End frame decodificato (gif): luminanza cifre 255€ (p90) 255 vs fondo card 29 (≥ 40 di differenza)

- **ESITO COMPLESSIVO 300x250: TUTTI I CONTROLLI AUTOMATICI SUPERATI**


## Controlli automatici 336x280 (qc_check_vertical.py)

- ✅ Fotogrammi: 250 (atteso 250) · dimensione (336, 280) (atteso (336, 280))
- ✅ CTA presente e integra (pill lime + testo scuro, x ≥ 3, fondo ≤ 230) dal f33 al f249: tutti
- ✅ Posizione CTA grande (S1) f35–f46: scarto max dal layout (78, 134, 180, 42) = 0 px (soglia 3)
- ✅ Posizione CTA media (S2–S4) f62–f180: scarto max dal layout (78, 178, 180, 40) = 0 px (soglia 3)
- ✅ Posizione CTA finale (S5, prima del pulse) f195–f221: scarto max dal layout (78, 188, 180, 36) = 0 px (soglia 3)
- ✅ Fascia disclaimer 0,246 336×34 piatta #061a12 su tutti i 250 fotogrammi (wipe e pulse inclusi): tutti
- ✅ Pari trattamento sequenziale (stessi tempi relativi, stessa altezza dei valori ±1 px): Sisal: card a u=0,20 (lum 33), valore completo a u=1,05 e stabile a u=1,45 → sì, altezza cifre 19 px · NetBet: card a u=0,20 (lum 33), valore completo a u=1,05 e stabile a u=1,45 → sì, altezza cifre 19 px · William Hill: card a u=0,20 (lum 33), valore completo a u=1,05 e stabile a u=1,45 → sì, altezza cifre 19 px
- ✅ Proporzioni dell'inchiostro dei loghi nelle hero card vs PNG ufficiali ridotti alla stessa larghezza (render 2x, soglia luminanza 100, tolleranza 5 %: sensibile al ricampionamento dei tratti sottili): Sisal 3.04 vs riferimento 3.08 (1.3 %) · NetBet 5.51 vs riferimento 5.51 (0.0 %) · William Hill 4.79 vs riferimento 4.85 (1.3 %)
- ✅ Box <img> dei loghi nel DOM non deformati (rapporto elemento = rapporto file PNG, tolleranza 0,5 %): Sisal elemento 136.0×43.4 = 3.134 vs file 3.136 (0.07 %) · NetBet elemento 130.0×33.8 = 3.846 vs file 3.839 (0.17 %) · William Hill elemento 160.0×53.3 = 3.002 vs file 3.000 (0.06 %)
- ✅ Valori nel template esattamente come da brief, 2 occorrenze ciascuno (hero + card): {'5.200€': 2, '1.000€': 2, '255€': 2} · testi vietati: nessuno
- ✅ Master MP4: 0.67 MB · durata 00:00:10.00 · audio sì (atteso sì)
- ✅ Web MP4: 0.37 MB (limite 3,5 MB) · durata 00:00:10.00 · audio sì (atteso sì)
- ✅ Web MP4 MUTO: 0.20 MB (limite 3,5 MB) · durata 00:00:10.00 · audio no (atteso no)
- ✅ GIF di controllo: 2.30 MB (limite 3,5 MB) · durata 00:00:10.00 · audio no (atteso no)
- ✅ Audio (web): loudness integrata -20.1 LUFS (target −20 ±1) · true peak -5.8 dBTP (≤ −1)
- ✅ Coda audio: ultimo suono sopra −60 dB a 9.93 s (≤ 9,95 s)
- ✅ Nessuna voce: bed = stessa clip stadio Higgsfield del master (whisper base + VAD: 0 segmenti di parlato) + SFX procedurali numpy; nessun modello TTS/voce invocato
- ✅ Fascia disclaimer nei fotogrammi decodificati (web, 10 campioni): deviazione max 3.0 (≤ 6)
- ✅ Fascia disclaimer nei fotogrammi decodificati (gif, 10 campioni): deviazione max 2.0 (≤ 6)
- ✅ End frame decodificato (web): luminanza cifre 255€ (p90) 253 vs fondo card 28 (≥ 40 di differenza)
- ✅ End frame decodificato (gif): luminanza cifre 255€ (p90) 255 vs fondo card 29 (≥ 40 di differenza)

- **ESITO COMPLESSIVO 336x280: TUTTI I CONTROLLI AUTOMATICI SUPERATI**


## Controlli automatici 1920x1080 (qc_check_vertical.py)

- ✅ Fotogrammi: 250 (atteso 250) · dimensione (1920, 1080) (atteso (1920, 1080))
- ✅ CTA presente e integra (pill lime + testo scuro, x ≥ 3, fondo ≤ 952) dal f33 al f249: tutti
- ✅ Posizione CTA grande (S1) f35–f46: scarto max dal layout (680, 554, 560, 120) = 0 px (soglia 3)
- ✅ Posizione CTA media (S2–S4) f62–f180: scarto max dal layout (700, 702, 520, 110) = 0 px (soglia 3)
- ✅ Posizione CTA finale (S5, prima del pulse) f195–f221: scarto max dal layout (700, 748, 520, 110) = 0 px (soglia 3)
- ✅ Fascia disclaimer 0,972 1920×108 piatta #061a12 su tutti i 250 fotogrammi (wipe e pulse inclusi): tutti
- ✅ Pari trattamento sequenziale (stessi tempi relativi, stessa altezza dei valori ±1 px): Sisal: card a u=0,20 (lum 36), valore completo a u=1,05 e stabile a u=1,45 → sì, altezza cifre 80 px · NetBet: card a u=0,20 (lum 34), valore completo a u=1,05 e stabile a u=1,45 → sì, altezza cifre 80 px · William Hill: card a u=0,20 (lum 36), valore completo a u=1,05 e stabile a u=1,45 → sì, altezza cifre 80 px
- ✅ Proporzioni dell'inchiostro dei loghi nelle hero card vs PNG ufficiali ridotti alla stessa larghezza (render 2x, soglia luminanza 100, tolleranza 5 %: sensibile al ricampionamento dei tratti sottili): Sisal 3.10 vs riferimento 3.11 (0.4 %) · NetBet 5.52 vs riferimento 5.52 (0.0 %) · William Hill 4.83 vs riferimento 4.83 (0.0 %)
- ✅ Box <img> dei loghi nel DOM non deformati (rapporto elemento = rapporto file PNG, tolleranza 0,5 %): Sisal elemento 520.0×165.8 = 3.136 vs file 3.136 (0.02 %) · NetBet elemento 494.0×128.7 = 3.838 vs file 3.839 (0.03 %) · William Hill elemento 610.0×203.3 = 3.000 vs file 3.000 (0.02 %)
- ✅ Valori nel template esattamente come da brief, 2 occorrenze ciascuno (hero + card): {'5.200€': 2, '1.000€': 2, '255€': 2} · testi vietati: nessuno
- ✅ Master MP4: 9.32 MB · durata 00:00:10.00 · audio sì (atteso sì)
- ✅ Web MP4: 2.61 MB (limite 3,5 MB) · durata 00:00:10.00 · audio sì (atteso sì)
- ✅ Web MP4 MUTO: 2.45 MB (limite 3,5 MB) · durata 00:00:10.00 · audio no (atteso no)
- ✅ GIF di controllo: 3.35 MB (limite 3,5 MB) · durata 00:00:10.00 · audio no (atteso no)
- ✅ Audio (web): loudness integrata -20.1 LUFS (target −20 ±1) · true peak -5.8 dBTP (≤ −1)
- ✅ Coda audio: ultimo suono sopra −60 dB a 9.93 s (≤ 9,95 s)
- ✅ Nessuna voce: bed = stessa clip stadio Higgsfield del master (whisper base + VAD: 0 segmenti di parlato) + SFX procedurali numpy; nessun modello TTS/voce invocato
- ✅ Fascia disclaimer nei fotogrammi decodificati (web, 10 campioni): deviazione max 3.0 (≤ 6)
- ✅ Fascia disclaimer nei fotogrammi decodificati (gif 720x405, 10 campioni): deviazione max 1.0 (≤ 6)
- ✅ End frame decodificato (web): luminanza cifre 255€ (p90) 255 vs fondo card 27 (≥ 40 di differenza)
- ✅ End frame decodificato (gif): luminanza cifre 255€ (p90) 255 vs fondo card 29 (≥ 40 di differenza)

- **ESITO COMPLESSIVO 1920x1080: TUTTI I CONTROLLI AUTOMATICI SUPERATI**
