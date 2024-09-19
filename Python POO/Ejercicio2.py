class ParSumador:
    def __init__(self, numeros, objetivo):
        self.numeros = numeros
        self.objetivo = objetivo

    def encontrar_indices(self):
        indices = {}
        for i, numero in enumerate(self.numeros):
            complemento = self.objetivo - numero
            if complemento in indices:              
                return indices[complemento] + 1, i + 1
            indices[numero] = i
        return None  

numeros = [10, 20, 10, 40, 50, 60, 70]
objetivo = 50
par_sumador = ParSumador(numeros, objetivo)
resultado = par_sumador.encontrar_indices()

if resultado:
    print(f"Salida: {resultado[0]}, {resultado[1]}")
else:
    print("No se encontró ningún par que sume el objetivo.")