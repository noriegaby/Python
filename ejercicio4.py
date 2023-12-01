"""Ejercicio 4"""

import random
nombre_jugador = input("Por favor, ingresa tu nombre: ")
PUNTAJE_USUARIO = 0
PUNTAJE_COMPUTADORA = 0

def obtener_opcion_computadora():
    """
    Genera aleatoriamente la elección de la computadora entre piedra, papel o tijera.

    Retorna:
    - La elección aleatoria de la computadora ('piedra', 'papel' o 'tijera').
    """
    opciones = ['piedra', 'papel', 'tijera']
    return random.choice(opciones)


def obtener_opcion_usuario():
    """
    Solicita al usuario que elija entre piedra, papel o tijera.

    Retorna:
    - La elección del usuario en minúsculas ('piedra', 'papel' o 'tijera').
    """
    while True:
        opcion = input("Elige piedra, papel o tijera: ").lower()
        if opcion in ['piedra', 'papel', 'tijera']:
            return opcion
        else:
            print("Opción inválida. Intenta de nuevo.")
            

def juego_piedra_papel_tijera(usuario, computadora):
    """
    Realiza un juego de piedra, papel o tijera y devuelve el resultado.

    Argumentos:
    - usuario: la elección del usuario ('piedra', 'papel' o 'tijera')
    - computadora: la elección aleatoria de la computadora ('piedra', 'papel' o 'tijera')

    Retorna:
    - Una cadena que indica el resultado del juego.
    - Puntos del usuario (1 si gana, 0 si empata o pierde).
    - Puntos de la computadora (1 si gana, 0 si empata o pierde).
    """
    if usuario == computadora:
        return "¡Es un empate!", 0, 0
    elif (usuario == "piedra" and computadora == "tijera") or (usuario == "papel" and computadora == "piedra") or (usuario == "tijera" and computadora == "papel"):
        return "¡Ganaste!", 1, 0
    else:
        return "¡La computadora gana!", 0, 1


while True:
    # Obtener la opción del usuario llamando a la funcion obtener_opcion_usuario() y almacena la eleccion en opcion_usuario
    opcion_usuario = obtener_opcion_usuario() 

    # Obtener la opción de la computadora
    opcion_computadora = obtener_opcion_computadora()

    # Mostrar las elecciones del usuario y la computadora
    print(f"Tu elección: {opcion_usuario}")
    print(f"Elección de la computadora: {opcion_computadora}")

    # Determinar el resultado y actualizar los puntajes
    resultado, puntos_usuario, puntos_computadora = juego_piedra_papel_tijera(opcion_usuario, opcion_computadora)
    PUNTAJE_USUARIO += puntos_usuario
    PUNTAJE_COMPUTADORA += puntos_computadora
    print(resultado)

    # Preguntar si quiere seguir jugando
    continuar = input("¿Quieres seguir jugando? (S/N): ").lower()
    if continuar != "s":
        break

# Mostrar los resultados finales con el nombre del jugador
print(f"\nPuntaje final \n {nombre_jugador}: {PUNTAJE_USUARIO}, Computadora: {PUNTAJE_COMPUTADORA}")
if PUNTAJE_USUARIO > PUNTAJE_COMPUTADORA:
    print(f"¡{nombre_jugador} ha ganado!")
elif PUNTAJE_USUARIO < PUNTAJE_COMPUTADORA:
    print("La computadora ha ganado.")
else:
    print("¡Es un empate!")
