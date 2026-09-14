# Report QC — famiglia orizzontale 1920×1080 · 300×250 · 336×280 (produzione 2026-09-14)

Master di riferimento: concept M rev 2 (970×250). Storyboard approvati dal cliente il 2026-09-14 ("approvo, passa alla creazione"). Durata 10,0 s · 25 fps · 250 fotogrammi · **con audio** (traccia del master ri-temporizzata a 10 s, profilo `horizontal` di `08_progetto/audio/make_audio.py`: come il profilo `vertical` ma con panoramica L→R sui whoosh perché il wipe è orizzontale come nel master; −20 LUFS, TP ≤ −1 dBTP); `10_export/horizontal/audio/` contiene WAV 48 kHz 24 bit e misura. Sfondo: ri-inquadratura 16:9 dello stesso still Higgsfield approvato (0 crediti). Pipeline: `adaptations/horizontal_family/src/make_horizontal.sh` (render 2× deterministico → Lanczos → x264 → GIF), QC: `11_qc/qc_check_horizontal.py`.

Il 1920×1080 è prodotto a 10 s come lo storyboard approvato (l'opzione 12 s con la timeline del master resta disponibile su richiesta).

## File consegnati (`10_export/horizontal/`)

TABELLA_FILE

## Note sulla compressione
NOTE_COMPRESSIONE


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
