# Famiglia orizzontale 1920×1080 · 300×250 · 336×280

Master di riferimento: **970×250 concept M rev 2** (commit `429e807`), non toccato. Metodo e pipeline della famiglia verticale (approvata e prodotta). **Fase: storyboard consegnati, in attesa di approvazione** — nessun MP4/GIF prodotto. Durata 10,0 s · 25 fps · **con audio** (traccia del master ri-temporizzata; opzione 12 s per il solo 1920×1080, da decidere al gate).

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

Sorgente parametrico: `src/banner_horizontal.html` (`?size=…&t=…&mode=final|wire&safe=1&grid=1`) e `src/render_horizontal.mjs`. Rigenerare i frame: `node src/render_horizontal.mjs --size 1920x1080 --times 0.6,1.5,2.15,3.3,4.9,6.9,8.2,9.96 --out 1920x1080/storyboard --prefix sb_1920x1080`.
