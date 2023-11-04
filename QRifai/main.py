from modulos.leer_qr import opc_leer_qr
from modulos.sistema import (
    cls,
    opcion
)
from modulos.crear_qr import (
    codigo_personalizado,
    codigo_predeterminado
)

def main():
    while True:
        cls()
        opcion_usuario = opcion(
            "Elige una opcion ingresando el numero correspondiente:\n1. Crear codigo QR\n2. Leer codigo QR\n3. Salir\n\n> ", 
            [1, 2, 3]
            )
        if opcion_usuario == 1: # Iniciamos todo el bloque de creacion de codigos QR
            while True:
                cls() 
                opcion_usuario = opcion("Elige una opcion para crear el QR \n(Ingresa el numero corespondiente):\n1. QR Clasico\n2. QR Personalizado\n3. Salir\n\n> ", [1, 2, 3])
                cls()
                if opcion_usuario == 1: # Crear QR Clasico, solo pidiendo el texto a convertir
                    codigo_predeterminado()
                elif opcion_usuario == 2: # Crear QR pidiendo al usuario el texto a convertir, nombre y diseño
                    codigo_personalizado()
                else: # Opcion "salir" y regresamos al menú
                    break
                respuesta = input("¿Deseas hacer otro codigo QR (Y/N)? ").strip().lower() # Pregunta para repetir bloque, o salir a menu
                if respuesta != 'y':
                    break
        elif opcion_usuario == 2: # Iniciamos bloque de lectura de QR
            opc_leer_qr()
            respuesta = input("¿Deseas revisar otro codigo QR (Y/N)? ").strip().lower()
            if respuesta != "y":
                break
        else:
            break

if __name__ == "__main__":
    main()