# Strategia dello sfondo orizzontale

## Principio
Stesso still Higgsfield del master (job `e190625a-b390-47f4-ba30-cc464acb0373`, 3168×1344): **nessuna nuova generazione**. Per il 16:9 si usa la fascia centrale 2389×1344 dello still (x 389–2778, altezza piena: cerchio di centrocampo e linea di metà campo al centro), ridimensionata a **1920×1080** (JPEG q80 4:2:0, 220.538 byte, md5 `77490f8c1684faae58ca8dd9bf11fbae`) → `08_progetto/assets/env/env_M_pitch_topdown_169_1920x1080.jpg`. Trasferita dal sandbox Higgsfield in 19 chunk base64 da 16.000 caratteri (una chiamata per chunk), hash verificato. 0 crediti.

È una ri-inquadratura (stesso pixel-aspect, stesso soggetto, stessa luce), posizionata in `cover` con bordo 60 px (1920) / 40 px (rettangoli) per la deriva di camera. Nessun outpainting, nessuna specchiatura.

## Copertura
| Size | Rapporto | Uso del file 1920×1080 | Scala di cover |
|---|---|---|---|
| 1920×1080 | 16:9 | intero + bordo 60 px | 1,06 (1×) · 2,12 (2×, vedi sotto) |
| 300×250 | 1,2:1 | ritaglio centrale ≈ 1300×1080 → 380×330 | < 1 |
| 336×280 | 1,2:1 | idem | < 1 |

## Continuità con il master
| Livello | Master | Orizzontali |
|---|---|---|
| Immagine | fascia centrale 21:9 | fascia centrale 16:9 dello stesso still (contiene per intero l'inquadratura del master) |
| Tinta / tono / vignetta | `color` 70 % + `screen` 12 %, +6 % / +4 % | identici |
| Ombra centrale | 650×170 blur 26, 28 % | 1560×640 · 268×190 · 300×210, blur 26, 28 % |
| Flare | 0,6 → 0,38 | 1600×1100 · 300×220 · 330×240 in alto a sinistra, stesso decadimento |
| Particelle | 22 (3 px) | 40 (5 px) · 8 · 8 |
| Fascia disclaimer | 970×40 piatta | 1920×108 · 300×30 · 336×34 piatte, dissolvenza di raccordo dentro l'area utile |

## Render 2× del 1920×1080 (produzione)
Il render a deviceScaleFactor 2 richiede 3840×2160 di copertura: il file 1920×1080 verrebbe ingrandito 2× (morbido). Opzioni, in ordine di preferenza:
1. **trasferire il ritaglio 2389×1344 alla risoluzione nativa** (stesso still, q84, ≈ 600 KB, ≈ 50 chunk) e lasciare che il template lo copra a scala 1,61 a 2×: nessun costo in crediti, nitidezza pari al master (che a 2× usa lo still a scala ≈ 1,0);
2. render 1920×1080 a **1× diretto** (nessun downsample): il 16:9 è già alla risoluzione di consegna; testi e loghi sono vettoriali/PNG ad alta risoluzione e restano nitidi; l'anti-aliasing 2× del master si perde solo sui bordi curvi;
3. `upscale_image` dello still (crediti) — solo se il check a 100 % dei frame lo richiedesse; non previsto.
Per 300×250 e 336×280 il file attuale basta anche a 2× (scala < 1).

## Ciò che NON si fa
Nessuna nuova generazione, nessuna variazione di soggetto (porte, spalti, palloni, giocatori), nessuno stretch, nessun elemento IP.
