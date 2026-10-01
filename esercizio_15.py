# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Rimuovere un elemento da una lista con .pop(indice)
# - Capire che .pop() restituisce l'elemento rimosso
# - Salvare l'elemento rimosso in una variabile
# - Accedere alle proprietà di un dizionario rimosso dalla lista
# - Verificare con len() che la lista contiene un elemento in meno
# - Capire che gli indici della lista cambiano dopo una rimozione
# - Gestire correttamente apici singoli e doppi dentro una f-string

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

UnitaCaduta = EsercitoAmandola.pop(2)
print(f"{UnitaCaduta['Tipo']} è caduto in battaglia")

print(f"L'esercito ora è composto da {len(EsercitoAmandola)} unità")

for unita in EsercitoAmandola:
    print(f'{unita["Tipo"]} - Vita: {unita["Vita"]} - Danno: {unita["Danno"]}')
