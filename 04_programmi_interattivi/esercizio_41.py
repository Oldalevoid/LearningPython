# DESCRIZIONE
# Introduce la copia indipendente delle unità reclutate.
# Quando il giocatore sceglie un'unità dal catalogo, viene aggiunta all'esercito
# una copia del dizionario originale, così ogni unità posseduta può avere uno
# stato indipendente dalle altre.
#
# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Capire che append(dizionario) aggiunge un riferimento allo stesso oggetto
# - Capire perché due riferimenti allo stesso dizionario condividono le modifiche
# - Usare .copy() per creare una copia indipendente di un dizionario semplice
# - Aggiungere all'esercito una copia dell'unità scelta dal catalogo
# - Preparare il sistema di reclutamento a gestire più unità dello stesso tipo

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
        esercito.append(caserma[indice].copy())
    else:
        print("Fondi non sufficienti")

    return oro


oro = recluta(unitadisponibili, esercitoAmandola, oro)

print(f"Oro rimasto: {oro}")
print(esercitoAmandola)
