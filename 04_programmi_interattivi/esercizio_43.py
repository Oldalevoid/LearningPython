# DESCRIZIONE
# Estrae la validazione di una scelta numerica in una funzione riutilizzabile.
# La funzione chiediscelta() gestisce input non numerici e valori fuori intervallo,
# mentre recluta() si concentra solo sulla logica di reclutamento.
#
# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Separare la validazione dell'input dalla logica principale
# - Creare una funzione riutilizzabile con parametri minimo e massimo
# - Usare return per restituire una scelta valida
# - Eliminare try/except duplicati quando la gestione degli errori è già delegata
# - Controllare il valore sentinella prima di convertire la scelta in indice

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


def recluta(caserma, esercito, oro):
    for numero, unita in enumerate(caserma, start=1):
        print(numero, "-", unita["Tipo"], "- Costo:", unita["Costo"])

    while True:
        print("0 - per terminare il reclutamento")
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
print(esercitoAmandola)
