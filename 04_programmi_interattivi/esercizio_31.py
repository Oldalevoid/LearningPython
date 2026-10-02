# DESCRIZIONE
# Simula una battaglia tra due eserciti con attaccanti e bersagli casuali.
# Ogni attacco può diventare un colpo critico con probabilità del 30%,
# infliggendo il doppio del danno senza modificare permanentemente il danno base.
#
# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Usare random.randint() per generare una probabilità semplice
# - Implementare un colpo critico tramite una condizione
# - Usare una variabile temporanea per il danno maggiorato
# - Evitare di modificare permanentemente il valore "Danno" dell'attaccante
# - Distinguere tra effetto temporaneo dell'attacco e stato permanente dell'unità

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
    varnellihit = random.randint(1, 100)
    dannomaggiorato = attaccante["Danno"] * 2

    if varnellihit > 70:
        bersaglio["Vita"] -= dannomaggiorato
        print("TREMILA DI TE PER FARNE UNO DI ME!!")
    else:
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
