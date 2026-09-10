# Concept — direzioni creative, valutazione e raccomandazione

> Stato: **proposta per approvazione**. Il layer brand (palette UI, font, raggi) è provvisorio (vedi `04_brand_identity/brand_audit.md`); struttura, comparazione, timing e pipeline sono definitivi salvo vostre osservazioni.

## 0. Vincoli che hanno guidato ogni scelta

1. **Pari dignità**: tre card identiche (168×146 px), stessi campi nello stesso posto, stessa dimensione dei valori (29 px/800), stesso ingresso, stessa rivelazione. Nessuna card più grande, nessun valore più grande, nessun competitor sfocato/scolorito/rimpicciolito.
2. **Nessun "migliore in assoluto"**: niente claim, niente podio, niente medaglie. Solo un'etichetta di criterio ("Importo massimo dichiarato") e un ordine motivato (decrescente per il criterio confrontato, che coincide con il cliente in prima posizione).
3. **Loghi ufficiali com'è** su fondo scuro (i tre file forniti usano il bianco come colore strutturale).
4. **CTA "SCOPRI DI PIÙ" dal fotogramma 0 all'ultimo**, mai sovrapposta a dati, loghi o safe area.
5. **Safe area disclaimer 970×40 px in basso (y 210–250)**, piatta, scura, senza movimento, sempre libera.
6. **Contesto sportivo chiaro ma generico**, senza IP (niente atleti, squadre, stemmi, sponsor, stadi riconoscibili, palloni marchiati).
7. **Compressione considerata dal disegno**: grandi aree stabili, movimento confinato, ambiente scurito sotto i testi.
8. **Higgsfield MCP** usato per ciò che sa fare meglio in questo contesto (ambiente fotografico generico), mai per testi/loghi/importi.

## 1. Quante alternative servono

Ho ridotto a **due direzioni realmente valide** più **una scartata con evidenza**. Non ha senso presentarne di più: struttura e gerarchia sono di fatto obbligate dal brief e dalle reference (griglia a tre colonne); la libertà creativa reale sta in (a) l'ambiente sportivo, (b) il linguaggio delle superfici, (c) il tipo di accento su Sisal, (d) il ritmo.

