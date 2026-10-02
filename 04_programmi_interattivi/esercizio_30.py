# DESCRIZIONE
# Simula una battaglia tra due eserciti scegliendo casualmente attaccanti e bersagli
# a ogni turno. Il programma mostra il numero del turno e chi attacca chi.
#
# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Salvare in variabili gli elementi scelti con random.choice()
# - Rendere più leggibile una simulazione stampando chi attacca chi
# - Usare un contatore dei turni
# - Effettuare una nuova selezione casuale dopo una possibile eliminazione
# - Evitare che un'unità morta continui ad attaccare

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


turno = 0

while len(EsercitoAmandola) > 0 and len(EsercitoNemico) > 0:
    turno += 1
    print(f"-- TURNO {turno} --")

    combattenteamandola = random.choice(EsercitoAmandola)
    combattenteorco = random.choice(EsercitoNemico)

    print(f"{combattenteamandola['Tipo']} attacca {combattenteorco['Tipo']}!")
    attacca(combattenteamandola, combattenteorco, EsercitoNemico)

    if len(EsercitoNemico) > 0:
        combattenteorco = random.choice(EsercitoNemico)
        combattenteamandola = random.choice(EsercitoAmandola)

        print(f"{combattenteorco['Tipo']} attacca {combattenteamandola['Tipo']}!")
        attacca(combattenteorco, combattenteamandola, EsercitoAmandola)


if len(EsercitoAmandola) > 0:
    print("A CHI LA MORTE? A NOI")
else:
    print("BWFWAARRRGHHHHHH")
