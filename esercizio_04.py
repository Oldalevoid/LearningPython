Tipo = "Arcere della Sibilla"
Vita = 80
Danno = 20

print(f"{Tipo} ha {Vita} punti vita")

danni = int(input("Quanti danni subisce l'Arcere?"))
print(f"{Tipo} dice ARGHHHHHHH")
Vita = Vita - danni

if Vita <= 0:
    print("L'Arcere è morto")
elif Vita <= 30:
    print("L'Arcere è gravemente ferito")
elif Vita <= 60:
    print("L'Arcere tentenna")
else:
    print("Arcere Pronto!")
