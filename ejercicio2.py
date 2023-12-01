"""Ejercicio 2"""
def numeros_pares_ordenados(lista):
    """
    Devuelve una lista ordenada de números pares a partir de la lista de entrada.

    Argumentos:
    - lista: una lista de números enteros

    Retorna:
    - Una lista ordenada que contiene únicamente números pares de la lista de entrada.
    """
    pares = [num for num in lista if num % 2 == 0] #comprension de list  El resultado es una nueva lista creada tras evaluar las expresiones que haya dentro
    pares.sort() #ordena 
    return pares 

numeros = [1, 7, 8, 3, 12, 5, 6, 10, 7, 2, 12, 45]
resultado = numeros_pares_ordenados(numeros)
print(resultado)
