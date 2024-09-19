any_actual = int(input("Ingrese el año en curso: "))
cantidad_alumnos = int(input("Ingresa tambien la cantidad de alumnos que deseas comprobar \n "))

personas = []

for i in range(cantidad_alumnos):
    nombre = input(f"Ingrese el nombre de la persona : \n ")
    any_nacimiento = int(input("Ingrese el año de nacimiento :  \n"))
    edad = any_actual - any_nacimiento
    personas.append((nombre, any_nacimiento, edad))

print("\n Datos de las personas:")
for nombre, any_nacimiento, edad in personas:
    print(f"{nombre} nació en {any_nacimiento} y cumplirá {edad} años en {any_actual}.")