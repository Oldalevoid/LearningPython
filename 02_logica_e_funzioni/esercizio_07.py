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
# - Usare confronti come >, <=
# - Usare l'indentazione per definire i blocchi di codice
# - Ripetere istruzioni con while
# - Combinare condizioni con and
# - Importare una libreria con import
# - Generare numeri casuali con random.randint()
# - Capire la differenza tra codice dentro e fuori da un ciclo:
#   dentro il while viene eseguito a ogni iterazione

import random

TipoArcere = "Arcere della Sibilla"
VitaArcere = 80

TipoGuerriero = "Guerriero dei Sibillini"
VitaGuerriero = 100

while VitaArcere > 0 and VitaGuerriero > 0:
  DannoArcere = random.randint(20, 30)
  print("Una freccia sibila nel vento")
  VitaGuerriero = VitaGuerriero - DannoArcere
  print(f"Il guerriero ha {VitaGuerriero} punti vita")
  
  if VitaGuerriero > 0:
    DannoGuerriero = random.randint(35, 45)
    print("Rumore di lame che affondano nelle carni")
    VitaArcere = VitaArcere - DannoGuerriero
    print(f"L'arcere ha {VitaArcere} punti vita")

if VitaArcere <= 0:
  print("L'arcere è morto")
else:
  print("Il guerriero è morto")
