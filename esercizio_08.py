# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Creare una funzione con def
# - Definire parametri dentro una funzione
# - Passare valori a una funzione quando viene chiamata
# - Richiamare la stessa funzione più volte per evitare codice duplicato
# - Capire che i parametri ricevono automaticamente i valori passati alla funzione
# - Capire meglio la differenza tra = e ==:
#   = assegna un valore, == confronta due valori

import random

def mostrastato(Tipo, Vita):
  print(f"{Tipo} ha {Vita} punti vita")


TipoArcere = "Arcere della Sibilla"
VitaArcere = 80

TipoGuerriero = "Guerriero dei Sibillini"
VitaGuerriero = 100

while VitaArcere > 0 and VitaGuerriero > 0:
  DannoArcere = random.randint(20, 30)
  print("Una freccia sibila nel vento")
  VitaGuerriero = VitaGuerriero - DannoArcere
  mostrastato(TipoGuerriero, VitaGuerriero)
  
  if VitaGuerriero > 0:
    DannoGuerriero = random.randint(35, 45)
    print("Rumore di lame che affondano nelle carni")
    VitaArcere = VitaArcere - DannoGuerriero
    mostrastato(TipoArcere, VitaArcere)

if VitaArcere <= 0:
  print("L'arcere è morto")
else:
  print("Il guerriero è morto")
