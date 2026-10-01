# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Aggiungere un nuovo elemento a una lista con .append()
# - Aggiungere un dizionario completo dentro una lista
# - Usare len() per sapere quanti elementi contiene una lista
# - Capire che il risultato di len() cambia dopo aver aggiunto un nuovo elemento
# - Scorrere la lista aggiornata con un ciclo for

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

NuovaUnità = {
  "Tipo": "Emanuele Baratto, il giullare della discordia",
  "Danno": 5,
  "Vita": 800
}

EsercitoAmandola.append(NuovaUnità)
print(len(EsercitoAmandola))

for unita in EsercitoAmandola:
    print(f'{unita["Tipo"]} - Vita: {unita["Vita"]} - Danno: {unita["Danno"]}')
