# DESCRIZIONE
# Aggiunge una funzione che calcola il valore totale dell'esercito sommando
# il costo di tutte le unità possedute.
#
# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Usare una variabile accumulatore inizializzata a 0
# - Scorrere una lista di dizionari con un ciclo for
# - Sommare progressivamente un valore numerico con +=
# - Restituire un totale calcolato con return
# - Separare il calcolo di una statistica dell'esercito in una funzione dedicata

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


oro = recluta(unitadisponibili, esercitoAmandola, oro)

print(f"Oro rimasto: {oro}")
mostraesercito(esercitoAmandola)

valoreamandola = calcolavaloreesercito(esercitoAmandola)
print(f"Valore totale dell'esercito: {valoreamandola}")
