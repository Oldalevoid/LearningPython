# DESCRIZIONE
# Applica danno a un'unità modificando direttamente il suo dizionario.
# La vita non può scendere sotto zero e il programma segnala se l'unità muore.
#
# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Modificare direttamente un dizionario ricevuto come parametro
# - Aggiornare lo stato di un oggetto senza usare return
# - Impedire che un valore scenda sotto una soglia minima
# - Usare if/else per distinguere un'unità viva da un'unità morta
# - Comprendere che modificando un dizionario dentro una funzione si modifica il dizionario originale

Guerriero = {
    "Tipo": "Guerriero della Sibilla",
    "Danno": 35,
    "Vita": 100
}


def subisci_danno(unita, danno):
    unita["Vita"] = unita["Vita"] - danno

    if unita["Vita"] < 0:
        unita["Vita"] = 0

    if unita["Vita"] == 0:
        print("L'unità è morta")
    else:
        print(f"La vita dell'unità è di {unita['Vita']} punti vita")


subisci_danno(Guerriero, 80)
subisci_danno(Guerriero, 40)
