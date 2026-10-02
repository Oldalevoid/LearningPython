# DESCRIZIONE
# Simula una battaglia tra due eserciti separando il calcolo del danno
# dall'applicazione del danno. La funzione calcoladanno() gestisce schivata,
# critico e armatura; attacca() applica il risultato alla vita e gestisce la morte.
#
# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Dividere una logica complessa in più funzioni con responsabilità diverse
# - Restituire da una funzione un valore calcolato con return
# - Usare return 0 per rappresentare un attacco schivato
# - Controllare il valore restituito prima di applicare il danno
# - Separare il calcolo del danno dalla modifica dello stato del bersaglio

import random

EsercitoAmandola = [
    {
        "Tipo": "Guerriero della Sibilla",
        "Danno": 35,
        "Vita": 100,
        "Armatura": 10
    },
    {
        "Tipo": "Mago Piceno",
        "Danno": 60,
        "Vita": 50,
        "Armatura": 0
    }
]

EsercitoNemico = [
    {
        "Tipo": "Orco delle Gole",
        "Danno": 40,
        "Vita": 120,
        "Armatura": 20
    },
    {
        "Tipo": "Goblin della Marca",
        "Danno": 20,
        "Vita": 60,
        "Armatura": 3
    }
]


def calcoladanno(attaccante, bersaglio):
    schivata = random.randint(1, 100)

    if schivata <= 20:
        print("NON CE SO CCOTO PAHRCOIVVDDVIO")
        return 0

    varnellihit = random.randint(1, 100)
    danno = attaccante["Danno"]

    if varnellihit > 70:
        danno = danno * 2
        print("TREMILA DI TE PER FARNE UNO DI ME!!")

    dannoeffettivo = danno - bersaglio["Armatura"]

    if dannoeffettivo < 1:
        dannoeffettivo = 1

    return dannoeffettivo


def attacca(attaccante, bersaglio, esercito_bersaglio):
    dannoeffettivo = calcoladanno(attaccante, bersaglio)

    if dannoeffettivo == 0:
        return

    bersaglio["Vita"] -= dannoeffettivo

    print(f"Danno effettivo: {dannoeffettivo}")

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
