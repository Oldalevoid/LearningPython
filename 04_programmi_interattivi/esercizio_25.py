# DESCRIZIONE
# Simula un attacco tra due unità rappresentate come dizionari.
# L'attaccante riduce la Vita del bersaglio usando il proprio valore di Danno.
# Se la Vita del bersaglio scende a zero o meno, viene riportata a zero
# e l'unità viene considerata morta.
#
# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Far interagire due dizionari tramite una funzione
# - Usare il valore Danno dell'attaccante per modificare la Vita del bersaglio
# - Usare l'operatore -= per aggiornare un valore numerico
# - Gestire il caso in cui il bersaglio sopravvive o muore
# - Combinare più competenze già apprese in una semplice meccanica di combattimento

Guerriero = {
    "Tipo": "Guerriero della Sibilla",
    "Danno": 35,
    "Vita": 100
}

Mago = {
    "Tipo": "Mago Piceno",
    "Danno": 60,
    "Vita": 50
}


def attacca(attaccante, bersaglio):
    print(f"{attaccante['Tipo']} sferra un colpo a {bersaglio['Tipo']}")
    bersaglio["Vita"] -= attaccante["Danno"]

    if bersaglio["Vita"] > 0:
        print(f"{bersaglio['Tipo']} tentenna e ha {bersaglio['Vita']} punti vita")
    else:
        bersaglio["Vita"] = 0
        print(f"{bersaglio['Tipo']} è morto")


attacca(Guerriero, Mago)
attacca(Guerriero, Mago)
