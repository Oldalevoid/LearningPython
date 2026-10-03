# DESCRIZIONE
# Separa il catalogo delle unità disponibili dall'esercito realmente posseduto.
# Il giocatore sceglie un'unità dalla caserma, il programma controlla il costo
# e, se l'oro è sufficiente, aggiunge l'unità all'esercito e scala il prezzo.
#
# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Separare una lista-catalogo dalla lista delle unità possedute
# - Passare più liste diverse alla stessa funzione con ruoli distinti
# - Selezionare un'unità dal catalogo tramite indice validato
# - Aggiungere l'unità scelta a un esercito separato con append()
# - Aggiornare l'oro dopo un reclutamento riuscito

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
            scelta = int(input("Quale unità vuoi reclutare? "))

            if scelta < 1 or scelta > len(caserma):
                print("Inserisci un valore valido")
                continue

            indice = scelta - 1
            break

        except ValueError:
            print("Inserisci un numero")
            continue

    if oro >= caserma[indice]["Costo"]:
        oro -= caserma[indice]["Costo"]
        print(f"Hai reclutato {caserma[indice]['Tipo']}")
        esercito.append(caserma[indice])
    else:
        print("Fondi non sufficienti")

    return oro


oro = recluta(unitadisponibili, esercitoAmandola, oro)

print(f"Oro rimasto: {oro}")
print(esercitoAmandola)
