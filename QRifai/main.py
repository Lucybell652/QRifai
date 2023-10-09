from modulos.crear_qr import crear_qr
from modulos.sistema import cls, final, obtener_nombre

def opcion(respuesta, opcion_valida):
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
        opcion_usuario = opcion("Elige una opcion para crear el QR \n(Ingresa el numero corespondiente):\n1. QR Clasico\n2. QR Personalizado\n3. Salir\n\n> ", [1, 2, 3])
        cls()
        if opcion_usuario == 1:
            valorQR = input("Introduzca el texto del código QR: ")
            cls()
            opc_usuario = 6 # Predeterminamos el diseño de Cuadrado Grande
            cls()
            imagenQR = obtener_nombre() # Crear nombre con la hora del usuario
            cls()
            crear_qr(valorQR, opc_usuario, imagenQR)
            cls()
            final()
        elif opcion_usuario == 2:
            valorQR = input("Introduzca el texto del código QR: ")
            cls()
            print("Tipo de QR:\n1. Círculo\n2. Cuadrado\n3. Barra vertical\n4. Barra Horizontal\n5. Redondeado\n6. Cuadrado Grande (clásico)\n")
            opc_usuario = opcion("¿Qué opción eliges? (Ingresa el número correspondiente):\n> ", [1, 2, 3, 4, 5, 6])
            cls()
            imagenQR = input("¿Nombre del QR?\n> ") + ".png"
            cls()
            crear_qr(valorQR, opc_usuario, imagenQR)
            cls()
            final()
        else:
            break

        respuesta = input("¿Deseas hacer otro codigo QR (Y/N)? ").strip().lower()
        if respuesta != 'y':
            break

if __name__ == "__main__":
    main()