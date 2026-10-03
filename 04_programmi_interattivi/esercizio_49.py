# DESCRIZIONE
# Introduce un menu principale che collega in un unico flusso interattivo
# le funzioni già costruite per mostrare l'esercito, reclutare unità,
# visualizzare il riepilogo e controllare l'oro.
#
# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Costruire un menu principale persistente con while True
# - Usare una funzione di menu per coordinare più funzioni già esistenti
# - Aggiornare una variabile di stato tramite il valore restituito da una funzione
# - Restituire lo stato aggiornato dal menu principale con return
# - Collegare più funzionalità in un unico flusso interattivo
# - Distinguere tra catalogo delle unità disponibili ed esercito posseduto

unitadisponibili = [
    {
        "Tipo": "Giuseppe The Butcher 'Chiappacelli",
        "Vita": 1000,
        "Costo": 400,
        "Potere": "Divinità"
    },
    {
        "Tipo": "Gisella The Golden Gremlin",
        "Vita": 800,
        "Costo": 150,
        "Potere": "Divinità"
    }
]

esercitoAmandola = []

oro = 1000


def mostramenu(oro):
    while True:
        print("1 - Mostra esercito")
        print("2 - Recluta unità")
        print("3 - Riepilogo esercito")
        print("4 - Mostra oro")
        print("0 - Esci")

        scelta = chiediscelta("Scegli un'opzione: ", 0, 4)

        if scelta == 0:
            break

        elif scelta == 1:
            mostraesercito(esercitoAmandola)

        elif scelta == 2:
            oro = recluta(unitadisponibili, esercitoAmandola, oro)

        elif scelta == 3:
            riepilogaesercito(esercitoAmandola)

        elif scelta == 4:
            print(f"Oro rimasto: {oro}")

    return oro


def chiediscelta(messaggio, minimo, massimo):
    while True:
        try:
            scelta = int(input(messaggio))

            if scelta < minimo or scelta > massimo:
                print("Inserisci un valore valido")
                continue

            return scelta

        except ValueError:
            print("Inserisci un intero")


def mostraesercito(esercito):
    if len(esercito) == 0:
        print("L'esercito è vuoto")
    else:
        for numero, unita in enumerate(esercito, start=1):
            print(
                numero,
                "-",
                unita["Tipo"],
                "- Vita:",
                unita["Vita"],
                "- Potere:",
                unita["Potere"]
            )


def mostracatalogo(caserma):
    for numero, unita in enumerate(caserma, start=1):
        print(numero, "-", unita["Tipo"], "- Costo:", unita["Costo"])


def recluta(caserma, esercito, oro):
    mostracatalogo(caserma)

    while True:
        print("0 - Termina il reclutamento")
        scelta = chiediscelta(
            "Quale unità vuoi reclutare? ",
            0,
            len(caserma)
        )

        if scelta == 0:
            break

        indice = scelta - 1

        if oro >= caserma[indice]["Costo"]:
            oro -= caserma[indice]["Costo"]
            print(f"Hai reclutato {caserma[indice]['Tipo']}")
            esercito.append(caserma[indice].copy())
        else:
            print("Fondi non sufficienti")

    return oro


def calcolavaloreesercito(esercito):
    valore = 0

    for unita in esercito:
        valore += unita["Costo"]

    return valore


def calcolavitatotaleesercito(esercito):
    lifepoints = 0

    for unita in esercito:
        lifepoints += unita["Vita"]

    return lifepoints


def riepilogaesercito(esercito):
    unitatotali = len(esercito)
    valoretotale = calcolavaloreesercito(esercito)
    vitatotale = calcolavitatotaleesercito(esercito)

    print(f"Unità totali: {unitatotali}")
    print(f"Valore totale: {valoretotale}")
    print(f"Vita totale: {vitatotale}")


oro = mostramenu(oro)
