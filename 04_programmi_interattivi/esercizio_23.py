# DESCRIZIONE
# Mostra un esercito numerato, permette all'utente di selezionare un'unità
# e restituisce direttamente il dizionario dell'unità scelta.
# La funzione è riutilizzabile con qualunque lista di unità strutturata allo stesso modo.
#
# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Passare una lista come argomento a una funzione
# - Far lavorare una funzione direttamente su una struttura dati
# - Usare len() sul parametro ricevuto invece di dipendere da una variabile globale
# - Restituire un intero dizionario con return
# - Salvare il valore restituito da una funzione
# - Accedere ai campi del dizionario restituito

EsercitoAmandola = [
    {
        "Tipo": "Arcere della Sibilla",
        "Danno": 25,
        "Vita": 80
    },
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


def seleziona_unita(esercito):
    for numero, unita in enumerate(esercito, start=1):
        print(numero, "-", unita["Tipo"])

    while True:
        try:
            scelta = int(input("Quale unità vuoi selezionare? "))

            if scelta >= 1 and scelta <= len(esercito):
                indice = scelta - 1
                break
            else:
                print("La scelta deve essere compresa tra 1 e", len(esercito))
        except ValueError:
            print("Inserisci un numero")

    return esercito[indice]


unitascelta = seleziona_unita(EsercitoAmandola)

print(f"Hai selezionato: {unitascelta['Tipo']}")
print(f"Danno: {unitascelta['Danno']}")
print(f"Vita: {unitascelta['Vita']}")
