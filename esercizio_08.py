# CONCETTI IMPARATI FINO A QUESTO ESERCIZIO
# - Creare variabili con =
# - Usare stringhe, ad esempio: Tipo = "Arcere"
# - Usare numeri interi, ad esempio: Vita = 80
# - Stampare valori con print()
# - Inserire variabili nel testo con le f-string: f"{variabile}"
# - Eseguire operazioni matematiche, in particolare sottrazioni
# - Aggiornare il valore di una variabile: Vita = Vita - Danno
# - Ricevere dati dall'utente con input()
# - Convertire il testo in numero con int()
# - Usare condizioni con if, elif ed else
# - Usare confronti come >, <= e ==
# - Capire la differenza tra = e ==:
#   = assegna un valore, == confronta due valori
# - Usare l'indentazione per definire i blocchi di codice
# - Ripetere istruzioni con while
# - Combinare condizioni con and
# - Importare una libreria con import
# - Generare numeri casuali con random.randint()
# - Capire la differenza tra codice dentro e fuori da un ciclo
# - Creare una funzione con def
# - Passare valori a una funzione tramite parametri
# - Richiamare una funzione più volte per riutilizzare la stessa logica

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
