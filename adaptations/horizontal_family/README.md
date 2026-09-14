# Famiglia orizzontale 1920×1080 · 300×250 · 336×280

Master di riferimento: **970×250 concept M rev 2** (commit `429e807`), non toccato. Metodo e pipeline della famiglia verticale. Storyboard approvati il 2026-09-14 ("approvo, passa alla creazione"); **produzione completata**: file in `10_export/horizontal/`, QC in `11_qc/report_qc_horizontal.md`, pipeline `src/make_horizontal.sh`. Durata 10,0 s · 25 fps · **con audio** (traccia del master ri-temporizzata, profilo `horizontal`); WEB_MUTO come variante extra. Il 1920×1080 è a 10 s come lo storyboard approvato (opzione 12 s disponibile su richiesta).

| # | Consegna | Dove |
|---|---|---|
| 1 | Pre-flight audit (inventario master, layout, UX, invarianti/ricomponibili/critici) | `preflight_audit/` |
| 2 | Sistema di famiglia (griglia, tipografia, motion + audio, sfondo 16:9, Higgsfield) | `family_system/` |
| 3 | Griglie per size (px) | `family_system/grid_system.md` + `<size>/layout_spec.md` |
| 4 | Wireframe (griglia + safe, 3 momenti) | `<size>/wireframes/` |
| 5 | Styleframe (3 momenti; variante con griglia e safe) | `<size>/styleframes/` |
| 6 | Storyboard (8 momenti chiave a risoluzione nativa, con/senza overlay safe) | `<size>/storyboard/` |
| 7 | Tavola comparativa multisize + confronto con il master | `comparative_storyboards/` |
| 8 | Safe area per size | `<size>/safe_area.md` |
| 9 | Check report (Check 1–4, nessun FAIL) | `checkpoints/check_report.md` |
| 10 | Piano Higgsfield (0 crediti, sfondo 16:9 ri-inquadrato) | `family_system/higgsfield_strategy.md`, `07_asset_generati/README_higgsfield.md` §9.3 |
| 11 | Piano di produzione, qualità, compressione | `production_plan/` |
| 12 | Criticità e correzioni | `checkpoints/check_report.md` (C1–C4), `preflight_audit/layout_audit.md` (P1–P10) |
| 13 | File di consegna (MP4 master/web/muto, GIF, end-frame, audio) | `10_export/horizontal/` |
| 14 | Report QC sui file consegnati + contact sheet dei decodificati | `11_qc/report_qc_horizontal.md`, `11_qc/decodificati_horizontal/` |

Produzione: `bash src/make_horizontal.sh <size>` (render 2× → Lanczos → x264 → GIF). Sorgente parametrico: `src/banner_horizontal.html` (`?size=…&t=…&mode=final|wire&safe=1&grid=1`) e `src/render_horizontal.mjs`. Rigenerare i frame: `node src/render_horizontal.mjs --size 1920x1080 --times 0.6,1.5,2.15,3.3,4.9,6.9,8.2,9.96 --out 1920x1080/storyboard --prefix sb_1920x1080`.
