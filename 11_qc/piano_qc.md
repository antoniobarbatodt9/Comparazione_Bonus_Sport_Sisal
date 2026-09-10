# Piano di controllo qualità

Ogni voce ha un metodo di verifica concreto. Le verifiche automatiche saranno script in `11_qc/` eseguiti sul master e sulle esportazioni; le voci visive vengono fatte alla dimensione reale (1×) e a 2×.

## A. Correttezza dei contenuti (bloccante)
| Verifica | Metodo |
|---|---|
| Testi esatti: "BONUS SPORT", "SCOPRI DI PIÙ", "FINO A 5.200€", "FINO A 1.000€", "FINO A 255€" | diff tra `config.json` e DOM del template; ispezione end frame |
| Nessun arrotondamento/riformattazione degli importi (punto delle migliaia, simbolo € dopo il numero, senza spazio) | come sopra |
| Loghi = file ufficiali, non ricostruiti; rapporto larghezza/altezza invariato | confronto `naturalWidth/naturalHeight` vs `width/height` renderizzati (script Playwright) |
| Nessun testo/logo/€/CTA dentro l'asset ambiente | ispezione dell'immagine Higgsfield prima dell'uso |
| Nessun elemento IP nell'ambiente (atleti, squadre, stemmi, sponsor, stadi riconoscibili, marchi) | ispezione + prompt negativo; scarto dell'asset in caso di dubbio |
| Nessun claim di superiorità assoluta; solo etichetta di criterio | lettura copy |

## B. Pari dignità (bloccante)
| Verifica | Metodo |
|---|---|
| Tre card di dimensione identica (168×146) | misura DOM |
| Valori a font-size identica (29 px) e baseline identica | misura DOM + overlay di allineamento |
| Stessi tempi di ingresso/rivelazione per le tre card (Δt = 0) | lettura timeline `TL` + confronto fotogrammi f38/f55/f68 |
| Nessun competitor sfocato, scolorito, ridotto | confronto istogrammi di luminanza dei tre box logo (tolleranza ±10%) sull'end frame |
| Ordine stabile per tutta la durata | verifica posizioni f0…f224 |

## C. Leggibilità e qualità visiva
| Verifica | Metodo |
|---|---|
| Contrasto testo/fondo ≥ 4,5:1 su ogni testo (target ≥ 7:1) | campionamento colori medi dietro i testi (script) |
| Nitidezza glifi dopo compressione: valori leggibili nell'MP4 web e nella GIF a 1× | ispezione end frame decodificato dai file esportati (non dai PNG) |
| Assenza di flicker/formicolio: differenza media tra fotogrammi consecutivi nella fase di fermo (5,3–9,0 s) sotto soglia | script: mean abs diff per frame < 0,5/255 nelle zone statiche |
| Assenza di banding nei gradienti dell'ambiente | ispezione a 2× + eventuale dither sottile nell'asset |
| Fluidità: easing continui, nessun salto > 6 px/frame negli ingressi | derivata delle posizioni dalla timeline |
| Stabilità loghi: nessun sub-pixel shimmer (posizioni intere a fine animazione) | verifica `transform` finale = identità |
| Colore controllato: primari lime/verde entro la palette; nessuna dominante nella conversione yuv420p | confronto colori CTA/lime tra PNG e frame decodificato (ΔE < 3) |

## D. CTA e safe area (bloccante)
| Verifica | Metodo |
|---|---|
| CTA visibile e integra in **ogni** fotogramma (opacità 1, nessuna sovrapposizione) | script: crop 800,83,150,44 su tutti i frame, verifica presenza pixel lime e testo |
| Safe area 0,210 → 970×40 identica al colore piatto in **ogni** fotogramma | script: deviazione standard dei pixel nella zona = 0 su tutti i 225 frame |

## E. Specifiche tecniche
| Verifica | Metodo |
|---|---|
| 970×250, 25 fps, 225 frame, durata 9,00 s, nessuna traccia audio | `ffprobe` |
| MP4 H.264 High, yuv420p, faststart | `ffprobe` |
| Distribuzione ≤ 3,5 MB reali (3.500.000 byte; verificato anche contro 3,5 MiB) | `stat` |
| GIF ≤ 3,5 MB, 970×250, loop flag secondo richiesta | `stat` + `ffprobe` |
| Master e web riproducibili in Chrome, Safari, VLC | test player (dove disponibile) |

## F. Coerenza con brief
Checklist finale spuntata voce per voce sul brief (elementi obbligatori, divieti, safe area, durata, frame rate, audio, pesi) in `11_qc/report_qc.md`.
