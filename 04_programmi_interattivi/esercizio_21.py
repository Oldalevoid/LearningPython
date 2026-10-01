# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Usare enumerate() per ottenere insieme numero e valore durante un ciclo for
# - Usare start=1 per mostrare una numerazione più naturale all'utente
# - Distinguere tra numero mostrato all'utente e indice reale della lista
# - Convertire una scelta numerica nell'indice corretto con scelta - 1
# - Accedere a un elemento specifico di una lista e poi a una chiave del dizionario contenuto

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


for numero, unita in enumerate(EsercitoAmandola, start=1):
  print(numero, "-", unita["Tipo"])

scelta = int(input("Quale unità vuoi selezionare? "))
indice = scelta - 1

print(f"Congratulazioni, hai selezionato {EsercitoAmandola[indice]['Tipo']}")
