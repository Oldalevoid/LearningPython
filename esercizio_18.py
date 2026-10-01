# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Creare un menu interattivo che resta attivo con while True
# - Usare input() per scegliere tra più opzioni
# - Gestire le diverse scelte con if, elif
# - Uscire da un ciclo infinito usando break
# - Usare for ... else per gestire una ricerca:
#   l'else viene eseguito se il ciclo termina senza incontrare break

EsercitoAmandola = [
    {
        "Tipo": "Arcere della Sibilla",
        "Danno": 25,
        "Vita": 80
    },
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


while True:
    print("1 - Mostra Esercito, 2 - Cerca Unità, 3 - Quit")
    scelta = input("Benvenuto a Dungeon Sibilla, cosa vuoi fare? ")

    if scelta == "1":
        print(EsercitoAmandola)

    elif scelta == "2":
        ricerca = input("Digita l'unità da cercare ")
        
        for unita in EsercitoAmandola:
            if ricerca == unita["Tipo"]:
                print("Trovato!")
                break
        else:
            print("L'unità non esiste")

    elif scelta == "3":
        print("CiaoCiao")
        break
