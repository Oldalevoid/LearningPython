# DESCRIZIONE
# Aggiunge una funzione che calcola la vita totale dell'esercito sommando
# la Vita di tutte le unità possedute.
#
# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Riutilizzare il pattern dell'accumulatore su una proprietà diversa
# - Scorrere una lista di dizionari e sommare una chiave numerica
# - Restituire con return una statistica aggregata dell'esercito
# - Consolidare la separazione tra calcolo e visualizzazione del risultato

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


def calcolavitatotaleesercito(esercito):
    lifepoints = 0

    for unita in esercito:
        lifepoints += unita["Vita"]

    return lifepoints


oro = recluta(unitadisponibili, esercitoAmandola, oro)

print(f"Oro rimasto: {oro}")
mostraesercito(esercitoAmandola)

valoreamandola = calcolavaloreesercito(esercitoAmandola)
vitaamandola = calcolavitatotaleesercito(esercitoAmandola)

print(f"Valore totale dell'esercito: {valoreamandola}")
print(f"Vita totale dell'esercito: {vitaamandola}")
