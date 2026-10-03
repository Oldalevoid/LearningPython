# RTS — Percorso di apprendimento Python

Sto imparando Python da zero attraverso un percorso di esercizi progressivi a tema RTS/game development.

Questo repository non è un progetto finito: è un **diario didattico progressivo**. Ogni esercizio introduce pochi concetti nuovi e riutilizza quelli già acquisiti. L'obiettivo è arrivare gradualmente da semplici programmi testuali a un piccolo RTS 2D, senza saltare le basi di Python.

## Istruzioni per l'AI che legge questa repository

Se stai usando questa repository per propormi nuovi esercizi:

- considera che sto imparando Python da zero e che il percorso deve restare graduale;
- prima di proporre un nuovo esercizio, osserva gli ultimi esercizi completati e non ripetere inutilmente concetti già acquisiti;
- introduci **pochi concetti nuovi alla volta**;
- lascia che sia io a scrivere la soluzione: spiega prima la nuova sintassi necessaria e poi assegna l'esercizio;
- quando sbaglio, indicami l'errore e aiutami a ragionare senza fornire subito l'intera soluzione, salvo mia richiesta;
- mantieni, quando possibile, il tema RTS/fantasy già usato negli esercizi;
- continua la numerazione progressiva degli esercizi;
- per ogni nuovo file completato aggiungi in testa:
  1. una breve sezione `DESCRIZIONE` che spiega cosa fa il programma;
  2. una sezione `COSA HO IMPARATO IN QUESTO ESERCIZIO` che elenca **solo i concetti nuovi o consolidati in quell'esercizio**, non un riepilogo cumulativo;
- gli esercizi completati vanno inseriti nella cartella didattica più adatta.

### Regola di sincronizzazione a ogni push

Ogni volta che viene completato e pushato un nuovo esercizio, l'AI deve **aggiornare anche questo README nello stesso momento**, mantenendolo sincronizzato con lo stato reale della repository. In particolare deve:

- aggiornare il numero e il percorso dell'**ultimo esercizio completato**;
- indicare quale deve essere il **prossimo esercizio da proporre**;
- aggiornare l'elenco dei **concetti già affrontati** con le nuove competenze introdotte o consolidate;
- aggiornare la sezione **Ultime competenze consolidate** descrivendo ciò che è stato appena acquisito;
- aggiornare il **livello attuale** solo quando il progresso complessivo lo giustifica;
- aggiornare la struttura delle cartelle se viene creata una nuova fase didattica.

Questa operazione fa parte del push dell'esercizio: non deve essere lasciata a un aggiornamento manuale successivo.

## Punto attuale del percorso

**Ultimo esercizio completato: esercizio_47.py**

Percorso attuale:

```text
01_fondamenti/
  esercizio_01.py - esercizio_05.py

02_logica_e_funzioni/
  esercizio_06.py - esercizio_09.py

03_strutture_dati/
  esercizio_10.py - esercizio_17.py

04_programmi_interattivi/
  esercizio_18.py - esercizio_47.py
```

Il prossimo esercizio da proporre è quindi **esercizio_48.py**, salvo diversa richiesta esplicita.

## Livello attuale

Livello: **principiante avanzato / intermedio iniziale in Python**.

Non sto più lavorando solo su singole istruzioni isolate: riesco a costruire piccoli programmi testuali interattivi usando insieme strutture dati, cicli, condizioni, funzioni, gestione basilare degli errori e una prima organizzazione modulare del codice in funzioni con responsabilità distinte.

### Concetti già affrontati

