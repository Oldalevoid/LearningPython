# DESCRIZIONE
# Simula una battaglia tra due eserciti scegliendo casualmente, a ogni turno,
# l'unità che attacca e il bersaglio. Le unità morte vengono rimosse dalla lista.
#
# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Usare random.choice() per selezionare un elemento casuale da una lista
# - Rendere meno rigido un ciclo di battaglia scegliendo unità casuali
# - Riutilizzare una funzione di attacco con attaccanti e bersagli variabili
# - Mantenere il controllo sulla lista vuota prima del secondo attacco del turno

import random

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


def attacca(attaccante, bersaglio, esercito_bersaglio):
    bersaglio["Vita"] -= attaccante["Danno"]

    if bersaglio["Vita"] > 0:
        print(f"{bersaglio['Tipo']} rimane con {bersaglio['Vita']} punti vita")
    else:
        bersaglio["Vita"] = 0
        print(f"{bersaglio['Tipo']} è morto")
        esercito_bersaglio.remove(bersaglio)


while len(EsercitoAmandola) > 0 and len(EsercitoNemico) > 0:
    attacca(random.choice(EsercitoAmandola), random.choice(EsercitoNemico), EsercitoNemico)

    if len(EsercitoNemico) > 0:
        attacca(random.choice(EsercitoNemico), random.choice(EsercitoAmandola), EsercitoAmandola)


if len(EsercitoAmandola) > 0:
    print("A CHI LA MORTE? A NOI")
else:
    print("BWFWAARRRGHHHHHH")
