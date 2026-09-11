# Report QC — famiglia verticale 300×600 · 320×480 · 160×600 (produzione 2026-09-11)

Master di riferimento: concept M rev 2 (970×250). Storyboard approvati dal cliente il 2026-09-11 ("perfette, valido gli storyboard"). Durata 10,0 s · 25 fps · 250 fotogrammi · **senza audio** (brief). Sfondo: ri-inquadratura verticale 896×1344 dello stesso still Higgsfield approvato (0 crediti). Pipeline: `adaptations/vertical_family/src/make_vertical.sh` (render 2× deterministico → Lanczos → x264 → GIF), QC: `11_qc/qc_check_vertical.py`.

## File consegnati (`10_export/vertical/`)

| Size | MASTER.mp4 (CRF 12, 4:2:0) | MASTER_444_archivio.mov | WEB.mp4 (CRF 17, ≤ 3,5 MB) | CONTROL.gif (≤ 3,5 MB) | ENDFRAME PNG |
|---|---|---|---|---|---|
| 300x600 | 0.94 MB | 1.31 MB | **0.39 MB** | **2.60 MB** (12,5 fps) | 185 KB |
| 320x480 | 0.80 MB | 1.11 MB | **0.33 MB** | **2.34 MB** (12,5 fps) | 155 KB |
| 160x600 | 0.50 MB | 0.68 MB | **0.23 MB** | **2.31 MB** (25 fps) | 108 KB |

Note: GIF a 25 fps oltre i 3,5 MB per 300×600 (3,98 MB) e 320×480 (3,63 MB) → fallback automatico a 12,5 fps come da piano di compressione; 160×600 resta a 25 fps. Tutti i file sono privi di traccia audio; la fascia disclaimer è vuota e piatta in ogni fotogramma.

## Controlli visivi sui fotogrammi decodificati
`11_qc/decodificati_vertical/contact_decodificati_vertical.png`: 8 momenti chiave × 3 size decodificati dai WEB.mp4 — titolo, hero card, confronto e CTA leggibili a 100 %; fascia disclaimer libera; nessun elemento tagliato; end frame completo (fallback statico coerente).

## Criticità e correzioni in fase di produzione
- Sfondo 2×: il ritaglio 800×1200 usato per gli storyboard è stato sostituito dal ritaglio 896×1344 a qualità piena (differenza media tra i frame < 1/255); nessuna nuova generazione.
- Rilevatore QC della CTA in S1: nella prima esecuzione la finestra di ricerca includeva il regolo lime del titolo (falso negativo di 28 px); finestra corretta a 6 px sotto il regolo. Nessuna modifica al banner.
- Misura dei loghi: la misura "a inchiostro" (soglia 170) sui tratti sottili del logo NetBet dava 4,1–4,4 % di scarto per ricampionamento; il controllo ora confronta il render con il PNG ufficiale ridotto alla stessa larghezza (soglia 100, tolleranza 5 %) e aggiunge la verifica geometrica del box `<img>` nel DOM (rapporto elemento = rapporto file, scarto ≤ 0,08 %): nessuna deformazione. Nessuna modifica al banner.


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
- ✅ Master MP4: 0.94 MB · durata 00:00:10.00 · audio no (atteso no)
- ✅ Web MP4: 0.39 MB (limite 3,5 MB) · durata 00:00:10.00 · audio no (atteso no)
- ✅ GIF di controllo: 2.60 MB (limite 3,5 MB) · durata 00:00:10.00 · audio no (atteso no)
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
- ✅ Master MP4: 0.80 MB · durata 00:00:10.00 · audio no (atteso no)
- ✅ Web MP4: 0.33 MB (limite 3,5 MB) · durata 00:00:10.00 · audio no (atteso no)
- ✅ GIF di controllo: 2.34 MB (limite 3,5 MB) · durata 00:00:10.00 · audio no (atteso no)
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
- ✅ Master MP4: 0.50 MB · durata 00:00:10.00 · audio no (atteso no)
- ✅ Web MP4: 0.23 MB (limite 3,5 MB) · durata 00:00:10.00 · audio no (atteso no)
- ✅ GIF di controllo: 2.31 MB (limite 3,5 MB) · durata 00:00:10.00 · audio no (atteso no)
- ✅ Fascia disclaimer nei fotogrammi decodificati (web, 10 campioni): deviazione max 3.0 (≤ 6)
- ✅ Fascia disclaimer nei fotogrammi decodificati (gif, 10 campioni): deviazione max 2.0 (≤ 6)
- ✅ End frame decodificato (web): luminanza fascia valore 255€ 130 vs fondo card 28 (≥ 40 di differenza)
- ✅ End frame decodificato (gif): luminanza fascia valore 255€ 131 vs fondo card 28 (≥ 40 di differenza)

- **ESITO COMPLESSIVO 160x600: TUTTI I CONTROLLI AUTOMATICI SUPERATI**

