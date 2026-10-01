Tipo = "Arcere della Sibilla"
Vita = 80
Danno = 20

print(f"{Tipo} ha {Vita} punti vita")

while Vita > 0:
    Danni = int(input("Quanti danni subisce l'Arcere?"))
    print(f"{Tipo} dice ARGHHHHHHH")
    Vita = Vita - Danni
    print(f"Ora l'arcere ha {Vita} di vita")

print("L'arcere è morto")
