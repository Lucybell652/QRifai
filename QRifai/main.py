from modulos.crear_qr import crear_qr
from modulos.sistema import cls, final
from modulos.func_para_qr import obtener_nombre

def main():
    while True:
        while True:
            cls() 
            opc_principal = input("¿Quieres un código clásico o personalizado?\n1. Código clásico\n2. Código personalizado\n> ")
            
            if opc_principal == '1' or opc_principal == '2':
                opc_principal = int(opc_principal)
                break
            else:
                cls()

        cls()

        if opc_principal == 1:
            valorQR = input("Introduzca el texto del código QR: ")
            cls()

            opc_usuario = 6
            cls()

            imagenQR = obtener_nombre()
            cls()

            crear_qr(valorQR, opc_usuario, imagenQR)
            cls()
            final()

        if opc_principal == 2:
            # Obtenemos el valor del código QR
            valorQR = input("Introduzca el texto del código QR: ")
            cls()

            # Solicitamos al usuario que elija una opción para el tipo de QR
            while True:
                print("Tipo de QR:\n1. Círculo\n2. Cuadrado\n3. Barra vertical\n4. Barra Horizontal\n5. Redondeado\n6. Cuadrado Grande (clásico)\n")
                opc_usuario = input("¿Qué opción eliges? (Ingresa el número correspondiente):\n> ")

                if opc_usuario in ['1', '2', '3', '4', '5', '6']:
                    opc_usuario = int(opc_usuario)
                    break
                else:
                    cls()
                cls()

            # Obtenemos el nombre del archivo de imagen QR
            cls()
            imagenQR = input("¿Nombre del QR?\n> ") + ".png"
            cls()

            crear_qr(valorQR, opc_usuario, imagenQR)
            cls()
            final()

        respuesta = input("¿Desea hacer un nuevo QR? Presione \"Y\"\nPara cerrar presione cualquier letra:\n> ").lower()
        if respuesta == 'y':
            main()
        else:
            break

if __name__ == "__main__":
    main()