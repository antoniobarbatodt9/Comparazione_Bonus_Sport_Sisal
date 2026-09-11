# Pre-flight audit · 1 — Inventario del master approvato

## Identificazione univoca del master (fonte unica creativa)

| Voce | Valore | Evidenza |
|---|---|---|
| Master approvato | **Concept M "Montaggio a scene", revisione 2** — 970×250, 25 fps, 12,0 s (300 fotogrammi), con audio | commit `429e807` (2026-09-10), ultima versione consegnata dopo le tre note del cliente (niente effetto vetro, audio stadio reale, solo pulse sulla CTA); nessuna ulteriore richiesta di modifica |
| Esportazioni master | `10_export/BonusSport_970x250_25fps_12s_M_{MASTER.mp4, MASTER_444_archivio.mov, WEB.mp4, WEB_MUTO.mp4, CONTROL.gif, ENDFRAME_fallback_statico.png}` | pesi/specifiche in `11_qc/report_qc_M.md` |
| Progetto sorgente | `08_progetto/banner_scene.html` (template deterministico, parametro `t`) + `render_scene.mjs` + `make_master_M.sh` + `config_M.json` | il DOM contiene testi, loghi, valori, CTA; l'ambiente è un layer separato |
| Sfondo approvato | still Higgsfield **campo di calcio zenitale**, job `e190625a-b390-47f4-ba30-cc464acb0373` (nano_banana_2, 3168×1344); nel master: fascia centrale 3168×927 (y=208) → `08_progetto/assets/env/env_M_pitch_topdown_FINAL_2036x596.jpg` (md5 `ea1d842587991411dbbb9bc7673308fa`) | `07_asset_generati/README_higgsfield.md` §7 |
| Trattamento sfondo | tinta verde Sisal (`mix-blend-mode:color` 70 % + screen 12 %), luminosità +6 %, contrasto +4 %, gradiente tonale alto/basso, ombra centrale 28 % (blur 26), vignetta; particelle deterministiche (22); raggi 0,35 e flare 0,6 (attenuati in rev. 2) | `banner_scene.html` righe `#env` |
| Storyboard approvato | `06_storyboard/storyboard_M.md` (v2 + §0-bis revisione 2) e `storyboard_M_contact_sheet.png`; `05_concept/concept_M.md` | — |
| Asset finali | loghi ufficiali `08_progetto/assets/loghi/{Sisal_white_neg_LRES.png, NetBet_PrimaryLogo_White.png, WilliamHill_white.png}`; font `assets/font/Montserrat-800.woff2`, `Inter-600.woff2`; sfondo sopra | rapporti larghezza/altezza dei loghi: Sisal 3,106 · NetBet 5,51 · William Hill 4,83 |
| Font | Montserrat 800 (titolo, valori, CTA), Inter 600 (etichetta "FINO A"); **sostitutivi** dichiarati (sito sisal.it non accessibile) | `04_brand_identity/brand_audit.md` |
| Palette (design token) | `--sisal-green #00643a`, `--sisal-lime #b9d531`, `--lime-hi #e6ff8a`, `--ground-0 #061a12`, testo `#fff`, testo attenuato `rgba(255,255,255,.74)`, CTA testo `#06301d`, card `rgba(6,26,18,.80)` + bordo `rgba(255,255,255,.13)` | `banner_scene.html :root` |
| Durata / fps | 12,0 s · 25 fps · 300 fotogrammi (f0…f299) | `config_M.json` |
| Audio | bed stadio reale (clip veo3_1 job `9d228081…`) + SFX procedurali; **non pertinente per le verticali (audio: nessuno, da brief)** | `08_progetto/audio/` |
| Decisioni approvate nelle iterazioni | 12 s; sfondo zenitale #21; niente due punti; ingresso BONUS → SPORT → CTA; etichetta piccola rimossa; CTA media nelle scene operatore; niente indici "n/3"; nessun accento sulla card Sisal in S5; niente effetto vetro; card solide; solo pulse sulla CTA finale | messaggi del cliente 2026-09-10 |
| Report QC | `11_qc/report_qc_M.md` (tutti i controlli automatici superati, revisione 2) | — |

