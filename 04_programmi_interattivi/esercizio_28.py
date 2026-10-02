# DESCRIZIONE
# Simula una battaglia tra due piccoli eserciti.
# Le prime unità disponibili si attaccano a turno finché uno dei due eserciti
# rimane senza unità. Le unità morte vengono rimosse dalla propria lista.
#
# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Usare un ciclo while per gestire una battaglia che continua nel tempo
# - Controllare che entrambi gli eserciti abbiano ancora unità
# - Evitare l'accesso all'indice 0 di una lista vuota
# - Far evolvere lo stato di due liste durante un ciclo
# - Terminare il combattimento quando uno dei due eserciti resta senza unità

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
    attacca(EsercitoAmandola[0], EsercitoNemico[0], EsercitoNemico)

    if len(EsercitoNemico) > 0:
        attacca(EsercitoNemico[0], EsercitoAmandola[0], EsercitoAmandola)


if len(EsercitoAmandola) > 0:
    print("A CHI LA MORTE? A NOI")
else:
    print("BWFWAARRRGHHHHHH")
