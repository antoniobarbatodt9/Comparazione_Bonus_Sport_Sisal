# Famiglia verticale 300×600 · 320×480 · 160×600

Master di riferimento: **970×250 concept M rev 2** (commit `429e807`), unico usato; il progetto 970×250 non è stato toccato. Storyboard approvati il 2026-09-11; **produzione completata**: file in `10_export/vertical/`, QC in `11_qc/report_qc_vertical.md`, pipeline `src/make_vertical.sh`. Durata 10,0 s · 25 fps · con audio (stessa traccia del master ri-temporizzata, vedi `family_system/motion_system.md` §Audio); variante WEB_MUTO per i placement senza audio.

| # | Consegna | Dove |
|---|---|---|
| 1 | Pre-flight audit (inventario master, layout, UX, invarianti/adattabili/critici) | `preflight_audit/` |
| 2 | Sistema di famiglia (griglia, tipografia, motion, sfondo, Higgsfield) | `family_system/` |
| 3 | Griglie per size (px) | `family_system/grid_system.md` + `<size>/layout_spec.md` |
| 4 | Wireframe (griglia + safe, 3 momenti) | `<size>/wireframes/` |
| 5 | Styleframe (3 momenti; variante con griglia e safe) | `<size>/styleframes/` |
| 6 | Storyboard (8 momenti chiave a risoluzione nativa, con/senza overlay safe) | `<size>/storyboard/` |
| 7 | Tavola comparativa multisize + confronto con il master | `comparative_storyboards/` |
| 8 | Safe area per size (px, stato durante l'animazione) | `<size>/safe_area.md` |
| 9 | Check report (Check 1–4, tabelle PASS/FAIL con correzioni) | `checkpoints/check_report.md` |
| 10 | Piano Higgsfield (nessuna generazione, 0 crediti) | `family_system/higgsfield_strategy.md`, `07_asset_generati/README_higgsfield.md` §9 |
| 11 | Piano di produzione, qualità, compressione | `production_plan/` |
| 12 | Criticità e correzioni | `checkpoints/check_report.md` (C1–C4) e `preflight_audit/layout_audit.md` (P1–P10) |

Sorgente parametrico: `src/banner_vertical.html` (URL `?size=…&t=…&mode=final|wire&safe=1&grid=1`) e `src/render_vertical.mjs`. Rigenerare i frame: `node src/render_vertical.mjs --size 300x600 --times 0.6,1.5,2.15,3.3,4.9,6.9,8.2,9.96 --out 300x600/storyboard --prefix sb_300x600`.
