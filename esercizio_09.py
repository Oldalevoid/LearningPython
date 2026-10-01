# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Usare return per far restituire un valore a una funzione
# - Assegnare a una variabile il valore restituito da una funzione
# - Passare parametri a una funzione per renderla riutilizzabile
# - Usare una funzione per generare valori casuali con random.randint()
# - Capire la differenza tra una funzione che stampa un valore e una funzione che lo restituisce

import random

def mostrastato(Tipo, Vita):
  print(f"{Tipo} ha {Vita} punti vita")

def generadanno(min, max):
  danno = random.randint(min,max)
  return danno


TipoArcere = "Arcere della Sibilla"
VitaArcere = 80

TipoGuerriero = "Guerriero dei Sibillini"
VitaGuerriero = 100

while VitaArcere > 0 and VitaGuerriero > 0:
  DannoArcere = generadanno(20,30)
  print("Una freccia sibila nel vento")
  VitaGuerriero = VitaGuerriero - DannoArcere
  mostrastato(TipoGuerriero, VitaGuerriero)
  
  if VitaGuerriero > 0:
    DannoGuerriero = generadanno(35,45)
    print("Rumore di lame che affondano nelle carni")
    VitaArcere = VitaArcere - DannoGuerriero
    mostrastato(TipoArcere, VitaArcere)

if VitaArcere <= 0:
  print("L'arcere è morto")
else:
  print("Il guerriero è morto")
