# DESCRIZIONE
# Simula una battaglia tra due eserciti con schivata, colpi critici e armatura.
# Il danno viene prima calcolato, poi ridotto dall'armatura e infine applicato
# una sola volta alla vita del bersaglio, con danno minimo pari a 1.
#
# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Aggiungere una nuova statistica alle unità tramite i dizionari
# - Separare il calcolo del danno dalla sua applicazione
# - Applicare l'armatura dopo aver determinato il danno normale o critico
# - Imporre un danno minimo per evitare valori negativi o cure involontarie
# - Applicare il danno alla vita una sola volta alla fine del calcolo

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


def attacca(attaccante, bersaglio, esercito_bersaglio):
    schivata = random.randint(1, 100)

    if schivata <= 20:
        print("NON CE SO CCOTO PAHRCOIVVDDVIO")
        return

    varnellihit = random.randint(1, 100)

    danno = attaccante["Danno"]

    if varnellihit > 70:
        danno = danno * 2
        print("TREMILA DI TE PER FARNE UNO DI ME!!")

    dannoeffettivo = danno - bersaglio["Armatura"]

    if dannoeffettivo < 1:
        dannoeffettivo = 1

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
