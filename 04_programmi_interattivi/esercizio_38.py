# DESCRIZIONE
# Introduce una prima risorsa di gioco: l'oro.
# Le unità hanno un costo e possono essere reclutate solo se il giocatore
# possiede abbastanza oro. Il costo viene sottratto e l'unità viene aggiunta
# all'esercito tramite append().
#
# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Aggiungere un costo alle unità tramite una nuova chiave del dizionario
# - Usare append() per inserire un'unità dentro un esercito
# - Modificare una risorsa numerica e restituirne il valore aggiornato
# - Usare >= per consentire un acquisto anche quando oro e costo coincidono
#
# CONCETTO IMPORTANTE
# Una funzione che deve restituire un valore deve farlo in tutti i percorsi
# possibili. Se un ramo termina senza return, Python restituisce automaticamente
# None. Se poi quel risultato viene salvato, ad esempio con:
#     oro = recluta(...)
# la variabile oro può diventare None e causare errori nei confronti successivi.

GuerrieroSibilla = {
    "Tipo": "Guerriero della Sibilla",
    "Danno": 35,
    "Vita": 100,
    "Armatura": 10,
    "Costo": 100
}

MagoPiceno = {
    "Tipo": "Mago Piceno",
    "Danno": 60,
    "Vita": 50,
    "Armatura": 0,
    "Costo": 150
}

EsercitoAmandola = []

oro = 300


def recluta(unita, esercito, oro):
    if oro >= unita["Costo"]:
        oro -= unita["Costo"]
        esercito.append(unita)
        return oro
    else:
        print("Oro insufficiente per il reclutamento")
        return oro


oro = recluta(GuerrieroSibilla, EsercitoAmandola, oro)
oro = recluta(MagoPiceno, EsercitoAmandola, oro)

print(EsercitoAmandola)
print(f"Oro rimasto: {oro}")
