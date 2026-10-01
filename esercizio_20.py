# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Usare continue dentro un ciclo
# - Ripetere una richiesta di input finché l'utente non inserisce un valore valido
# - Combinare while True con try ed except
# - Usare break per uscire dal ciclo quando il dato è corretto
# - Capire la differenza tra break e continue:
#   break termina il ciclo, continue passa alla prossima iterazione
# - Rendere più robusta una funzione evitando di interrompere il reclutamento al primo errore

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


def reclutamento():
  tipo = input("Inserisci il tipo ")

  while True:
    try:
      vita = int(input("Inserisci la vita "))
      break
    except ValueError:
      print("la vita deve avere un valore numerico ")
      continue

  while True:
    try:
      danno = int(input("Inserisci quanto danno deve fare "))
      break
    except ValueError:
      print("Il danno deve avere un valore numerico")
      continue
 
  return {
    "Tipo": tipo,
    "Danno": danno,
    "Vita": vita
  }

recluta = reclutamento()
EsercitoAmandola.append(recluta)

print(EsercitoAmandola)
