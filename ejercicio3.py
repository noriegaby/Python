"""Ejercicio 3"""
import random  # Módulo para generar caracteres aleatorios
import string # Para acceder a ascii lower y upper, digits y punctuation

def generar_password():
    """
    Genera una contraseña aleatoria que contiene letras mayúsculas, minúsculas, dígitos y símbolos.

    Retorna:
    - Una cadena que representa la contraseña generada.
    """
    letras_min = string.ascii_lowercase
    letras_may = string.ascii_uppercase
    digitos = string.digits
    simbolos = string.punctuation

    # Generar por lo menos un carácter de cada tipo
    caracter = random.choice(letras_min)
    caracter += random.choice(letras_may)
    caracter += random.choice(digitos)
    caracter += random.choice(simbolos)

    # Generar el resto de la contraseña aleatoria metodo random choise
    longitud_restante = 4
    caracter += ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=longitud_restante))

    # Convertir la cadena a lista para mezclarla, ramdom.shuffle método cambia la lista original
    lista_caracteres = list(caracter)
    random.shuffle(lista_caracteres)

    # Convertir la lista nuevamente a cadena con join   
    password = ''.join(lista_caracteres)
    return password

# Generar la contraseña
CONTRASENA = generar_password()
print("Contraseña generada:", CONTRASENA)
