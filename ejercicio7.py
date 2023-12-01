"""Ejercicio 6"""
import sqlite3 #librería proporciona una API para trabajar con bases de datos SQLite 
import json # librería proporciona funcionalidades para trabajar con datos en formato JSON 

# Conexión a la base de datos SQLite (creará el archivo si no existe)
conexion = sqlite3.connect('datos_personas.db') #variable conexion - metodo sqlite3.connect

# Cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Crear tabla personas si no existe
cursor.execute('''CREATE TABLE IF NOT EXISTS personas (
                    nombre TEXT,
                    edad INTEGER,
                    genero TEXT,
                    ocupacion TEXT,
                    UNIQUE(nombre, edad, genero, ocupacion)
                )''')

# Leer el archivo JSON y agregar los datos que no existan en la base de datos
with open('datos_personas.json', 'r', encoding="utf-8") as archivo_json:
    datos = json.load(archivo_json)
    for persona in datos:
        cursor.execute('SELECT * FROM personas WHERE nombre=? AND edad=? AND genero=? AND ocupacion=?',
                       (persona['nombre'], persona['edad'], persona['genero'], persona['ocupacion']))
        existe_registro = cursor.fetchone()
        if not existe_registro:
            cursor.execute('INSERT INTO personas VALUES (?, ?, ?, ?)',
                           (persona['nombre'], persona['edad'], persona['genero'], persona['ocupacion']))

# Confirmar los cambios y cerrar la conexión
conexion.commit()
conexion.close()

print("Los datos se han insertado correctamente en la base de datos.")
