import os
import qrcode
from modulos.func_para_qr import ruta_fin_qr
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
    carpeta_qr = ruta_fin_qr()  # Obtener la carpeta de destino
    imagenQR = os.path.join(carpeta_qr, imagenQR)  # Agregar la carpeta de destino a la ruta de la imagen
    
    # Preparamos el formato para el código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Aplicamos el valor al objeto QR
    qr.add_data(valorQR)

    # Establecemos el tipo de QR según la opción seleccionada por el usuario
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

    # Generamos el código QR y lo almacenamos en el fichero de imagen PNG
    img = qr.make_image(image_factory=StyledPilImage, module_drawer=tipoQRC)
    f = open(imagenQR, "wb")
    img.save(f)