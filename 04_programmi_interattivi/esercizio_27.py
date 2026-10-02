# DESCRIZIONE
# Simula un attacco tra due unità e rimuove il bersaglio dal suo esercito
# quando la sua Vita scende a zero.
#
# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Rimuovere direttamente un elemento da una lista con .remove()
# - Distinguere .remove(elemento) da .pop(indice)
# - Modificare lo stato di un esercito durante il combattimento
# - Eliminare un'unità morta dalla lista che la contiene

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
        "Vita": 30
    }
]


def attacca(attaccante, bersaglio, esercito_bersaglio):
    bersaglio["Vita"] -= attaccante["Danno"]

    if bersaglio["Vita"] > 0:
        print(f"{bersaglio['Tipo']} rimane con {bersaglio['Vita']} punti vita")
    else:
        bersaglio["Vita"] = 0
        print(f"{bersaglio['Tipo']} è morto")
        esercito_bersaglio.remove(bersaglio)


attacca(EsercitoAmandola[0], EsercitoNemico[1], EsercitoNemico)

print(EsercitoNemico)
