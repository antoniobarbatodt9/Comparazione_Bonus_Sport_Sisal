# Pre-flight audit · 4 — Mappa: invariabili · ricomponibili · critici

## Elementi invariabili (coerenza visiva e funzionale con il master)
| Elemento | Vincolo |
|---|---|
| Copy (titolo, "FINO A", importi, €, CTA) | identico, stesso casing |
| Loghi ufficiali | stessi PNG, proporzioni intatte, solo width, rapporto ottico 1 : 0,949 : 1,169 |
| Palette e token | stessi HEX/alpha; card 80 %, bordo 13 %; lime per CTA e "SPORT"/regolo |
| Font | Montserrat 800 / Inter 600 (sostitutivi dichiarati) |
| Sfondo | stesso asset Higgsfield e stessi livelli di trattamento (tinta, tono, ombra, vignetta, particelle) |
| Struttura narrativa | S1 titolo+CTA → Sisal → NetBet → William Hill (clip identiche) → comparazione → pulse CTA |
| Linguaggio motion | rivelazione da maschera con tracking, ingresso card con salita+rotateX+blur, cifre una alla volta allineate alla fine, wipe di luce, CTA unica con morph e pulse |
| CTA | unica, sempre presente dal suo ingresso, pill lime, mai nella safe area |
| Safe area | fascia inferiore continua, piatta, vuota per tutta l'animazione |

## Elementi ricomponibili (posizione, scala, disposizione, percorso)
| Elemento | Libertà |
|---|---|
| Titolo | da una riga (S1) a due righe impilate e centrate; corpo 30–46 px |
| Card | da affiancate a impilate; dimensioni e padding ricalcolati per size; struttura interna invariata |
| Hero card | centrata nel formato, CTA sotto anziché a destra |
| CTA | tre taglie/posizioni per size, morph verticale |
| Wipe | direzione verticale (alto→basso) nelle size strette |
| Camera dell'ambiente | scala/spostamento per scena ricalibrati sul riframe verticale |
| Particelle | numero ridotto proporzionalmente all'area (22 → 14 / 12 / 8) |
| Raggi/flare | riposizionati in alto (fuori dai testi) |

## Elementi critici (rischio di leggibilità/equilibrio per size)
| Elemento | 300×600 | 320×480 | 160×600 |
|---|---|---|---|
| "FINO A" nelle card | 11 px ok | 10 px, da verificare | **9,5 px**: minimo assoluto, verificato a size reale |
| Logo William Hill in card | 117 px ok | 103 px ok | **100 px** in card 136 (padding 18): verificato |
| Importo "5.200€" in card | 24 px ok | 22 px ok | **21 px** (larghezza ≈ 80 px in 136) |
| CTA | 200×48 | 180×44 | **136×40, testo 11,5 px**: verificato |
| Densità verticale | ok (60 px di safe) | **5 blocchi in 430 px utili**: spaziature 10–18 px | ok (safe 56) |
| Wipe | orizzontale possibile | verticale | verticale |
| Regolo lime | 120 px | 100 px | 60 px |
