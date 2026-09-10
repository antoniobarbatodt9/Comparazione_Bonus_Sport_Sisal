# FASE 1 — Analisi critica del PDF di ricerca

**Fonte analizzata:** `00_ricerca/Ricerca-visuale-comparazione-tre-offerte.pdf` (35 pagine, "Dossier di ricerca visuale — Tre offerte. Pari dignità visiva", datato 10 settembre 2026).
**Testo integrale estratto:** `02_analisi/pdf_testo_estratto.txt` · **Pagine con immagini rasterizzate:** `02_analisi/pdf_pagine/`.
**Metodo:** lettura integrale delle 35 pagine, verifica visiva delle 10 schede, riclassificazione di ogni informazione in **osservato / dichiarato / dedotto / proposto**.

Legenda usata in tutto il progetto:
- **[OSS]** osservato direttamente (nel PDF, nei file forniti, nei test eseguiti);
- **[DIC]** dichiarato dalla fonte (il dossier o la fonte che il dossier cita), non verificato da me;
- **[DED]** deduzione mia a partire da evidenze;
- **[PRO]** proposta originale mia.

---

## 1. Che cosa dice il dossier (sintesi fedele)

| Tema | Contenuto del dossier | Classificazione |
|---|---|---|
| Conclusione centrale | "La soluzione da sviluppare è una griglia persistente di tre moduli equivalenti" (p.1). | [DIC] |
| Limite dichiarato | "Nessun esempio verificato soddisfa contemporaneamente Italia, tre operatori, comparazione animata e pari dignità visiva" (p.1). | [DIC] |
| Corpus | 22 candidati, 10 schede visuali, 5 reference "da consegnare". 13 candidati su 22 sono **portfolio/preview** (P), solo 3 annunci pubblicati (A), 4 campagne dichiarate dal fornitore (A*), 1 case study, 1 tutorial (p.2, p.4). | [OSS] sul PDF |
| Mercato italiano | Richiamo alle linee guida AGCOM art. 9 (delibera 132/19/CONS): i comparatori sono ammessi se continenti, non ingannevoli e trasparenti; "anche luce, pulse, claim e CTA possono contribuire all'enfasi promozionale" (p.3). | [DIC] |
| Criterio per dire "migliore" | Criterio esplicito, dati omogenei, stesso istante, fonte verificabile; "per offerte e bonus: non confrontare soltanto il valore nominale" (p.3). | [DIC] |
| Pattern da adottare (p.29) | tre card persistenti; rivelazione sincronizzata dei dati; un solo accento moderato; movimento confinato; finale completo e stabile. | [DIC] |
| Pattern da evitare (p.29) | podio sproporzionato; pulse continuo e urgenza; ricchezza/simulazione di vincita; confronti non omogenei; carosello che nasconde i concorrenti. | [DIC] |
| Direzioni proposte (p.30–31) | 01 Tavola dati sportiva (prioritaria); 02 Galleria di giochi (casinò, non pertinente); 03 Comparatore editoriale. | [DIC] |
| Ipotesi di motion | "Una sola sottolineatura o variazione di luminosità in circa 600–900 ms, seguita da fermo. Valori iniziali proposti, non soglie normative" (p.31). | [DIC] |
| Sequenza proposta per 970×250 | 0–1,2 s contesto e identità; 1,2–3 s dati simultanei; 3–4,5 s accento; 4,5–12 s fermo (p.30). | [DIC] |
| Regola multiformato 970×250 | "Tre colonne equivalenti, contesto comune e condizioni in fascia dedicata. Un accento locale; ampio fermo finale" (p.28). | [DIC] |

## 2. Analisi critica delle reference (scheda per scheda)

Le 10 schede sono state guardate nelle pagine rasterizzate. Valutazione mia dell'utilità reale per un 970×250 animato di comparazione bonus:

| # | Reference | Cosa dimostra davvero [OSS] | Limite per noi [DED] | Principio che tengo [PRO] |
|---|---|---|---|---|
| 01 | BMW Finance, selettore modelli (240×480) | Dato e visual aggiornati insieme, coordinate dei campi fisse. Interattivo, un solo brand alla volta. | Formato verticale, interazione hover/drag: fragile in un leaderboard, nessun confronto simultaneo. | **Coordinate fisse dei campi**: logo, "fino a" e valore stanno sempre nello stesso posto in tutte e tre le card. |
| 02 | Greatodds 1/X/2 (statico 410×410) | Tre celle numeriche di pari larghezza e baseline. Atleti e stemmi reali. | È statico; le tre celle sono esiti, non operatori; IP di squadre/giocatori inutilizzabile. | **Tre celle identiche**: stessa larghezza, stessa baseline, stessa dimensione dei numeri. |
| 03 | Merkur XTip (statico 529×529) | Contrasto fascia scura/numeri/accento giallo. Cella centrale più stretta (errore da non ripetere). | Statico, IP di nazionali e competizione. | Solo contrasto fondo scuro + numeri chiari + un accento colore. |
| 04 | Bluestep (HTML5, uno stato) | Rivelazione localizzata su una superficie, il resto fermo. Gesto completo non acquisito. | Nulla di verificato sull'animazione. | **Rivelazione confinata**: il valore si rivela dentro la sua card, non spostando il layout. |
| 05 | Storytel (HTML5) | Movimento in una sola zona, identità ferma, leggibile senza audio. | Un solo contenuto, non un confronto. | Titolo/loghi fermi; muove solo ciò che informa. |
| 06 | Meliá Wonder Week (verticale) | Profondità 2,5D con ombre lunghe; percentuale dominante. | Titolo monumentale non trasferibile in 250 px di altezza; movimento delle ombre non verificato. | Tre superfici uguali possono ricevere **un diverso accento di luce** senza cambiare dimensione. |
| 07 | Casumo Wheel | Palette ridotta, tre livelli di lettura, CTA evidente. | Copy di vincita/invito al gioco: escluso in Italia. | Solo il principio "tre livelli di lettura": titolo, dati, azione. |
| 08 | BMW Serie 5 Hotspot | Punti luce piccoli guidano l'attenzione; su hover appare una lente. | Lente/zoom coprirebbe i concorrenti; hover non esiste in un video. | **Una sola accensione morbida lungo il bordo** della card da valorizzare, senza sovrapposizioni. |
| 09 | Facile.it "Va a pagare" (TV) | Nomina subito la dimensione confrontata; still live action. | Non è una meccanica di card; film non analizzato. | **Nominare il criterio** ("importo massimo dichiarato") invece di un claim. |
| 10 | Tipico Lakers/Orlando (statico) | Identità cromatiche distinte in un contenitore comune; numeri sulla stessa fascia. | Due squadre, incentivo in dollari, IP NBA. | Contenitore comune neutro; i loghi portano la loro identità, il contenitore no. |

Candidati 11–22: nessuno aggiunge meccaniche verificate (quasi tutti ND); 20 (Casino Behance) e 11 (Mozzart) servono solo come **perimetro da evitare** (oro, monete, accumulo decorativo). Il case study Kaizen (+20% CR dichiarato) non isola alcuna causa visiva: **nessuna prova che un "pulse" migliori i risultati** [DIC → non usato come argomento].

## 3. Cosa il dossier NON dà (limiti che condizionano il progetto)

1. **Nessuna reference animata verificata a 970×250 con tre operatori.** Il dossier lo ammette (p.1, p.27). Le catture non hanno timing: durate, easing e pulse citati sono **ipotesi** [DIC]. Quindi i tempi del nostro storyboard sono **proposte originali mie** [PRO], calibrate sulla leggibilità, non "prese dalla ricerca".
2. **Il dossier è pensato per un banner HTML5 in loop lungo** (sequenza 4,5–12 s di fermo, nove size, fallback statico). Il nostro brief è diverso: **video 8–10 s, 25 fps, senza audio, master MP4 + GIF**. La sequenza proposta (p.30) va **compressa nel tempo**: il fermo finale non può durare 7 s.
3. **Nessuna indicazione sul contesto sportivo visivo.** Il dossier parla di "texture sportiva appena percepibile" (p.30) ma non mostra alcun ambiente sportivo generico privo di IP. La scelta dell'ambiente è interamente nostra.
4. **Nessuna indicazione di brand Sisal.** Il dossier è brand-agnostico; l'identità viene solo dagli asset ufficiali (vedi `04_brand_identity/`).
5. **Le immagini del dossier non sono riutilizzabili** (attribuzione a terzi, p.35): sono servite a capire principi, non a copiare.

## 4. Adattabilità al 970×250 (osservazioni misurate)