- variabili;
- stringhe e numeri;
- `print()`;
- f-string;
- `input()`;
- conversione con `int()`;
- operatori aritmetici;
- condizioni `if`, `elif`, `else`;
- operatori di confronto;
- operatore logico `and`;
- cicli `while`;
- `while True`;
- `break`;
- `continue`;
- modulo `random` e `random.randint()`;
- funzioni con `def`;
- parametri;
- `return`;
- liste;
- indicizzazione delle liste;
- modifica degli elementi;
- `for`;
- dizionari;
- liste di dizionari;
- accesso annidato lista/dizionario;
- `.append()`;
- `.pop()`;
- `len()`;
- ricerca di elementi;
- valori booleani `True` e `False`;
- `for ... else`;
- `try` / `except ValueError`;
- `None` e `is not None`;
- `enumerate()`;
- `enumerate(..., start=1)`;
- relazione tra numero mostrato all'utente e indice reale di una lista;
- validazione di un input numerico sia per tipo sia per intervallo;
- passaggio di una lista come argomento a una funzione;
- uso di una struttura dati tramite un parametro di funzione;
- restituzione di un dizionario con `return`;
- salvataggio e utilizzo del dizionario restituito da una funzione;
- modifica diretta di un dizionario ricevuto come parametro;
- aggiornamento dello stato di un'unità senza usare `return`;
- controllo di una soglia minima per impedire valori negativi;
- distinzione tra unità viva e unità morta tramite `if / else`;
- interazione tra due dizionari tramite una funzione;
- uso di `-=` per aggiornare un valore numerico;
- applicazione del `Danno` di un'unità alla `Vita` di un'altra;
- costruzione di una prima semplice meccanica di combattimento;
- gestione di due eserciti distinti;
- riuso della stessa funzione di selezione su liste diverse;
- combinazione tra selezione dell'attaccante, selezione del bersaglio e attacco;
- rimozione diretta di un elemento da una lista con `.remove()`;
- distinzione concettuale tra `.remove(elemento)` e `.pop(indice)`;
- aggiornamento della composizione di un esercito durante il combattimento;
- ciclo di battaglia con `while`;
- controllo simultaneo dello stato di due eserciti;
- prevenzione dell'accesso a una lista vuota durante il combattimento;
- conclusione della battaglia quando un esercito resta senza unità;
- selezione casuale di un elemento da una lista con `random.choice()`;
- scelta casuale di attaccante e bersaglio durante una battaglia;
- salvataggio delle scelte casuali in variabili;
- uso di un contatore dei turni;
- stampa leggibile di chi attacca chi;
- nuova selezione dell'attaccante dopo una possibile eliminazione;
- generazione di un tiro casuale con `random.randint()` per determinare un evento di combattimento;
- implementazione di un colpo critico con probabilità del 30%;
- uso di una variabile temporanea per applicare un danno maggiorato senza alterare permanentemente il danno base;
- uso di `return` per interrompere anticipatamente una funzione;
- implementazione di una probabilità di schivata del 20%;
- ordinamento logico degli eventi casuali: prima schivata, poi eventuale critico;
- aggiunta della statistica `Armatura` alle unità;
- separazione tra calcolo del danno e applicazione del danno;
- calcolo del danno effettivo come danno meno armatura;
- imposizione di un danno minimo pari a 1;
- separazione della logica in funzioni con responsabilità distinte;
- restituzione del danno calcolato tramite `return`;
- uso di `return 0` per rappresentare un attacco schivato;
- controllo del valore restituito prima di modificare lo stato del bersaglio;
- spostamento di un intero scambio di attacchi in una funzione dedicata;
- uso dei parametri della funzione al posto di variabili globali quando possibile;
- semplificazione del ciclo principale tramite astrazione;
- incapsulamento dell'intero ciclo di battaglia in una funzione dedicata;
- gestione del contatore dei turni come stato locale della funzione `battaglia()`;
- riduzione del programma principale a una singola chiamata ad alto livello;
- restituzione di una stringa da una funzione con `return`;
- separazione tra determinazione del risultato e presentazione del risultato;
- salvataggio del valore restituito da `battaglia()` in una variabile;
- uso del valore restituito per scegliere il messaggio finale;
- introduzione della risorsa `oro`;
- aggiunta della chiave `Costo` alle unità;
- reclutamento condizionato dalla disponibilità di risorse;
- aggiornamento dell'oro tramite valore restituito da una funzione;
- uso di `>=` per consentire l'acquisto quando oro e costo coincidono;
- importanza di restituire un valore in tutti i percorsi della funzione per evitare `None` inattesi;
- uso combinato di `enumerate()`, `try/except`, `while True`, `continue` e `break` per validare una scelta di menu;
- trasformazione della scelta mostrata all'utente nell'indice reale della lista con `scelta - 1`;
- distinzione operativa tra `continue`, `break` e `return`;
- separazione tra catalogo delle unità disponibili ed esercito posseduto;
- passaggio di due liste con ruoli distinti alla stessa funzione;
- aggiunta dell'unità scelta dal catalogo a una lista esercito separata;
- differenza tra aggiungere un riferimento a un dizionario e aggiungerne una copia;
- uso di `.copy()` per creare unità indipendenti a partire dal catalogo;
- uso di un valore sentinella (`0`) per terminare una fase interattiva;
- controllo del valore sentinella prima della conversione della scelta in indice;
- gestione di più reclutamenti consecutivi nello stesso ciclo;
- estrazione della validazione dell'input in una funzione riutilizzabile;
- uso di parametri `minimo` e `massimo` per generalizzare i controlli;
- eliminazione di `try/except` duplicati dalla logica principale;
- separazione della visualizzazione del catalogo in una funzione dedicata;
- richiamo di una funzione da un'altra funzione per ridurre responsabilità e duplicazioni;
- visualizzazione strutturata dell'esercito tramite una funzione dedicata;
- controllo esplicito del caso lista vuota con `len()`;
- uso di un accumulatore per sommare una statistica dell'esercito;
- funzione `calcolavaloreesercito()` che restituisce la somma dei costi delle unità;
- funzione `calcolavitatotaleesercito()` che somma la Vita di tutte le unità;
- riuso consapevole del pattern dell'accumulatore su proprietà diverse.

