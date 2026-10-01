# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Usare valori booleani: True e False
# - Usare una variabile booleana per ricordare se una condizione si è verificata
# - Cambiare il valore di una variabile booleana durante l'esecuzione
# - Interrompere un ciclo for con break
# - Usare una variabile booleana per gestire il caso in cui una ricerca non trovi risultati

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

ricerca = input("Quale unità vuoi ricercare? ")

trovato = False

for unita in EsercitoAmandola:
  if ricerca == unita["Tipo"]:
    print("Trovato")
    trovato = True
    print(unita)
    break

if trovato == False:
    print("L'unità non esiste")
