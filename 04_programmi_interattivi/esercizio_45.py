# DESCRIZIONE
# Aggiunge una funzione dedicata alla visualizzazione dell'esercito posseduto.
# Se l'esercito è vuoto viene mostrato un messaggio specifico; altrimenti
# vengono stampate tutte le unità con numero, tipo, vita e potere.
#
# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Verificare se una lista è vuota usando len()
# - Gestire due casi alternativi con if / else
# - Usare enumerate(..., start=1) per numerare le unità possedute
# - Visualizzare in modo leggibile dati contenuti in una lista di dizionari
# - Separare la presentazione dello stato dell'esercito in una funzione dedicata

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


def mostracatalogo(caserma):
    for numero, unita in enumerate(caserma, start=1):
        print(numero, "-", unita["Tipo"], "- Costo:", unita["Costo"])


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


oro = recluta(unitadisponibili, esercitoAmandola, oro)

print(f"Oro rimasto: {oro}")
mostraesercito(esercitoAmandola)
