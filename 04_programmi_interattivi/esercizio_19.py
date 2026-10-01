# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Gestire errori con try ed except
# - Intercettare un ValueError quando int() riceve un valore non numerico
# - Restituire None da una funzione quando l'operazione non può essere completata
# - Controllare con is not None se una funzione ha restituito un valore valido
# - Evitare di aggiungere dati non validi a una lista
# - Creare e restituire un dizionario da una funzione

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
  try:
    vita = int(input("Inserisci la vita "))
  except ValueError:
    print("la vita deve avere un valore numerico ")
    return None
  try:
    danno = int(input("Inserisci quanto danno deve fare "))
  except ValueError:
    print("Il danno deve avere un valore numerico")
    return None
  return {
    "Tipo": tipo,
    "Danno": danno,
    "Vita": vita
  }

recluta = reclutamento()
if recluta is not None:
  EsercitoAmandola.append(recluta)

print(EsercitoAmandola)
