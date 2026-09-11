# Pre-flight audit · 4 — Mappa: invariabili · ricomponibili · critici (famiglia orizzontale)

## Invariabili
| Elemento | Vincolo |
|---|---|
| Copy, casing, importi | identici al master |
| Loghi | stessi PNG ufficiali, solo `width` (height auto): rapporto box = rapporto file (3,136 · 3,839 · 3,000, verificato); pesi ottici 1 : 0,95 : 1,17 |
| Token colore, card 80 %, bordo 13 %, lime per CTA / "SPORT" / regolo | identici |
| Font | Montserrat 800 / Inter 600 (sostitutivi dichiarati) |
| Sfondo | stesso still Higgsfield, stesso trattamento; ri-inquadratura 16:9 senza deformazione |
| Narrazione | S1 → Sisal → NetBet → William Hill (clip identiche) → confronto → pulse |
| Motion | rivelazione da maschera con tracking, card con salita + rotateX + blur, cifre roll-up, wipe di luce, CTA unica con morph e pulse, nessun anello |
| Audio | sempre presente (regola cliente); traccia del master ri-temporizzata (profilo `vertical` a 10 s) |
| Safe area | fascia inferiore continua, piatta, vuota su tutti i fotogrammi |

## Ricomponibili
| Elemento | Libertà usata |
|---|---|
| Titolo S1 | una riga, corpo 168 / 32 / 36 px |
| Hero card | centrata, CTA sotto (master: a destra) |
| S5 | card affiancate (1920) oppure righe logo-sinistra / dati-destra (rettangoli) |
| CTA | tre taglie per size, morph verticale lungo l'asse |
| Wipe | orizzontale come il master, larghezza banda per size (280 / 120 / 130) |
| Camera, particelle, flare, ombra centrale | ricalibrati per area (particelle 40 / 8 / 8) |

## Critici (verificati a 100 %, vedi `checkpoints/check_report.md`)
| Elemento | 1920×1080 | 300×250 | 336×280 |
|---|---|---|---|
| "FINO A" | 36 / 30 px | 10 / 10 px (limite) | 11 / 10 px |
| Logo William Hill in S5 | 350 px | **72 px** in riga 38 px | 80 px |
| Importo "5.200€" S5 | 84 px (324 px largh.) | **16 px in colonna 62** (61,1 px) | 17 px in colonna 68 (66,1) |
| CTA | 560×120 / 520×110 | 160×38 / 160×36 / **160×32, testo 12** | 180×42 / 180×40 / 180×36 |
| Gap CTA ↔ righe S5 durante l'ingresso | 32 px | **6,8 px** | 8,8 px |
| Peso del titolo S1 nel quadro | 168 px (8,75 % H) | 32 px | 36 px |
