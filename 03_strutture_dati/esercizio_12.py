# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Creare un dizionario usando le parentesi graffe {}
# - Rappresentare un'unità con più proprietà collegate
# - Usare coppie chiave: valore
# - Leggere un valore del dizionario tramite la sua chiave
# - Modificare il valore associato a una chiave
# - Stampare sia l'intero dizionario sia singole proprietà

Arcere = {
  "Tipo": "Arcere della Sibilla",
  "Danno": 25,
  "Vita": 80
}

print(Arcere)

print(Arcere["Tipo"])
print(Arcere["Vita"])

Arcere["Vita"] = Arcere["Vita"] - 30
print(Arcere["Vita"])
