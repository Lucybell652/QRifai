
# QRifai (⁠ﾉ⁠◕⁠ヮ⁠◕⁠)⁠ﾉ⁠*⁠.⁠✧

Este programa te permite generar códigos QR personalizados o clásicos de forma sencilla. Puedes elegir el contenido del código QR y su estilo. 
También puedes generar múltiples códigos QR en una sola ejecución del programa.

## Requisitos 📜

Para ejecutar este programa, asegúrate de tener instalado Python en tu sistema. Además, necesitas tener los siguientes módulos Python instalados:

- `Pillow`: Utilizado para crear la imagen del código QR.
- `qrcode`: Utilizado para generar el código QR.

Puedes instalar estos módulos utilizando `pip`:

```bash
pip install Pillow qrcode
```

## Uso 💻

1. Ejecuta el programa desde la línea de comandos:

```bash
python main.py
```

2. El programa te preguntará si deseas generar un código clásico o personalizado.

3. Si eliges un código clásico, ingresa el texto que deseas codificar en el código QR. El programa generará automáticamente un código QR y lo guardará en un archivo PNG.

4. Si eliges un código personalizado, ingresa el texto y elige un estilo para el código QR entre las opciones disponibles:
   * Círculo
   * Cuadrado
   * Barra vertical
   * Barra horizontal
   * Redondeado
   * Cuadrado grande (clásico).
6. También puedes especificar un nombre personalizado para el archivo de imagen QR.

6. El programa generará el código QR personalizado y lo guardará en un archivo PNG.

7. Puedes generar más códigos QR o salir del programa según tu elección.

## Futuras actualizaciones ✨

1. Leer códigos QR
2. Solicitar al usuario una ruta personalizada dónde guardar los códigos
3. Interfaz gráfica