import os
import qrcode
from modulos.sistema import (
    ruta_fin_qr,
    opcion,
    obtener_nombre,
    cls,
    msg_listo
)
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import (
    CircleModuleDrawer, 
    GappedSquareModuleDrawer, 
    HorizontalBarsDrawer, 
    RoundedModuleDrawer, 
    SquareModuleDrawer, 
    VerticalBarsDrawer,
)

def crear_qr(valorQR, opc_usuario, imagenQR):
    """Crea un código QR con el texto especificado.

    Args:
        valorQR: El texto que se incluirá en el código QR.
        opc_usuario: La opción elegida por el usuario para el tipo de código QR.
        imagenQR: El nombre del archivo de imagen del código QR.
    """
    carpeta_qr = ruta_fin_qr()
    imagenQR = os.path.join(carpeta_qr, imagenQR)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(valorQR)
    if opc_usuario == 1:
        tipoQRC = CircleModuleDrawer()
    elif opc_usuario == 2:
        tipoQRC = GappedSquareModuleDrawer()
    elif opc_usuario == 3:
        tipoQRC = VerticalBarsDrawer()
    elif opc_usuario == 4:
        tipoQRC = HorizontalBarsDrawer()
    elif opc_usuario == 5:
        tipoQRC = RoundedModuleDrawer()
    elif opc_usuario == 6:
        tipoQRC = SquareModuleDrawer()
    else:
        print("Opción no válida. Se utilizará el tipo de QR por defecto (cuadrado_grande).")
        tipoQRC = SquareModuleDrawer()
    img = qr.make_image(image_factory=StyledPilImage, module_drawer=tipoQRC)
    f = open(imagenQR, "wb")
    img.save(f)

def codigo_predeterminado():
    """Genera un código QR con el texto especificado y el formato predeterminado (cuadrado grande).

    Args:
        valorQR: El texto del código QR.
    """
    valorQR = input("Introduzca el texto del código QR: ")
    cls()
    opc_usuario = 6
    cls()
    imagenQR = obtener_nombre()
    cls()
    crear_qr(valorQR, opc_usuario, imagenQR)
    cls()
    msg_listo()

def codigo_personalizado():
    """Genera un código QR con el texto especificado y el formato personalizado seleccionado por el usuario.

    Args:
        valorQR: El texto del código QR.
        opc_usuario: El formato del código QR seleccionado por el usuario.
        imagenQR: El nombre del archivo del código QR.
    """
    valorQR = input("Introduzca el texto del código QR: ")
    cls()
    print("Tipo de QR:\n1. Círculo\n2. Cuadrado\n3. Barra vertical\n4. Barra Horizontal\n5. Redondeado\n6. Cuadrado Grande (clásico)\n")
    opc_usuario = opcion("¿Qué opción eliges? (Ingresa el número correspondiente):\n> ", [1, 2, 3, 4, 5, 6])
    cls()
    imagenQR = input("¿Nombre del QR?\n> ") + ".png"
    cls()
    crear_qr(valorQR, opc_usuario, imagenQR)
    cls()
    msg_listo()