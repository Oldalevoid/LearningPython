# DESCRIZIONE
# Gestisce due piccoli eserciti e permette all'utente di scegliere
# un attaccante e un bersaglio. L'attacco modifica direttamente
# la Vita del bersaglio usando il Danno dell'attaccante.
#
# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Gestire due liste di dizionari distinte
# - Riutilizzare una funzione di selezione su eserciti diversi
# - Validare una scelta numerica rispetto alla lunghezza della lista
# - Combinare selezione e combattimento in un unico programma
# - Far interagire più funzioni sullo stesso insieme di dati

EsercitoAmandola = [
    {
        "Tipo": "Guerriero della Sibilla",
        "Danno": 35,
        "Vita": 100
    },
    {
        "Tipo": "Mago Piceno",
        "Danno": 60,
        "Vita": 50
    }
]

EsercitoNemico = [
    {
        "Tipo": "Orco delle Gole",
        "Danno": 40,
        "Vita": 120
    },
    {
        "Tipo": "Goblin della Marca",
        "Danno": 20,
        "Vita": 60
    }
]


def seleziona_unita(esercito):
    for numero, unita in enumerate(esercito, start=1):
        print(numero, "-", unita["Tipo"])

    while True:
        try:
            unitaselezionata = int(input("Seleziona unità "))

            if unitaselezionata >= 1 and unitaselezionata <= len(esercito):
                indice = unitaselezionata - 1
                break
            else:
                print("Seleziona un numero nel menù!")
        except ValueError:
            print("Inserisci un valore numerico")
            continue

    return esercito[indice]


def attacca(attaccante, bersaglio):
    print(f"{attaccante['Tipo']} sferra un colpo a {bersaglio['Tipo']}")
    bersaglio["Vita"] -= attaccante["Danno"]

    if bersaglio["Vita"] > 0:
        print(f"{bersaglio['Vita']} punti vita rimangono a {bersaglio['Tipo']}")
    else:
        bersaglio["Vita"] = 0
        print(f"{bersaglio['Tipo']} è morto")


print("Scegli il tuo attaccante")
attaccante = seleziona_unita(EsercitoAmandola)

print("Scegli il bersaglio")
bersaglio = seleziona_unita(EsercitoNemico)

attacca(attaccante, bersaglio)
