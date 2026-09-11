# Sistema tipografico della famiglia verticale

Font invariati dal master: **Montserrat 800** (titolo, valori, CTA) e **Inter 600** (etichetta "FINO A"), sostitutivi dichiarati in `04_brand_identity/brand_audit.md` (sisal.it non raggiungibile). Nessun testo aggiunto: il set è "BONUS", "SPORT", "FINO A", "5.200€", "1.000€", "255€", "SCOPRI DI PIÙ".

## Scala (px) — master → size

| Ruolo | Master 970×250 | 300×600 | 320×480 | 160×600 | Tracking | Note |
|---|---|---|---|---|---|---|
| Titolo S1 | 56 / lh 66 (una riga) | 46 / 50, due righe | 40 / 44, due righe | 30 / 34, due righe | 0,14 → −0,01 em (animato, come master) | impilato "BONUS" / "SPORT": rapporto 0,82 / 0,71 / 0,54 del master |
| Valore hero | 38 / 46 | 34 / 40 | 32 / 38 | 26 / 32 | −0,01 em, cifre tabulari | sempre su una riga; "5.200€" larghezza 132 / 121 / 98,5 px |
| FINO A hero | 13 | 13 | 12 | 10,5 | 0,16 em, maiuscolo, bianco 74 % | mai sotto 10 px |
| Titolo S5 | 37 / 46 due righe | 26 / 30 una riga "BONUS SPORT" | 24 / 28 una riga | 20 / 22 due righe | 0,10 → −0,01 em | in S5 il titolo è secondario (dati già noti) |
| Valore card S5 | 29 / 38 | 24 / 30 | 22 / 26 | 21 / 26 | −0,01 em | "5.200€" 93,6 / 82,7 / 81,8 px |
| FINO A card | 11 | 11 | 10 | 10 | 0,14 em | minimo assoluto 10 px |
| CTA S1 | 20 | 18 | 17 | 12 | 0,05 em, maiuscolo | |
| CTA operatore | 18 | 17 | 16 | 12 | | |
| CTA confronto | 13,5 | 17 | 16 | 12 | | nelle verticali la CTA finale non si rimpicciolisce sotto la CTA operatore: c'è spazio e la gerarchia resta corretta |

## Regole
- **Gerarchia invariata**: valore > logo > CTA > titolo (S5) > FINO A. In S1: titolo > CTA.
- **Rapporto etichetta/valore** costante ≈ 0,38–0,40 (master 13/38 = 0,34; card 11/29 = 0,38).
- **Distanza etichetta→valore** = lh(FINO A) + 2…4 px; identica nelle tre card di S5 (stessa struttura, stesso padding).
- **€** sempre attaccato alla cifra, stesso corpo, stesso peso (nessun apice, nessuna riduzione).
- **Baseline**: valori e FINO A allineati a griglia di 2 px; i tre valori in S5 condividono `top` relativo alla card, quindi baseline coincidenti tra card.
- **A capo**: unico cambio consentito dal brief — "BONUS" / "SPORT" su due righe in S1 (come già nel master S5) e su 160×600 anche in S5; "SCOPRI DI PIÙ" resta sempre su una riga (`white-space:nowrap`, verificata: 300 → 220 px box, 160 → 136 px box con testo 12 px ≈ 104 px).
- **Colore**: "BONUS" bianco, "SPORT" lime `#b9d531` (come master); valori bianco; FINO A bianco 74 %; CTA testo `#06301d` su lime.
- **Contrasto** (WCAG, verificato in check 2): bianco su fondo card ≈ 12:1; lime su verde ≈ 6,5:1; testo CTA su lime ≈ 9,6:1.
