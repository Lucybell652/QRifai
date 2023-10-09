import argparse
import cv2

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--fichero", type=str, 
        help="Ruta y nombre del fichero de imagen QR a leer")
    return parser.parse_args()
    
def obt_ruta_qr():
    args = parse_arguments()
    if args.fichero:
        return args.fichero
    else:
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