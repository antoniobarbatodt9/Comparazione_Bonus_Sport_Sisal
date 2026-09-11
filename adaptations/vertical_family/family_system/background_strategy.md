# Strategia dello sfondo verticale

## Principio
Lo sfondo delle verticali è **lo stesso asset Higgsfield approvato** per il master (still campo di calcio zenitale, job `e190625a-b390-47f4-ba30-cc464acb0373`, 3168×1344): non è stato generato nulla di nuovo. Il master usa la fascia centrale 3168×927 (formato 21:9 ➜ 970×250); le verticali usano la **fascia centrale verticale 896×1344** dello stesso still (cerchio di centrocampo + linea di metà campo verticale), ridimensionata a `08_progetto/assets/env/env_M_pitch_topdown_VERT_800x1200.jpg` (md5 `d73f25578e8675d9c66088b4e88d4f3b`, JPEG q76 4:2:0, 106 KB; trasferito via sandbox in 9 chunk, hash verificato).

È una **ri-inquadratura**, non una deformazione: stesso pixel-aspect, stesso soggetto, stessa luce; l'immagine viene posizionata in `cover` con un bordo di 40 px per la deriva di camera. Nessuna duplicazione o specchiatura, nessun outpainting.

## Continuità con il master
| Livello | Master | Verticali | Note |
|---|---|---|---|
| Immagine | fascia centrale orizzontale | fascia centrale verticale dello stesso still | il cerchio di centrocampo resta l'ancora visiva in entrambi |
| Tinta verde Sisal | `mix-blend-mode:color` 70 % + `screen` 12 % | identico | stessi token |
| Luminosità/contrasto | +6 % / +4 % | identico | |
| Ombra centrale (leggibilità card) | 650×170 a blur 26, 28 % | 252×380 · 280×300 · 136×400 a blur 26, 28 % | copre l'area delle card |
| Raggi / flare | 0,35 / 0,6 (attenuati) | flare 0,6 in alto a sinistra, con decadimento a 0,38 dopo 1,4 s | raggi omessi nelle verticali (secondari, dichiarato) |
| Vignetta + gradiente tonale | sì | sì, con la parte bassa che scurisce verso la fascia (dissolvenza di 22 px entro l'area utile) | la fascia disclaimer resta piatta `#061a12` |
| Particelle | 22 | 14 / 12 / 8 | proporzionali all'area |
| Fascia disclaimer | 970×40 piatta | 300×60 · 320×50 · 160×56 piatte | nessun elemento, nessuna luce |

## Copertura dell'area verticale
- 300×600 e 160×600: il ritaglio 896×1344 (2:3) copre 300×600 (1:2) e 160×600 (~1:3,75) con scala ≥ 1 rispetto al ritaglio a 800×1200: la linea di metà campo passa vicino all'asse, il cerchio sta nella metà alta/centrale dietro il blocco titolo o le card.
- 320×480 (2:3): rapporto identico al ritaglio, nessun taglio aggiuntivo.
- Render di produzione a 2× (dopo approvazione): l'area necessaria è 680×1360 per 300×600 (600×1200 + bordo 80), 720×1040 per 320×480, 400×1360 per 160×600. La fascia verticale 896×1344 dello still originale copre tutte e tre (scala di cover ≤ 1,02): basta ritrasferire lo stesso ritaglio a 896×1344 q84 (≈ 200 KB), senza upscale né nuova generazione. Decisione formale in `production_plan/production_plan.md`.

## Ciò che NON si fa
Nessuna nuova generazione, nessuna variazione di soggetto (niente porte, spalti, tribune, palloni, giocatori), nessun elemento IP, nessuno stretch, nessuna duplicazione visibile del cerchio.
