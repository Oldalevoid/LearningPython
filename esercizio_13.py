# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Combinare liste e dizionari
# - Creare una lista in cui ogni elemento è un dizionario
# - Scorrere una lista di dizionari con un ciclo for
# - Accedere alle proprietà di ogni dizionario dentro il ciclo
# - Usare accessi annidati come lista[indice]["chiave"]
# - Modificare una proprietà di un dizionario contenuto dentro una lista
# - Stampare più proprietà dello stesso elemento con una f-string

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

print(EsercitoAmandola)
print(EsercitoAmandola[0])

for unita in EsercitoAmandola:
  print(f'{unita["Tipo"]} - Vita: {unita["Vita"]} - Danno: {unita["Danno"]}')

EsercitoAmandola[1]["Vita"] = EsercitoAmandola[1]["Vita"] - 30
print(EsercitoAmandola[1]["Vita"])
