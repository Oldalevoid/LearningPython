TipoArcere = "Arcere della Sibilla"
DannoArcere = 25
VitaArcere = 80

TipoGuerriero = "Guerriero dei Sibillini"
DannoGuerriero = 30
VitaGuerriero = 100

while VitaArcere > 0 and VitaGuerriero > 0:
  print ("Una freccia sibila nel vento")
  VitaGuerriero = VitaGuerriero - DannoArcere
  print(VitaGuerriero)
  
  if VitaGuerriero > 0:
    print("Rumore di lame che affondano nelle carni")
    VitaArcere = VitaArcere - DannoGuerriero
    print(VitaArcere)
  

if VitaArcere <= 0:
  print("L'arcere è morto")
else:
  print("Il guerriero è morto")
