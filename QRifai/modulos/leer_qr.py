import cv2
from modulos.sistema import (
    cls, 
    msg_listo,
    separador as sp
)
    
def obt_ruta_qr():
    ruta = input("Introduzca la ruta del QR a leer\nClick derecho en el codigo, y \"Copiar como ruta\"\n(Windows suele colocar comillas en la ruta, borralos)\n> ")
    try:
        ruta = ruta.strip('"')
        return ruta
    except FileNotFoundError:
        print("El archivo no existe")
        return obt_ruta_qr()

def leer_qr(image_path):
    try:
        img = cv2.imread(image_path)
        det = cv2.QRCodeDetector()
        valorQRLeido, pts, st_code = det.detectAndDecode(img)
        return valorQRLeido
    except cv2.error:
        print("No se pudo leer el codigo\n Revisa que la ruta sea correcta")

def opc_leer_qr():
    """Permite al usuario leer el contendio de un codigo QR.

    El codigo debe estar en formato PNG.

    Returns:
        El texto contenido en el codigo QR.
    """
    while True:
        cls()
        image_path = obt_ruta_qr() # Pedimos ruta
        try:
            valorQRLeido = leer_qr(image_path) # Se lee la imagen dada
        except cv2.error:
            cls()
            sp()
            print("No se pudo leer el código QR")
            break
        else:
            cls()
            sp()
            if valorQRLeido is not None: # Cuando hay un error, python retorna "None" y falla. Aquí evitamos eso
                print(f"El texto del QR es:\n{valorQRLeido:^50}") # Imprimir el texto convertido
            else:
                print("No se pudo leer el código QR") # Imprimir error cuando sea el caso
            sp()
        msg_listo()
        respuesta = input("¿Deseas hacer otro codigo QR (Y/N)? ").strip().lower()
        if respuesta != 'y':
            break