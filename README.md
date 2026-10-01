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

## Punto attuale del percorso

**Ultimo esercizio completato: esercizio_22.py**

Percorso attuale:

```text
01_fondamenti/
  esercizio_01.py - esercizio_05.py

02_logica_e_funzioni/
  esercizio_06.py - esercizio_09.py

03_strutture_dati/
  esercizio_10.py - esercizio_17.py

04_programmi_interattivi/
  esercizio_18.py - esercizio_22.py
```

Il prossimo esercizio da proporre è quindi **esercizio_23.py**, salvo diversa richiesta esplicita.

## Livello attuale

Livello: **principiante, ma ormai capace di combinare autonomamente diversi costrutti fondamentali di Python**.

Non sto più lavorando solo su singole istruzioni isolate: riesco a costruire piccoli programmi testuali interattivi usando insieme strutture dati, cicli, condizioni, funzioni e gestione basilare degli errori.

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
- validazione di un input numerico sia per tipo sia per intervallo.

## Ultime competenze consolidate

Negli esercizi più recenti sono stati costruiti:

- menu testuali persistenti;
- funzioni per creare nuove unità;
- input numerici robusti che non fanno terminare il programma in caso di errore;
- selezione numerata di unità tramite `enumerate()`;
- controlli che impediscono di accedere a indici inesistenti.

L'esercizio 22 mostra un esercito numerato, chiede all'utente quale unità selezionare e continua a richiedere l'input finché non viene inserito un numero valido e compreso tra le opzioni disponibili.

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
