# DESCRIZIONE
# Mostra un elenco numerato di unità disponibili e permette al giocatore di
# sceglierne una da reclutare. L'input viene validato sia come tipo sia come
# intervallo, così il programma continua a chiedere finché la scelta non è valida.
#
# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Usare enumerate(..., start=1) per mostrare un menu numerato
# - Convertire la scelta dell'utente nell'indice reale della lista con scelta - 1
# - Gestire input non numerici con try / except ValueError
# - Usare while True e continue per ripetere la richiesta
# - Usare break per uscire dal ciclo quando l'input è valido
# - Distinguere tra continue, break e return
# - Controllare che una scelta numerica rientri nell'intervallo valido

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

oro = 1000


def recluta(esercito, oro):
    for numero, unita in enumerate(esercito, start=1):
        print(numero, "-", unita["Tipo"], "- Costo:", unita["Costo"])

    while True:
        try:
            scelta = int(input("Quale unità vuoi reclutare? "))

            if scelta < 1 or scelta > len(esercito):
                print("Inserisci un valore valido")
                continue

            indice = scelta - 1
            break

        except ValueError:
            print("Inserisci un numero")
            continue

    if oro >= esercito[indice]["Costo"]:
        oro -= esercito[indice]["Costo"]
        print(f"Hai reclutato {esercito[indice]['Tipo']}")
    else:
        print("Fondi non sufficienti")

    return oro


oro = recluta(unitadisponibili, oro)

print(f"Oro rimasto: {oro}")
