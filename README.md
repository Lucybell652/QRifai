
# QRifai (⁠ﾉ⁠◕⁠ヮ⁠◕⁠)⁠ﾉ⁠*⁠.⁠✧

Este programa te permite generar códigos QR personalizados o clásicos de forma sencilla. Puedes elegir el contenido del código QR y su estilo. 
También puedes generar múltiples códigos QR en una sola ejecución del programa.

## Requisitos 📜

Para ejecutar este programa, asegúrate de tener instalado Python en tu sistema. Además, necesitas tener las siguientes libterias instalados:

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
2. Te dará 3 opciones:
   * Crear codigo QR
   * Leer codigo QR
   * Salir

3. Si eliges la primera opcioon, te preguntará si deseas generar un código clásico o personalizado.

3. Si eliges un código clásico, solo deberás de ingresa el texto que deseas codificar. El programa generará automáticamente un
código QR y lo guardará en un archivo PNG.

5. Si eliges un código personalizado, ingresa el texto y elige un estilo para el código QR entre las opciones disponibles:
   * Círculo
   * Cuadrado
   * Barra vertical
   * Barra horizontal
   * Redondeado
   * Cuadrado grande (clásico).
6. También puedes especificar un nombre personalizado para el archivo de imagen QR, y lo guardará en formato PNG.
7. Puedes generar más códigos QR o salir al menú según tu elección.
9. Si eligues la segunda opcion del menú (leer QR), te pedirá la ruta donde está guardado el codigo QR a leer.
10. Al final mostará una pantalla con el texto del codigo, y podrás leer otro QR o salir al Menu
11. Si eliges la opcion "Salir", se cerrará el programa.

## Futuras actualizaciones ✨

1. Solicitar al usuario una ruta personalizada dónde guardar los códigos
2. Interfaz gráfica