## Ultime competenze consolidate

Negli esercizi più recenti sono stati costruiti:

- menu testuali persistenti;
- funzioni per creare nuove unità;
- input numerici robusti che non fanno terminare il programma in caso di errore;
- selezione numerata di unità tramite `enumerate()`;
- controlli che impediscono di accedere a indici inesistenti;
- funzioni riutilizzabili che ricevono un esercito come parametro;
- restituzione e successivo utilizzo del dizionario dell'unità selezionata;
- funzioni che modificano direttamente lo stato di un'unità;
- gestione della vita minima a zero e riconoscimento della morte dell'unità;
- interazione tra due unità tramite una funzione di attacco;
- selezione di attaccante e bersaglio da due eserciti distinti;
- rimozione delle unità morte dalla lista dell'esercito;
- ciclo completo di battaglia tra due eserciti;
- battaglia con attaccanti e bersagli scelti casualmente tramite `random.choice()`;
- log testuale dei combattimenti con numero del turno e nomi di attaccante e bersaglio;
- riselezione sicura delle unità prima del contrattacco;
- colpi critici casuali che raddoppiano il danno solo per il singolo attacco;
- schivate casuali che interrompono subito l'attacco tramite `return`;
- armatura che riduce il danno ricevuto;
- calcolo del danno effettivo prima di modificare la vita del bersaglio;
- funzione dedicata `calcoladanno()` separata da `attacca()`;
- funzione `combattimento()` che gestisce un intero scambio di attacchi;
- funzione `battaglia()` che gestisce l'intera battaglia e restituisce il vincitore;
- gestione del messaggio finale fuori dalla funzione di battaglia;
- funzione `recluta()` che aggiunge unità all'esercito e aggiorna l'oro;
- controllo delle risorse prima del reclutamento;
- menu numerato di reclutamento con input robusto;
- selezione di un'unità tramite indice validato;
- separazione tra caserma/catalogo ed esercito realmente posseduto;
- creazione di copie indipendenti delle unità reclutate tramite `.copy()`;
- fase di reclutamento ripetuta con `while True` e uscita tramite valore sentinella `0`;
- funzione `chiediscelta()` dedicata alla validazione robusta di input numerici;
- funzione `mostracatalogo()` dedicata alla visualizzazione delle unità disponibili;
- funzione `mostraesercito()` dedicata alla visualizzazione delle unità possedute;
- funzione `calcolavaloreesercito()` dedicata al calcolo del valore complessivo dell'esercito;
- funzione `calcolavitatotaleesercito()` dedicata al calcolo della Vita complessiva.

L'esercizio 47 consolida il pattern dell'accumulatore con la funzione `calcolavitatotaleesercito(esercito)`, che somma la Vita di tutte le unità. Lo studente ha riutilizzato autonomamente la stessa struttura logica già usata per il costo totale, mostrando di aver compreso il pattern e non soltanto il singolo esercizio.

Il prossimo passo deve introdurre una funzione di sintesi che combini più statistiche dell'esercito in un'unica presentazione, riutilizzando funzioni già scritte invece di ripetere i calcoli.

## Direzione del percorso

Il percorso deve continuare ancora con Python di base/intermedio prima di passare alla grafica. I prossimi esercizi dovrebbero gradualmente portare verso programmi più strutturati e verso un piccolo RTS testuale.

Argomenti da introdurre progressivamente possono includere, senza necessariamente seguire rigidamente questo ordine:

- semplificazione e riuso della validazione dell'input;
- funzioni che lavorano direttamente sulle unità;
- combattimenti tra unità memorizzate in liste/dizionari;
- gestione di due eserciti;
- selezione di attaccante e bersaglio;
- rimozione delle unità morte;
- risorse e costi di reclutamento;
- menu più articolati;
- organizzazione del codice in più funzioni;
- tuple e altri costrutti Python utili;
- introduzione graduale alle classi e agli oggetti;
- piccoli progetti testuali che combinino le competenze acquisite.

Solo dopo aver consolidato queste basi, il percorso potrà passare a **Pygame** e ai concetti necessari per un RTS 2D: game loop, coordinate x/y, sprite, input del mouse, selezione e movimento delle unità, combattimento, edifici, risorse, camera, pathfinding e IA semplice.

## Obiettivo

Arrivare a padroneggiare Python attraverso la pratica e, successivamente, usare le competenze acquisite per sviluppare un piccolo RTS 2D.
