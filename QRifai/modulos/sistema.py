import os
import datetime
from art import *

def separador():
    print("=" * 50)

def cls():
    os.system('cls')
    separador()
    tprint("        QRifai")
    separador()

def msg_listo():
    fin = "♥ Listo ♥"
    print(f"{fin:^50}")
    separador()

def ruta_fin_qr():
    descargas_path = os.path.join(os.path.expanduser('~'), 'Downloads') #Obtener ruta raiz de descargas
    carpeta_qr = os.path.join(descargas_path, 'Qr') #Crear carpeta de qr
    if not os.path.exists(carpeta_qr): #Si la carpeta no existe...
        os.makedirs(carpeta_qr)  #...pues lo crea
    return carpeta_qr

def obtener_nombre():
    fecha_hora_actual = datetime.datetime.now()
    nombre = str(fecha_hora_actual.strftime("%d%m%y-%H%M%S"))  # Cambio los ":" a "" en la marca de tiempo.
    return nombre + ".png"

def opcion(respuesta, opcion_valida):
    """Pide al usuario que introduzca una opción válida.

    Args:
        respuesta: Un string que se mostrará al usuario antes de pedirle la opción.
        opcion_valida: Una lista de opciones válidas.

    Returns:
        La opción elegida por el usuario.
    """
    while True:
        try:
            opcion = int(input(respuesta))
            if opcion in opcion_valida:
                return opcion
            else:
                cls()
        except ValueError:
            cls()