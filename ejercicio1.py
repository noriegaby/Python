"""Ejercicio 1"""
def contar_mayusculas(cadena):
    """
    Cuenta el número de letras mayúsculas en una cadena dada.

    Argumentos:
    - cadena: una cadena de texto

    Retorna:
    - El número de letras mayúsculas en la cadena.
    """
    contador = 0

    for caracter in cadena:
        if caracter.isupper(): #busca mayusculas
            contador += 1

    return contador


print(contar_mayusculas("Hola Mundo")) 
print(contar_mayusculas("Esta es mi direccion, Prol Angel Leaño 445"))
print(contar_mayusculas("123ABC"))