- Altezza utile reale: 250 px meno la fascia disclaimer. Riservando **40 px** in basso restano **210 px**: bastano per una riga di card da 146 px con margini, non per una gerarchia verticale "monumentale" (Meliá) [DED].
- Tre colonne con larghezza identica sono la sola composizione che regge i tre loghi forniti, che hanno **proporzioni molto diverse** (Sisal 3,1:1, William Hill 4,8:1, NetBet 5,5:1 — misurate sui PNG, vedi `04_brand_identity/brand_audit.md`). Righe orizzontali (300×250) qui non entrano [DED].
- I loghi forniti (SVG e PNG) contengono bianco come colore strutturale (NetBet "Net", William Hill "HILL", Sisal negativo): sono **pensati per fondi scuri** [OSS]. Questo esclude di fatto la direzione 03 "editoriale chiara" senza ricolorare i loghi, cosa vietata dal brief [DED].

## 5. Rischi di leggibilità individuati

| Rischio | Evidenza | Mitigazione [PRO] |
|---|---|---|
| Valori troppo piccoli dopo compressione | GIF a 256 colori + H.264 4:2:0 ammorbidiscono i bordi dei glifi sottili | Valori ≥ 28 px, peso 800, bianco puro su fondo scuro; niente outline, niente ombre colorate. |
| Loghi con pesi ottici diversi | NetBet ha densità d'inchiostro 0,70, William Hill 0,38, Sisal 0,35 (misurato) | Normalizzazione per **area d'inchiostro**, non per larghezza: NetBet 112 px, Sisal 118 px, William Hill 138 px (larghezze scelte per equalizzare la massa visiva, proporzioni intatte). |
| Sfondo fotografico che "rumoreggia" sotto i testi | Bokeh e grana aumentano il bitrate e disturbano i glifi | Ambiente scurito e sfocato sotto le card; card semi-opache; **movimento dell'ambiente lentissimo e deterministico** (nessun video generativo sotto i testi). |
| "Migliore" implicito | Il dossier avverte: valore nominale ≠ offerta migliore | Nessun claim; solo etichetta di criterio "Importo massimo dichiarato"; l'ordine delle card è dichiaratamente per valore decrescente del criterio. |
| Pulse continuo | Pattern da evitare (p.29) | Un solo passaggio di luce (850 ms) + bordo statico; un solo riflesso sulla CTA; poi tutto fermo. |

## 6. Trend e tecniche osservati, e come li uso

- **Card di vetro / superfici semitrasparenti su ambiente scuro** (Meliá, Merkur, Tipico) → adottate, ma con opacità calibrata per la GIF (niente gradienti ampi in movimento dentro le card).
- **Numeri come protagonisti** (Greatodds, BMW) → adottato: il valore è l'elemento più grande dopo il titolo, identico per i tre.
- **Rivelazione localizzata** (Bluestep) → adottata per i valori (maschera che sale dentro la card, simultanea per i tre).
- **Luce come accento** (BMW Hotspot, Meliá) → adottata come unico accento su Sisal: bordo lime + passaggio di luce.
- **Selettori, hover, caroselli, lenti** → esclusi: nascondono concorrenti o non esistono in un video.

## 7. Decisione sulla direzione del dossier

Il dossier raccomanda "01 Tavola dati sportiva". La **adotto nella struttura** (tre colonne equivalenti, dati simultanei, un accento, finale stabile) perché è l'unica coerente con brief, loghi forniti e mercato italiano. La **modifico** in tre punti, motivati:

1. **Contesto sportivo esplicito e non "appena percepibile"**: a 970×250 una texture impercettibile non comunica "sport"; uso un ambiente generico da stadio/campo notturno, generato (senza IP), scurito sotto i dati. Motivo: il brief richiede che il contesto sportivo sia chiaro.
2. **Tempi compressi in 9 s** (invece di 12 s con lungo fermo): apertura 0–0,9 s, card 0,9–1,8 s, dati 2,15–2,75 s, accento 4,0–5,1 s, fermo 5,1–9,0 s. Motivo: durata obbligatoria 8–10 s.
3. **CTA presente dal fotogramma 0** (il dossier la colloca nel "finale completo"): il brief la vuole visibile in tutta la durata utile.

Le alternative valutate e la raccomandazione sono in `05_concept/concept.md`.
