# Bonus Sport — banner dinamico di comparazione 970×250 (Sisal · NetBet · William Hill)

**Stato: PRODUZIONE (approvazione con modifiche ricevuta il 2026-09-10: 9 s, senza etichetta criterio, alone attivo, ordine confermato, motion graphics di livello superiore). Master, versione web, GIF di controllo e report QC in `10_export/` e `11_qc/`.**

## Consegna di produzione
- `10_export/BonusSport_970x250_25fps_9s_MASTER.mp4` — master H.264 CRF 12 (+ copia archivio yuv444p)
- `10_export/BonusSport_970x250_25fps_9s_WEB.mp4` — versione di distribuzione (≤ 3,5 MB)
- `10_export/BonusSport_970x250_CONTROL.gif` — GIF di controllo (≤ 3,5 MB, ambiente fermo)
- `10_export/BonusSport_970x250_25fps_9s_ENDFRAME_fallback_statico.png` — end frame
- `11_qc/report_qc.md` — controlli automatici e visivi
- `06_storyboard/storyboard_v2_contact_sheet.png` — storyboard definitivo dai fotogrammi del master
- Pipeline riproducibile: `08_progetto/make_master.sh` (render 2× → Lanczos → ffmpeg)

## Dove guardare (in ordine)
1. `06_storyboard/storyboard_contact_sheet.png` — lo storyboard scena per scena (11 fotogrammi reali 970×250, safe area evidenziata).
2. `05_concept/styleframe_contact_sheet.png` — confronto delle direzioni A / B / C.
3. `05_concept/concept.md` — direzioni, razionale, punti di forza/criticità, raccomandazione.
4. `06_storyboard/storyboard.md` — durata, fotogrammi, cosa è statico/animato, gerarchia, ruolo di Sisal, spazio, loop.
5. `04_brand_identity/brand_audit.md` — **blocco di accesso a sisal.it documentato** + tutto ciò che è osservabile dagli asset ufficiali; richiesta materiali.
6. `02_analisi/analisi_ricerca.md` — analisi critica del PDF (osservato / dichiarato / dedotto / proposto).
7. `07_asset_generati/README_higgsfield.md` — capacità, costi, esplorazione (4 still) e piano d'uso di Higgsfield MCP.
8. `11_qc/piano_produzione.md`, `piano_qc.md`, `strategia_compressione.md` — piani e misure reali di compressione.

## Struttura delle cartelle
```
00_ricerca/            PDF di ricerca (input)
01_loghi/              loghi ufficiali (input, mai modificati)
02_analisi/            analisi del PDF, testo estratto, pagine rasterizzate
03_fonti/              registro fonti con URL/data/classificazione
04_brand_identity/     audit (parziale), log del blocco, font sostitutivi (OFL)
05_concept/            concept.md, styleframe/, styleframe_contact_sheet.png
06_storyboard/         storyboard.md, frames/ (con safe area), frames_clean/, contact sheet
07_asset_generati/     README Higgsfield + preview delle 4 immagini esplorative
08_progetto/           PROGETTO MODIFICABILE: banner.html (template deterministico), render.mjs, config.json, assets/
09_preview/            test di pipeline (non definitivi): MP4/GIF di prova per le misure di peso
10_export/             (vuoto) master, web, GIF — dopo approvazione
11_qc/                 piani di produzione, QC e compressione; report QC dopo produzione
```

## Come rigenerare un fotogramma o lo storyboard
```
cd 08_progetto
node render.mjs --times 0,2.7,9 --out ../06_storyboard/frames --safe 1 --bg assets/env/env_A_pitch_PREVIEW.jpg --prefix scena
# oppure aprire banner.html?t=4.4&safe=1&bg=assets/env/env_A_pitch_PREVIEW.jpg in Chromium
```

## Dati della comparazione (dal brief, non modificati)
Sisal — FINO A 5.200€ · NetBet — FINO A 1.000€ · William Hill — FINO A 255€ · Criterio: importo massimo dichiarato del bonus sport.

## Nota sullo stato del push (2026-09-10)
Da questa sessione **non è possibile scrivere sul repository GitHub**: il push via git è rifiutato (403: "Claude doesn't have GitHub access to antoniobarbatodt9/Comparazione_Bonus_Sport_Sisal for your organization") e anche la creazione del branch via API GitHub è rifiutata (403 "Resource not accessible by integration"). I commit esistono sul branch locale `claude/intelligent-feynman-sqxtf5` della sessione. La consegna completa (137 file, 17,9 MB) è nello zip `consegna_01_concept_storyboard.zip` inviato in chat. Per allineare GitHub: installare la Claude GitHub App sul repo (https://github.com/apps/claude/installations/select_target) o ricollegare GitHub da claude.ai (Settings → Connectors) e chiedere di ripetere il push; in alternativa estrarre lo zip nella root del repo e committare.

## Gate di approvazione
Per procedere alla produzione occorre un'approvazione esplicita di concept e storyboard, e (per chiudere il brand audit) lo sblocco di `www.sisal.it` oppure screenshot/materiali ufficiali. Dettagli in `04_brand_identity/brand_audit.md` §1.
