# Strategia Higgsfield per la famiglia orizzontale

Vincoli invariati: Higgsfield non produce loghi, nomi, importi, €, CTA, disclaimer, testi; nessun elemento IP; nessuna generazione definitiva in questa fase.

| Asset | Origine | Decisione | Motivazione |
|---|---|---|---|
| Still campo zenitale (job `e190625a…`, 3168×1344) | Higgsfield | **riuso con ri-inquadratura 16:9** (2389×1344 → 1920×1080) | contiene per intero l'inquadratura del master; 0 crediti |
| Clip stadio con audio (job `9d228081…`) | Higgsfield | **riuso della sola traccia audio** (già trasferita) | l'audio deve restare sempre |
| Titolo, loghi, valori, CTA, card, wipe, particelle | DOM/CSS | riuso nel template `src/banner_horizontal.html` | non materia Higgsfield |

## Generazioni eventuali (solo dopo approvazione e solo se necessarie)
- Nessuna necessaria per gli storyboard né per la produzione a 1×.
- Per il render 2× del 1920×1080: opzione A (0 crediti) trasferimento del ritaglio 2389×1344 nativo; opzione B `upscale_image` dello still (≈ 2–4 crediti), da valutare solo con test A/B a 100 %; opzione C `outpaint_image`: non necessaria e sconsigliata (rischio di elementi non richiesti ai bordi campo).

## Registro
Crediti spesi in questa fase: **0**. Job avviati: **0**. Voce §9.3 in `07_asset_generati/README_higgsfield.md`.
