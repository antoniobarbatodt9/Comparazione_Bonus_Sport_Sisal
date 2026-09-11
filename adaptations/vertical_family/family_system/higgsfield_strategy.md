# Strategia Higgsfield per la famiglia verticale

Vincoli (invariati): Higgsfield non produce mai loghi, nomi operatore, importi, €, CTA, disclaimer o testi leggibili; nessun elemento IP; nessuna generazione definitiva in questa fase.

## Valutazione asset per asset

| Asset del master | Origine | Decisione per le verticali | Motivazione |
|---|---|---|---|
| Still campo zenitale (job `e190625a…`, nano_banana_2, 3168×1344) | Higgsfield | **Riuso con ri-inquadratura** (fascia centrale verticale 896×1344 → 800×1200) | il soggetto è simmetrico e centrato; la fascia verticale contiene cerchio + linea; nessuna deformazione. 0 crediti |
| Clip stadio con audio (job `9d228081…`, veo3_1) | Higgsfield | **Non usata** | audio: nessuno (brief). Non serve la componente video |
| Still ambiente concept A (`env_A_pitch_FINAL`) e varianti scartate (#22–#24) | Higgsfield | **Esclusi** | non fanno parte del master approvato |
| Titolo, loghi, valori, CTA, regoli, card, particelle, wipe | DOM/CSS deterministico | riuso nel template verticale | non sono materia Higgsfield |

## Eventuali generazioni (solo se richieste dopo l'approvazione)
Nessuna è necessaria per produrre le tre size. Se in produzione a 2× si volesse più risoluzione sullo sfondo:
1. **opzione A (preferita, 0 crediti)**: nuovo trasferimento della stessa fascia 896×1344 a qualità superiore (q84, ≈ 200 KB) — è lo stesso file sorgente già presente nel sandbox/CDN del job;
2. **opzione B (upscale, ~2–4 crediti)**: `upscale_image` del solo still approvato, poi stessa ri-inquadratura; da valutare solo con test A/B a 100 %, perché l'upscale può introdurre micro-texture sull'erba diversa dal master;
3. **opzione C (estensione, sconsigliata)**: `outpaint_image` per allungare verticalmente — non necessaria (il ritaglio copre già tutti i formati) e rischia elementi non richiesti (bordi campo, tribune).

Nessun modello viene pre-scelto: la scelta tra A/B avviene solo se il check 4 sui frame 2× mostrasse morbidezza eccessiva (non riscontrata a 1×).

## Registro
Crediti spesi in questa fase: **0**. Job avviati: **0**. Voce aggiunta a `07_asset_generati/README_higgsfield.md` §9.
