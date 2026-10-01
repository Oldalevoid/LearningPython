Tipo = "Arcere della Sibilla"
Vita = 80
Danno = 20

print(f"{Tipo} ha {Vita} punti vita")

danni = int(input("Quanti danni subisce l'arcere?"))
print(f"{Tipo} dice ARGHHHHHHH")
Vita = Vita - danni

if Vita <= 0:
    print("L'arcere è morto")
else:
    print("Arcere Pronto!")
