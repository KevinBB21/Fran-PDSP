#entrada = input("Dime una lista de palabras \n")
#entradan = input("Dime a que numero tienen que ser mayor que \n")

#palabras_sep = entrada.split()


def filtrar_palabras(palabras,entradan):
    palabras_sep = palabras.split()
    palabrasmayores = []
    for palabra in palabras_sep:  
        if len(palabra) > entradan:
            palabrasmayores.append(palabra)
    print(palabrasmayores)
    

filtrar_palabras("pepepep mamama memremre memremrm meme",3)