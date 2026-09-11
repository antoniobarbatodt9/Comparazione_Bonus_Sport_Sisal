# Pre-flight audit · 1 — Inventario del master approvato (famiglia orizzontale)

Fonte unica creativa: **Concept M "Montaggio a scene", revisione 2** — 970×250, 25 fps, 12,0 s, con audio, commit `429e807` (2026-09-10). Il progetto 970×250 non viene toccato; la famiglia verticale (commit `a896faf`) è il precedente diretto per metodo e pipeline.

| Voce | Valore | Evidenza |
|---|---|---|
| Esportazioni master | `10_export/BonusSport_970x250_25fps_12s_M_{MASTER.mp4, MASTER_444_archivio.mov, WEB.mp4, WEB_MUTO.mp4, CONTROL.gif, ENDFRAME_fallback_statico.png}` | `11_qc/report_qc_M.md` |
| Progetto sorgente | `08_progetto/banner_scene.html` + `render_scene.mjs` + `make_master_M.sh` + `config_M.json` | template deterministico, parametro `t` |
| Sfondo approvato | still Higgsfield campo zenitale, job `e190625a-b390-47f4-ba30-cc464acb0373` (nano_banana_2, 3168×1344); master: fascia centrale 3168×927 → `env_M_pitch_topdown_FINAL_2036x596.jpg`; verticali: fascia centrale verticale 896×1344 | `07_asset_generati/README_higgsfield.md` §7, §9 |
| Trattamento sfondo | tinta verde Sisal (`color` 70 % + `screen` 12 %), luminosità +6 %, contrasto +4 %, gradiente tonale, ombra centrale 28 % (blur 26), vignetta, particelle deterministiche, flare attenuato | `banner_scene.html` `#env` |
| Asset finali | loghi ufficiali `08_progetto/assets/loghi/{Sisal_white_neg_LRES.png 2126×678, NetBet_PrimaryLogo_White.png 837×218, WilliamHill_white.png 2172×724}`; font `Montserrat-800.woff2`, `Inter-600.woff2` | rapporti file 3,136 · 3,839 · 3,000 (con padding trasparente); rapporti dell'inchiostro 3,106 · 5,51 · 4,83 |
| Font | Montserrat 800 (titolo, valori, CTA), Inter 600 ("FINO A"); sostitutivi dichiarati (sisal.it non accessibile) | `04_brand_identity/brand_audit.md` |
| Palette (token) | `--sisal-green #00643a`, `--sisal-lime #b9d531`, `--lime-hi #e6ff8a`, `--ground-0 #061a12`, testo `#fff` / `rgba(255,255,255,.74)`, CTA testo `#06301d`, card `rgba(6,26,18,.80)` + bordo `rgba(255,255,255,.13)` | `banner_scene.html :root` |
| Struttura temporale master | S1 0,00–2,60 · T1 · S2 2,95–4,80 · T2 · S3 5,10–6,95 · T3 · S4 7,25–9,10 · T4 · S5 9,45–12,00; CTA in 1,10; morph 2,50–3,05 e 9,05–9,50; pulse 10,70 / 11,45 | `06_storyboard/storyboard_M.md` |
| Audio master | bed stadio reale (clip veo3_1 job `9d228081…`) + SFX procedurali, −20 LUFS, TP ≤ −1 dBTP | `08_progetto/audio/make_audio.py` profilo `master` |
| Regola cliente (2026-09-11) | **"l'audio deve restare sempre"**: ogni adattamento esce con audio; la variante muta è un extra, non il default | messaggio del cliente sulla famiglia verticale |
| Decisioni approvate | 12 s master; sfondo zenitale; niente due punti; ingresso BONUS → SPORT → CTA; CTA media nelle scene operatore; niente indici; nessun accento esclusivo sulla card Sisal in S5; niente effetto vetro; solo pulse sulla CTA finale; famiglia verticale a 10 s approvata | messaggi 2026-09-10/11 |

## Cosa eredita la famiglia orizzontale
- Dal **master**: composizione orizzontale (titolo su una riga, S5 con tre card affiancate su 1920×1080), wipe di luce da sinistra a destra (skew −14°), ordine di lettura sinistra → destra.
- Dalla **famiglia verticale**: timeline 10,0 s (S1 0–2,00 · S2 2,30–3,80 · S3 4,10–5,60 · S4 5,90–7,40 · S5 7,70–10,00), profilo audio `vertical` già validato (−20 LUFS, ultimo evento 9,938 s), pipeline render 2× + Lanczos + encoding + QC, CTA sotto il blocco contenuti nei formati compatti.
