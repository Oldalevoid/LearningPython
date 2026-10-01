# DESCRIZIONE
# Mostra l'esercito numerato e permette all'utente di selezionare un'unità.
# Il programma continua a chiedere la scelta finché non viene inserito un numero
# valido e compreso nell'intervallo delle unità disponibili.
#
# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Verificare che un numero sia compreso in un intervallo valido
# - Usare len() per rendere il controllo dipendente dalla lunghezza della lista
# - Distinguere un errore di conversione da un valore numerico non accettabile
# - Combinare while True, try/except e if/else per validare un input
# - Ripetere la richiesta finché l'utente non effettua una scelta valida

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

while True:
  try:
    scelta = int(input("Quale unità vuoi selezionare? "))
    if scelta >= 1 and scelta <= len(EsercitoAmandola):
      indice = scelta - 1
      break
    else:
      print("La scelta deve essere compresa tra 1 e ", len(EsercitoAmandola))
      continue
  except ValueError:
    print("Inserisci un numero ")
    
print(f"Congratulazioni, hai selezionato {EsercitoAmandola[indice]['Tipo']}")
