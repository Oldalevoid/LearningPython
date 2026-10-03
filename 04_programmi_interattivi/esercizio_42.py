# DESCRIZIONE
# Trasforma il reclutamento singolo in una vera fase di reclutamento ripetuta.
# Il giocatore può acquistare più unità in successione e terminare inserendo 0.
# L'oro viene aggiornato dopo ogni acquisto riuscito.
#
# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Usare un valore sentinella per terminare un ciclo interattivo
# - Ripetere una fase di gioco completa con while True
# - Controllare il valore sentinella prima di usare la scelta come indice
# - Evitare che 0 diventi indice -1 in Python
# - Aggiornare progressivamente una risorsa durante più operazioni consecutive

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


def recluta(caserma, esercito, oro):
    for numero, unita in enumerate(caserma, start=1):
        print(numero, "-", unita["Tipo"], "- Costo:", unita["Costo"])

    while True:
        try:
            print("0 - Termina il reclutamento")
            scelta = int(input("Quale unità vuoi reclutare? "))

            if scelta < 0 or scelta > len(caserma):
                print("Inserisci un valore valido")
                continue

            if scelta == 0:
                break

            indice = scelta - 1

            if oro >= caserma[indice]["Costo"]:
                oro -= caserma[indice]["Costo"]
                print(f"Hai reclutato {caserma[indice]['Tipo']}")
                esercito.append(caserma[indice].copy())
            else:
                print("Fondi non sufficienti")

        except ValueError:
            print("Inserisci un numero")
            continue

    return oro


oro = recluta(unitadisponibili, esercitoAmandola, oro)

print(f"Oro rimasto: {oro}")
print(esercitoAmandola)
