entrada = input("Buenas, dime las palabras que quieras separadas por espacios y te dare la mas larga: ")
listapal = [pal for pal in entrada.split()]

mas_larga = listapal[0]

for pal in listapal:
    if len(pal) > len(mas_larga):
        mas_larga = pal

print(mas_larga)

