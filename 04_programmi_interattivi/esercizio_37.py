# DESCRIZIONE
# Simula una battaglia tra due eserciti e restituisce il nome del vincitore.
# La funzione battaglia() non decide più il messaggio finale da mostrare:
# restituisce semplicemente il risultato, che viene poi usato dal programma principale.
#
# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Restituire una stringa da una funzione con return
# - Separare il calcolo del risultato dalla sua presentazione a schermo
# - Salvare il valore restituito da una funzione in una variabile
# - Rendere una funzione più riutilizzabile passando anche i nomi degli eserciti
# - Usare il valore restituito per decidere cosa fare nel programma principale

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


def battaglia(esercitobuono, esercitoavversario, nome1, nome2):
    turno = 0

    while len(esercitobuono) > 0 and len(esercitoavversario) > 0:
        turno += 1
        print(f"______________________________ TURNO {turno} ________________________________")
        combattimento(esercitobuono, esercitoavversario)

    if len(esercitobuono) > 0:
        return nome1
    else:
        return nome2


nome_esercito_buono = "Le Guardie Della Sibilla"
nome_esercito_avversario = "Gli Orchi Di Comunanza"

vincitore = battaglia(
    EsercitoAmandola,
    EsercitoNemico,
    nome_esercito_buono,
    nome_esercito_avversario
)

if vincitore == nome_esercito_buono:
    print(f"Il sangue nemico sgorga nel Tenna, A NOI! Vincono {vincitore}")
else:
    print(f"BWFWAARRRGHHHHHH! Vincono {vincitore}")