| | A · "Campo di luce" (raccomandata) | B · "Tabellone di luce" | C · "Editoriale chiaro" (scartata) |
|---|---|---|---|
| Styleframe | `styleframe/A_campo_di_luce_01_t9.00s.png` (finale) · `…_02_t4.45s.png` (momento dell'accento) | `styleframe/B_tabellone_di_luce_01_t9.00s.png` | `styleframe/C_editoriale_chiaro_SCARTATA_01_t9.00s.png` |
| Ambiente | Campo notturno generico da riflettori, sfocato, banda superiore scura (Higgsfield, still) + deriva lenta programmata | Arena astratta: raggi di luce da destra, fondo quasi nero (Higgsfield, still) | Fondo chiaro neutro, nessun ambiente |
| Superfici | Card "vetro" scure semitrasparenti, bordo 1 px al 16%, raggio 12 px | Nessuna card: tre colonne separate da linee sottili, come un tabellone | Card bianche con ombra leggera |
| Accento Sisal | Un passaggio di luce lungo il bordo (850 ms) → bordo lime 1,5 px persistente + alone lime tenue dietro la card | Sottolineatura lime 2 px sotto il valore Sisal | Bordo lime |
| Sport | Esplicito (erba, linea di campo, riflettori) | Allusivo (luce da stadio) | Assente |
| Coerenza Sisal | Verde/lime dal logo come luce d'ambiente, titolo, CTA | Lime solo su titolo/CTA/accento | Verde su chiaro |
| Loghi ufficiali | Perfetti (bianco su scuro) | Perfetti | **Sisal negativo e "Net"/"HILL" bianchi invisibili** → richiederebbe ricolorare i loghi: vietato |

## 2. Direzione A — "Campo di luce" (RACCOMANDATA)

**Idea.** La comparazione avviene *sul campo*: tre card equivalenti appoggiate a un campo notturno generico illuminato dai riflettori. Il verde dell'erba è anche il verde di Sisal: l'identità del cliente diventa l'**ambiente** in cui tutti e tre gli operatori sono mostrati alla pari, non un trattamento speciale della sua card. La memorabilità di Sisal emerge da tre scelte misurate e cumulative: (1) posizione di lettura primaria (prima card a sinistra, ordine motivato dal criterio); (2) un solo accento di luce, che è l'unico evento dell'ultima metà del banner; (3) la CTA lime che riprende esattamente il lime del logo Sisal, creando un legame cromatico card Sisal ↔ azione senza toccare i competitor.

**Razionale.**
- Rispetta tutti i pattern del dossier (tre card persistenti, rivelazione sincronizzata, un solo accento, movimento confinato, finale stabile) e i "da evitare".
- Il contesto sportivo è inequivocabile anche a 250 px di altezza grazie a erba, linea curva e bokeh dei riflettori: non serve nessun oggetto (pallone, atleta), quindi zero rischio IP.
- L'ambiente è **un'immagine still**: niente artefatti temporali dell'AI video, niente flicker. Il movimento è programmato (deriva 10 px/9 s + scala 1,035→1,0) e quindi fluido, deterministico, ripetibile.
- La struttura a tre colonne funziona come base per le altre size (non richieste ora), ricomponendo il layout e non scalando.

**Punti di forza.** Leggibilità (contrasto ≥ 8,9:1 su ogni testo), sport esplicito, identità Sisal "ambientale" e non discriminatoria, compressibilità (test: MP4 324 KB a CRF 14, vedi `11_qc/strategia_compressione.md`), un solo asset generativo da produrre.

**Criticità e mitigazioni.**
- *Bokeh sotto le card*: possono disturbare i loghi → in produzione l'ambiente viene scurito del 25% nella fascia delle card e i punti luce più intensi verranno tenuti fuori dall'area 232–776 px in fase di selezione/outpaint.
- *GIF*: la deriva continua dell'ambiente fa pesare la GIF (5,1 MB a 12,5 fps/256 colori). Mitigazione già testata: nella versione GIF l'ambiente resta fermo (`bgmode=still`), il resto dell'animazione è identico → vedi misure in `11_qc/`.
- *Alone lime dietro Sisal*: potrebbe essere letto come "card più luminosa". È mantenuto tenue (opacità max 0,9 di un gradiente al 35%) e non altera dimensione né contrasto dei competitor; se lo ritenete eccessivo, si spegne con un parametro (è un layer separato).

## 3. Direzione B — "Tabellone di luce"

**Idea.** Un tabellone luminoso di stadio, astratto: fondo quasi nero, tre colonne separate da sottili linee, raggi di luce di riflettori da destra. I valori si rivelano come su un tabellone; l'accento su Sisal è una sottolineatura lime sotto il valore.

**Punti di forza.** Massima nitidezza dei testi (fondo quasi uniforme), GIF leggerissima, look "dati" molto pulito, meno dipendenza dall'asset generativo.

**Criticità.** Lo sport è solo alluso (nessun campo): a 970×250 può leggersi come un generico "dark UI"; i raggi di luce attraversano l'area dei valori (rischio di leggibilità in compressione, visibile nello styleframe dietro "1.000€"); l'estetica "tabellone" rischia di ricordare grafiche televisive, cosa da evitare per il brief; l'identità Sisal è meno presente (solo lime).

**Perché non la raccomando.** Comunica meno sport e meno Sisal della A a parità di correttezza comparativa. Resta una valida "variante sobria" se il cliente preferisce un fondo più neutro.

## 4. Direzione C — "Editoriale chiaro" (SCARTATA con evidenza)

È la direzione 03 del dossier. Lo styleframe dimostra il problema: **i loghi ufficiali forniti sono bianchi** (Sisal negativo, "Net" di NetBet, "HILL" di William Hill) e su fondo chiaro spariscono. L'unico modo di realizzarla sarebbe ricolorare o ricostruire i loghi, esplicitamente vietato dal brief. Inoltre non comunica sport. Scartata.

## 5. Raccomandazione

**Direzione A "Campo di luce"**, durata **9,0 s (225 fotogrammi a 25 fps)**, ambiente still generato con Higgsfield, compositing HTML/CSS deterministico renderizzato fotogramma per fotogramma con Chromium headless, encoding ffmpeg. Storyboard completo in `06_storyboard/storyboard.md`.

### Perché 9,0 s e non 8 o 10
- Lettura: 3 loghi + 3 valori + titolo + criterio + CTA ≈ 12 parole/numeri → ~4 s di lettura comoda. Con dati stabili da 2,75 s e accento chiuso a 5,1 s restano **3,9 s di fermo completo**: sufficienti, e il fermo è il momento più "compresso" (quasi zero bit).
- 8,0 s costringerebbe l'accento a 3,5 s e il fermo a 2,9 s: leggibile ma affrettato. 10,0 s aggiunge solo fermo; utile se il cliente vuole più tempo di lettura in fase di loop. La timeline è parametrica: cambiare la durata è un valore (`TL.duration`) e un re-render.

### Che cosa resta statico e che cosa si anima
| Elemento | Comportamento |
|---|---|
| Safe area disclaimer (0,210 → 970×40) | **Statica, vuota, piatta** per tutti i 225 fotogrammi |
| CTA "SCOPRI DI PIÙ" (800,83 → 150×44) | **Presente e leggibile dal fotogramma 0**; un solo riflesso diagonale a 6,6–7,2 s; posizione fissa |
| Titolo "BONUS" / "SPORT" + criterio | Entrano 0,2–1,1 s (salita 14 px + dissolvenza), poi **fermi** |
| Tre card (232,32 → 3×168×146, gap 20) | Entrano insieme 0,9–1,6 s (salita 22 px), poi **ferme**; nessun riordino |
| Loghi (box 130×40 in ogni card) | Dissolvenza simultanea 1,25–1,75 s, poi **fermi**; mai scalati o deformati |
| "FINO A" + valori | Etichetta 2,0–2,35 s; valori con rivelazione mascherata dal basso 2,15–2,75 s, **identica per i tre**, poi fermi |
| Accento Sisal | Passaggio di luce sul bordo 4,0–4,85 s; bordo lime 4,6–5,1 s; alone 4,5–5,3 s; poi **fermo** |
| Ambiente | Dissolvenza 0–0,6 s; deriva lentissima e continua (10 px e scala 1,035→1,0 in 9 s), **spenta nella GIF** |

### Loop
Il file è pensato per **riproduzione singola con fermo finale** (l'ultimo fotogramma è un end-frame completo e stabile, usabile come fallback statico). Se il canale esige loop, la ripartenza dal fotogramma 0 (ambiente nero → dissolvenza) è morbida per costruzione; non è prevista una transizione di loop dedicata, per non alterare la durata.
