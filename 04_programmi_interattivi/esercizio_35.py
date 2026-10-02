# DESCRIZIONE
# Simula una battaglia tra due eserciti organizzando il codice in funzioni
# con responsabilità distinte. combattimento() gestisce un intero scambio
# di attacchi tra i due eserciti, rendendo il ciclo principale più semplice.
#
# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Spostare un intero turno di combattimento in una funzione dedicata
# - Rendere il ciclo principale più corto e leggibile
# - Usare parametri di funzione invece di dipendere da variabili globali
# - Controllare il valore restituito da una funzione prima di usarlo
# - Organizzare meglio il flusso del programma senza introdurre classi

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


turno = 0

while len(EsercitoAmandola) > 0 and len(EsercitoNemico) > 0:
    turno += 1
    print(f"-- TURNO {turno} --")
    combattimento(EsercitoAmandola, EsercitoNemico)


if len(EsercitoAmandola) > 0:
    print("A CHI LA MORTE? A NOI")
else:
    print("BWFWAARRRGHHHHHH")
