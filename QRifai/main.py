import cv2
from modulos.crear_qr import crear_qr
from modulos.leer_qr import (
    obt_ruta_qr, 
    leer_qr
)
from modulos.sistema import (
    cls, 
    msg_listo, 
    obtener_nombre, 
    separador as sp
)

def opcion(respuesta, opcion_valida): # Evitamos la repetición de codigo al crear funcion para la opcion del usuario
    while True:
        try:
            opcion = int(input(respuesta))
            if opcion in opcion_valida: # Bucle para verificar que la opcion del usuario sea corecta...
                return opcion
            else: #... caso contrario se repite la pregunta
                cls()
        except ValueError:
            cls()

def main():
    while True:
        cls()
        opcion_usuario = opcion( # Llamamos la funcion de opcion
            "Elige una opcion ingresando el numero correspondiente:\n1. Crear codigo QR\n2. Leer codigo QR\n3. Salir\n\n> ", 
            [1, 2, 3]
            )
        if opcion_usuario == 1: # Iniciamos todo el bloque de creacion de codigos QR
            while True:
                cls() 
                opcion_usuario = opcion("Elige una opcion para crear el QR \n(Ingresa el numero corespondiente):\n1. QR Clasico\n2. QR Personalizado\n3. Salir\n\n> ", [1, 2, 3])
                cls()
                if opcion_usuario == 1: # Crear QR Clasico, solo pidiendo el texto a convertir
                    valorQR = input("Introduzca el texto del código QR: ")
                    cls()
                    opc_usuario = 6 # Fijamos el diseño de Cuadrado Grande
                    cls()
                    imagenQR = obtener_nombre() # Crear nombre con la hora del usuario
                    cls()
                    crear_qr(valorQR, opc_usuario, imagenQR)
                    cls()
                    msg_listo()
                elif opcion_usuario == 2: # Crear QR pidiendo al usuario el texto a convertir, nombre y diseño
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
                else: # Opcion "salir" y regresamos al menú
                    break
                respuesta = input("¿Deseas hacer otro codigo QR (Y/N)? ").strip().lower() # Pregunta para repetir bloque, o salir a menu
                if respuesta != 'y':
                    break
        elif opcion_usuario == 2: # Iniciamos bloque de lectura de QR
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
        else: # Opcion "Salir" para cerrar programa
            break

if __name__ == "__main__":
    main()