Versioni **non** usate: concept A (pannello unico, 9 s, `banner.html`), storyboard v1, ambiente in prospettiva `env_A_pitch_FINAL`, varianti Higgsfield scartate (#22, #23, #24), audio sintetico rev. 1.

## Inventario completo degli elementi (per scena, px, origine in alto a sinistra)

| # | Elemento | Scena | Box (x, y, w, h) | Tipografia / asset | Colore |
|---|---|---|---|---|---|
| E1 | Sfondo campo zenitale + livelli (tinta, tono, ombra, vignetta) | tutte | 0,0 970×250 (immagine 1050×330 a −40,−40, camera per scena) | JPEG 2036×596 | — |
| E2 | Particelle (22 punti 3 px) | tutte | y < 205 | — | bianco, opacità ≤ 0,55 |
| E3 | Wipe di luce (transizioni T1–T4) | T | banda 140×330, skew −14°, da x −120 a +1010 | — | bianco-lime |
| E4 | Titolo S1 "BONUS" | S1 | 142, 72, 212×66 | Montserrat 800 56 px, tracking 0,14→−0,01 em | bianco |
| E5 | Titolo S1 "SPORT" | S1 | 372, 72, 197×66 | idem | lime |
| E6 | Regolo S1 | S1 | 142, 150, 427×2 | — | lime 0,9 |
| E7 | CTA grande | S1 | 599, 79, 230×52, raggio 999 | Montserrat 800 20 px, tracking 0,05 em, maiuscolo | lime / testo #06301d |
| E8 | Hero card | S2–S4 | 195, 30, 300×158, raggio 14 | fondo card 80 %, bordo 13 %, ombra 0 12 34 30 % | — |
| E9 | Logo nella hero | S2–S4 | box 195,52 300×56; larghezze Sisal 172 · NetBet 164 · William Hill 202 | PNG ufficiali, height auto | bianco |
| E10 | "FINO A" hero | S2–S4 | 195,116 300×16 | Inter 600 13 px, tracking 0,16 em | bianco 74 % |
| E11 | Valore hero | S2–S4 | 195,134 300×46 | Montserrat 800 38 px, tabulari, tracking −0,01 em | bianco |
| E12 | CTA media | S2–S4 | 565, 80, 210×54 | Montserrat 800 18 px | lime |
| E13 | Titolo S5 "BONUS"/"SPORT" (due righe) | S5 | 26, 60, 196×92 | Montserrat 800 37 px | bianco / lime |
| E14 | Regolo S5 | S5 | 26, 148, 44×2 | — | lime |
| E15 | Card ×3 | S5 | 232 / 420 / 608, 32, 168×146, raggio 12 | come E8 | — |
| E16 | Logo nelle card | S5 | box +0,+22 168×40; larghezze 118 · 112 · 138 | PNG ufficiali | bianco |
| E17 | "FINO A" card | S5 | +0,+76 168×13 | Inter 600 11 px, tracking 0,14 em | bianco 74 % |
| E18 | Valore card | S5 | +0,+94 168×38 | Montserrat 800 29 px | bianco |
| E19 | CTA piccola | S5/S6 | 800, 83, 150×44 | Montserrat 800 13,5 px | lime |
| E20 | Safe area disclaimer | tutte | 0, 210, 970×40 | piatta `#061a12`, vuota | — |

## Struttura dei livelli (z-order dal basso)
1. `#env` (proc → img → tint → tint2 → rays → flare → tone → shade → vignette) · 2. `#particles` · 3. scene `#s1…#s5` (mascherate da `clip-path` durante i wipe) · 4. `#wipe` (banda di luce, z 6) · 5. `#cta` (unica, z 5, mai mascherata) · 6. `#safe` (fascia disclaimer, sempre sopra tutto).

## Timeline del master (s)
S1 0,00–2,60 · T1 2,60–2,95 · S2 Sisal 2,95–4,80 · T2 4,80–5,10 · S3 NetBet 5,10–6,95 · T3 6,95–7,25 · S4 William Hill 7,25–9,10 · T4 9,10–9,45 · S5 9,45–12,00 (pulse CTA 10,70–11,25 e 11,45–12,00). CTA: ingresso 1,10–1,55; morph grande→media 2,50–3,05; morph media→piccola 9,05–9,50. Clip operatore (relativo): hero 0–0,50 · logo 0,30–0,70 · FINO A 0,60–0,85 · cifre complete 1,15 · fermo fino a 1,85.
