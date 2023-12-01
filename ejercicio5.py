"""Ejercicio 5"""

def busqueda_binaria(lista, elemento):
    """
    Realiza una búsqueda binaria en una lista ordenada para encontrar un elemento dado.

    Argumentos:
    - lista: una lista ordenada de números enteros.
    - elemento: el número que se desea buscar en la lista.

    Retorna:
    - La posición del elemento en la lista si se encuentra.
    - '-1' si el elemento no está presente en la lista.
    """
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        # Verificar si el elemento está en el medio
        if lista[medio] == elemento:
            return medio
        # Si el elemento es mayor, buscar en la mitad derecha
        elif lista[medio] < elemento:
            izquierda = medio + 1
        # Si el elemento es menor, buscar en la mitad izquierda
        else:
            derecha = medio - 1

    return -1  # Si no se encuentra el elemento en la lista

# Obtener la lista ordenada de números del usuario
entrada = input("Ingrese una lista ordenada de números separados por comas: ")
numeros = [int(numero) for numero in entrada.split(",")]

# Obtener el número a buscar
numero_a_buscar = int(input("Ingrese el número a buscar: "))

# Aplicar la búsqueda binaria
posicion = busqueda_binaria(numeros, numero_a_buscar)

# Mostrar el resultado
if posicion != -1:
    print(f"El número {numero_a_buscar} se encuentra en la posición {posicion} de la lista.")
else:
    print(f"El número {numero_a_buscar} no se encontró en la lista.")
