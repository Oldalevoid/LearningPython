# DESCRIZIONE
# Separa la visualizzazione del catalogo dalla logica di reclutamento.
# La funzione mostracatalogo() si occupa esclusivamente di stampare le unità
# disponibili, mentre recluta() gestisce la scelta, il controllo dell'oro
# e l'aggiunta delle unità all'esercito.
#
# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Separare responsabilità diverse in funzioni dedicate
# - Creare una funzione mostracatalogo() riutilizzabile
# - Richiamare una funzione da un'altra funzione
# - Rendere recluta() più leggibile e modulare
# - Eliminare rami else inutili dopo un break

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
print(esercitoAmandola)
