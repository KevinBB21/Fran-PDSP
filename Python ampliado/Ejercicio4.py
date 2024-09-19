entrada = input("Dime una cadena y te dire cuantas mayusculas posee \n")

mincar= ord('A')
maxcar= ord('Z')

letrasmay = 0

for i in entrada :
    if ord(i) >= mincar and ord(i) <= maxcar:
        letrasmay += 1

print(letrasmay)