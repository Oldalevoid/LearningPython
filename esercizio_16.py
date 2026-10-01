# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Cercare un elemento dentro una lista di dizionari
# - Combinare un ciclo for con una condizione if
# - Confrontare il valore cercato con una proprietà del dizionario usando ==
# - Usare input() per scegliere dinamicamente cosa cercare
# - Evitare di usare nomi di funzioni integrate, come input, come nomi di variabili

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

for unita in EsercitoAmandola:
  if ricerca == unita["Tipo"]:
    print("Trovato")
    print(unita)
