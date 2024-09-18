entrada = input("Buenas, dime los números que quieras separados por espacios y te daré el más grande: ")
listanum = [int(num) for num in entrada.split()]

mayor = listanum[0]

for num in listanum:
    if num > mayor:
        mayor = num

print(mayor)


    