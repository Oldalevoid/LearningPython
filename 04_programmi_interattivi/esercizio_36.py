# DESCRIZIONE
# Simula una battaglia completa tra due eserciti organizzando la logica
# in funzioni dedicate. battaglia() gestisce l'intero ciclo dei turni e
# determina il vincitore, mentre combattimento(), attacca() e calcoladanno()
# gestiscono livelli più specifici della logica.
#
# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Spostare l'intero ciclo della battaglia in una funzione dedicata
# - Rendere il programma principale quasi ridotto a una singola chiamata
# - Mantenere il contatore dei turni fuori dal ciclo per non azzerarlo ogni volta
# - Usare funzioni annidate per livelli di responsabilità sempre più chiari
# - Interrompere correttamente un attacco quando il danno restituito è 0

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


def combattimento(esercitobuono, esercitoavversario):
    combattenteamandola = random.choice(esercitobuono)
    combattenteorco = random.choice(esercitoavversario)

    print(f"{combattenteamandola['Tipo']} attacca {combattenteorco['Tipo']}!")
    attacca(combattenteamandola, combattenteorco, esercitoavversario)

    if len(esercitoavversario) > 0:
        combattenteorco = random.choice(esercitoavversario)
        combattenteamandola = random.choice(esercitobuono)

        print(f"{combattenteorco['Tipo']} attacca {combattenteamandola['Tipo']}!")
        attacca(combattenteorco, combattenteamandola, esercitobuono)


def battaglia(esercitobuono, esercitoavversario):
    turno = 0

    while len(esercitobuono) > 0 and len(esercitoavversario) > 0:
        turno += 1
        print(f"______________________________ TURNO {turno} ________________________________")
        combattimento(esercitobuono, esercitoavversario)

    if len(esercitobuono) > 0:
        print("A CHI LA MORTE? A NOI")
    else:
        print("BWFWAARRRGHHHHHH")


battaglia(EsercitoAmandola, EsercitoNemico)
