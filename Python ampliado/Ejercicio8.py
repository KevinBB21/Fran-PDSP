def contar_vocales(frase):

    conteo_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    frase = frase.lower()
    
    for letra in frase:
        if letra in conteo_vocales:
            conteo_vocales[letra] += 1
            
    return conteo_vocales

frase = input("Dime una frase para sacar sus vocales ")
resultado = contar_vocales(frase)
print(resultado)