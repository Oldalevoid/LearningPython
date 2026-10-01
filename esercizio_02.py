Tipo = "Arcere della Sibilla"
Vita = 80
Danno = 20

print(f"Sono l'{Tipo} - Ho {Vita} di Vita e {Danno} di Danno")

danni = int(input("Quanti danni subisce l'arciere? "))
Vita = Vita - danni

print(f"L'{Tipo} ora ha {Vita} punti vita")
