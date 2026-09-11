# Report QC — famiglia verticale 300×600 · 320×480 · 160×600 (produzione 2026-09-11)

Master di riferimento: concept M rev 2 (970×250). Storyboard approvati dal cliente il 2026-09-11 ("perfette, valido gli storyboard"). Durata 10,0 s · 25 fps · 250 fotogrammi · **con audio** (revisione del 2026-09-11: "l'audio deve restare sempre"; il brief iniziale indicava audio: nessuno). Traccia: bed stadio reale della clip Higgsfield del master + SFX procedurali, ri-temporizzata a 10 s (`08_progetto/audio/make_audio.py --profile vertical`, −20 LUFS, TP ≤ −1 dBTP); `10_export/vertical/audio/` contiene WAV 48 kHz 24 bit e misura. Sfondo: ri-inquadratura verticale 896×1344 dello stesso still Higgsfield approvato (0 crediti). Pipeline: `adaptations/vertical_family/src/make_vertical.sh` (render 2× deterministico → Lanczos → x264 → GIF), QC: `11_qc/qc_check_vertical.py`.

## File consegnati (`10_export/vertical/`)

| Size | MASTER.mp4 (CRF 12, AAC 192k) | MASTER_444_archivio.mov (PCM 24 bit) | WEB.mp4 (CRF 17, AAC 128k, ≤ 3,5 MB) | WEB_MUTO.mp4 | CONTROL.gif (≤ 3,5 MB) | ENDFRAME PNG |
|---|---|---|---|---|---|---|
| 300x600 | 1.19 MB | 4.20 MB | **0.55 MB** | 0.39 MB | **2.60 MB** (12,5 fps) | 185 KB |
| 320x480 | 1.04 MB | 4.00 MB | **0.50 MB** | 0.33 MB | **2.34 MB** (12,5 fps) | 155 KB |
| 160x600 | 0.75 MB | 3.56 MB | **0.39 MB** | 0.23 MB | **2.31 MB** (25 fps) | 108 KB |
- Audio: prima esportazione muta per aderenza letterale al brief ("audio: nessuno"); su richiesta del cliente la traccia del master è stata ri-temporizzata a 10 s e remixata (whoosh senza panoramica L→R perché il wipe è verticale; ping del pulse a 8,90 e 9,45 s; dissolvenza finale di 80 ms così che l'ultimo suono cada a 9,93 s). Il profilo `master` di `make_audio.py` produce misure identiche a prima (−20,0 LUFS, −5,5 dBTP, ultimo evento 11,90 s): il 970×250 non cambia.


## Controlli automatici 300x600 (qc_check_vertical.py)

- ✅ Fotogrammi: 250 (atteso 250) · dimensione (300, 600) (atteso (300, 600))
- ✅ CTA presente e integra (pill lime + testo scuro, x ≥ 3, fondo ≤ 520) dal f33 al f249: tutti
- ✅ Posizione CTA grande (S1) f35–f46: scarto max dal layout (40, 316, 220, 52) = 0 px (soglia 3)
- ✅ Posizione CTA media (S2–S4) f62–f180: scarto max dal layout (50, 350, 200, 48) = 0 px (soglia 3)
- ✅ Posizione CTA finale (S5, prima del pulse) f195–f221: scarto max dal layout (50, 444, 200, 48) = 0 px (soglia 3)
- ✅ Fascia disclaimer 0,540 300×60 piatta #061a12 su tutti i 250 fotogrammi (wipe e pulse inclusi): tutti
- ✅ Pari trattamento sequenziale (stessi tempi relativi, stessa altezza dei valori ±1 px): Sisal: card a u=0,20 (lum 34), valore completo a u=1,05 e stabile a u=1,45 → sì, altezza cifre 23 px · NetBet: card a u=0,20 (lum 33), valore completo a u=1,05 e stabile a u=1,45 → sì, altezza cifre 23 px · William Hill: card a u=0,20 (lum 34), valore completo a u=1,05 e stabile a u=1,45 → sì, altezza cifre 23 px
- ✅ Proporzioni dell'inchiostro dei loghi nelle hero card vs PNG ufficiali ridotti alla stessa larghezza (render 2x, soglia luminanza 100, tolleranza 5 %: sensibile al ricampionamento dei tratti sottili): Sisal 3.11 vs riferimento 3.11 (0.0 %) · NetBet 5.63 vs riferimento 5.51 (2.2 %) · William Hill 4.85 vs riferimento 4.85 (0.0 %)
- ✅ Box <img> dei loghi nel DOM non deformati (rapporto elemento = rapporto file PNG, tolleranza 0,5 %): Sisal elemento 150.0×47.8 = 3.138 vs file 3.136 (0.08 %) · NetBet elemento 142.0×37.0 = 3.838 vs file 3.839 (0.04 %) · William Hill elemento 175.0×58.3 = 3.002 vs file 3.000 (0.06 %)
- ✅ Valori nel template esattamente come da brief, 2 occorrenze ciascuno (hero + card): {'5.200€': 2, '1.000€': 2, '255€': 2} · testi vietati: nessuno
- ✅ Master MP4: 1.19 MB · durata 00:00:10.00 · audio sì (atteso sì)
- ✅ Web MP4: 0.55 MB (limite 3,5 MB) · durata 00:00:10.00 · audio sì (atteso sì)
- ✅ Web MP4 MUTO: 0.39 MB (limite 3,5 MB) · durata 00:00:10.00 · audio no (atteso no)
- ✅ GIF di controllo: 2.60 MB (limite 3,5 MB) · durata 00:00:10.00 · audio no (atteso no)
- ✅ Audio (web): loudness integrata -20.1 LUFS (target −20 ±1) · true peak -5.9 dBTP (≤ −1)
- ✅ Coda audio: ultimo suono sopra −60 dB a 9.93 s (≤ 9,95 s)
- ✅ Nessuna voce: bed = stessa clip stadio Higgsfield del master (whisper base + VAD: 0 segmenti di parlato) + SFX procedurali numpy; nessun modello TTS/voce invocato
- ✅ Fascia disclaimer nei fotogrammi decodificati (web, 10 campioni): deviazione max 3.0 (≤ 6)
- ✅ Fascia disclaimer nei fotogrammi decodificati (gif, 10 campioni): deviazione max 1.0 (≤ 6)
- ✅ End frame decodificato (web): luminanza fascia valore 255€ 126 vs fondo card 27 (≥ 40 di differenza)
- ✅ End frame decodificato (gif): luminanza fascia valore 255€ 128 vs fondo card 29 (≥ 40 di differenza)

- **ESITO COMPLESSIVO 300x600: TUTTI I CONTROLLI AUTOMATICI SUPERATI**


## Controlli automatici 320x480 (qc_check_vertical.py)

- ✅ Fotogrammi: 250 (atteso 250) · dimensione (320, 480) (atteso (320, 480))
- ✅ CTA presente e integra (pill lime + testo scuro, x ≥ 3, fondo ≤ 410) dal f33 al f249: tutti
- ✅ Posizione CTA grande (S1) f35–f46: scarto max dal layout (60, 254, 200, 46) = 0 px (soglia 3)
- ✅ Posizione CTA media (S2–S4) f62–f180: scarto max dal layout (70, 284, 180, 44) = 0 px (soglia 3)
- ✅ Posizione CTA finale (S5, prima del pulse) f195–f221: scarto max dal layout (70, 360, 180, 44) = 0 px (soglia 3)
- ✅ Fascia disclaimer 0,430 320×50 piatta #061a12 su tutti i 250 fotogrammi (wipe e pulse inclusi): tutti
- ✅ Pari trattamento sequenziale (stessi tempi relativi, stessa altezza dei valori ±1 px): Sisal: card a u=0,20 (lum 34), valore completo a u=1,05 e stabile a u=1,45 → sì, altezza cifre 22 px · NetBet: card a u=0,20 (lum 33), valore completo a u=1,05 e stabile a u=1,45 → sì, altezza cifre 22 px · William Hill: card a u=0,20 (lum 34), valore completo a u=1,05 e stabile a u=1,45 → sì, altezza cifre 22 px
- ✅ Proporzioni dell'inchiostro dei loghi nelle hero card vs PNG ufficiali ridotti alla stessa larghezza (render 2x, soglia luminanza 100, tolleranza 5 %: sensibile al ricampionamento dei tratti sottili): Sisal 3.11 vs riferimento 3.11 (0.0 %) · NetBet 5.63 vs riferimento 5.51 (2.2 %) · William Hill 4.85 vs riferimento 4.85 (0.0 %)
- ✅ Box <img> dei loghi nel DOM non deformati (rapporto elemento = rapporto file PNG, tolleranza 0,5 %): Sisal elemento 150.0×47.8 = 3.138 vs file 3.136 (0.08 %) · NetBet elemento 142.0×37.0 = 3.838 vs file 3.839 (0.04 %) · William Hill elemento 175.0×58.3 = 3.002 vs file 3.000 (0.06 %)
- ✅ Valori nel template esattamente come da brief, 2 occorrenze ciascuno (hero + card): {'5.200€': 2, '1.000€': 2, '255€': 2} · testi vietati: nessuno
- ✅ Master MP4: 1.04 MB · durata 00:00:10.00 · audio sì (atteso sì)
- ✅ Web MP4: 0.50 MB (limite 3,5 MB) · durata 00:00:10.00 · audio sì (atteso sì)
- ✅ Web MP4 MUTO: 0.33 MB (limite 3,5 MB) · durata 00:00:10.00 · audio no (atteso no)
- ✅ GIF di controllo: 2.34 MB (limite 3,5 MB) · durata 00:00:10.00 · audio no (atteso no)
- ✅ Audio (web): loudness integrata -20.1 LUFS (target −20 ±1) · true peak -5.9 dBTP (≤ −1)
- ✅ Coda audio: ultimo suono sopra −60 dB a 9.93 s (≤ 9,95 s)
- ✅ Nessuna voce: bed = stessa clip stadio Higgsfield del master (whisper base + VAD: 0 segmenti di parlato) + SFX procedurali numpy; nessun modello TTS/voce invocato
- ✅ Fascia disclaimer nei fotogrammi decodificati (web, 10 campioni): deviazione max 3.0 (≤ 6)
- ✅ Fascia disclaimer nei fotogrammi decodificati (gif, 10 campioni): deviazione max 1.0 (≤ 6)
- ✅ End frame decodificato (web): luminanza fascia valore 255€ 139 vs fondo card 39 (≥ 40 di differenza)
- ✅ End frame decodificato (gif): luminanza fascia valore 255€ 140 vs fondo card 41 (≥ 40 di differenza)

- **ESITO COMPLESSIVO 320x480: TUTTI I CONTROLLI AUTOMATICI SUPERATI**


## Controlli automatici 160x600 (qc_check_vertical.py)

- ✅ Fotogrammi: 250 (atteso 250) · dimensione (160, 600) (atteso (160, 600))
- ✅ CTA presente e integra (pill lime + testo scuro, x ≥ 3, fondo ≤ 524) dal f33 al f249: tutti
- ✅ Posizione CTA grande (S1) f35–f46: scarto max dal layout (12, 300, 136, 40) = 0 px (soglia 3)
- ✅ Posizione CTA media (S2–S4) f62–f180: scarto max dal layout (12, 330, 136, 40) = 0 px (soglia 3)
- ✅ Posizione CTA finale (S5, prima del pulse) f195–f221: scarto max dal layout (12, 456, 136, 40) = 0 px (soglia 3)
- ✅ Fascia disclaimer 0,544 160×56 piatta #061a12 su tutti i 250 fotogrammi (wipe e pulse inclusi): tutti
- ✅ Pari trattamento sequenziale (stessi tempi relativi, stessa altezza dei valori ±1 px): Sisal: card a u=0,20 (lum 34), valore completo a u=1,05 e stabile a u=1,45 → sì, altezza cifre 17 px · NetBet: card a u=0,20 (lum 35), valore completo a u=1,05 e stabile a u=1,45 → sì, altezza cifre 17 px · William Hill: card a u=0,20 (lum 34), valore completo a u=1,05 e stabile a u=1,45 → sì, altezza cifre 17 px
- ✅ Proporzioni dell'inchiostro dei loghi nelle hero card vs PNG ufficiali ridotti alla stessa larghezza (render 2x, soglia luminanza 100, tolleranza 5 %: sensibile al ricampionamento dei tratti sottili): Sisal 3.03 vs riferimento 3.11 (2.3 %) · NetBet 5.45 vs riferimento 5.45 (0.0 %) · William Hill 4.91 vs riferimento 4.81 (2.2 %)
- ✅ Box <img> dei loghi nel DOM non deformati (rapporto elemento = rapporto file PNG, tolleranza 0,5 %): Sisal elemento 104.0×33.2 = 3.133 vs file 3.136 (0.10 %) · NetBet elemento 99.0×25.8 = 3.837 vs file 3.839 (0.06 %) · William Hill elemento 122.0×40.7 = 2.998 vs file 3.000 (0.08 %)
- ✅ Valori nel template esattamente come da brief, 2 occorrenze ciascuno (hero + card): {'5.200€': 2, '1.000€': 2, '255€': 2} · testi vietati: nessuno
- ✅ Master MP4: 0.75 MB · durata 00:00:10.00 · audio sì (atteso sì)
- ✅ Web MP4: 0.39 MB (limite 3,5 MB) · durata 00:00:10.00 · audio sì (atteso sì)
- ✅ Web MP4 MUTO: 0.23 MB (limite 3,5 MB) · durata 00:00:10.00 · audio no (atteso no)
- ✅ GIF di controllo: 2.31 MB (limite 3,5 MB) · durata 00:00:10.00 · audio no (atteso no)
- ✅ Audio (web): loudness integrata -20.1 LUFS (target −20 ±1) · true peak -5.9 dBTP (≤ −1)
- ✅ Coda audio: ultimo suono sopra −60 dB a 9.93 s (≤ 9,95 s)
- ✅ Nessuna voce: bed = stessa clip stadio Higgsfield del master (whisper base + VAD: 0 segmenti di parlato) + SFX procedurali numpy; nessun modello TTS/voce invocato
- ✅ Fascia disclaimer nei fotogrammi decodificati (web, 10 campioni): deviazione max 3.0 (≤ 6)
- ✅ Fascia disclaimer nei fotogrammi decodificati (gif, 10 campioni): deviazione max 2.0 (≤ 6)
- ✅ End frame decodificato (web): luminanza fascia valore 255€ 130 vs fondo card 28 (≥ 40 di differenza)
- ✅ End frame decodificato (gif): luminanza fascia valore 255€ 131 vs fondo card 28 (≥ 40 di differenza)

- **ESITO COMPLESSIVO 160x600: TUTTI I CONTROLLI AUTOMATICI SUPERATI**
