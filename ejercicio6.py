"""Ejercicio 6"""
import qrcode #libreria para generar el QR

def generar_qr(texto):
    """
    Genera un código QR a partir de un texto dado.

    Argumentos:
    - texto: el texto que se desea codificar en el código QR.

    Retorna:
    - Una imagen del código QR generado.
    """
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(texto)
    qr.make(fit=True)
    imagen = qr.make_image(fill_color="black", back_color="white")
    return imagen

texto_usuario = input("Ingrese el texto para el código QR: ")

CODIGO_QR = generar_qr(texto_usuario)

# Guardar el código QR como una imagen PNG
NOMBRE_ARCHIVO = "codigo_qr.png"
CODIGO_QR.save(NOMBRE_ARCHIVO)

# Mostrar la imagen del código QR
CODIGO_QR.show()
