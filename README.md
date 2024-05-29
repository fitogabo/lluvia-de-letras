# 🌦️🔡 Lluvia de letras
Videojuego donde van cayendo letras y al presionarlas en el teclado desaparecen

## Aprendizaje y Mecanografía

Este videojuego está diseñado para ayudar a los niños a aprender Python y mejorar sus habilidades de mecanografía. Las letras caen desde la parte superior de la pantalla y el jugador debe presionar la tecla correspondiente en el teclado para hacerlas desaparecer. Esto ayuda a los niños a familiarizarse con la ubicación de las teclas en el teclado y a mejorar su velocidad y precisión al tipear.

## Fonoaudiología y Aprendizaje de Lectura y Escritura

Además de mejorar las habilidades de mecanografía, el juego también ayuda con la fonoaudiología y los métodos de aprendizaje para aprender a leer y escribir. Cada vez que aparece una letra cayendo en la pantalla, el juego reproduce el sonido de esa letra, no su nombre, sino cómo suena en palabras. Esto puede ayudar a los niños a asociar los sonidos con las letras y mejorar su habilidad para leer y escribir.

## Rango de Edad

Este juego es adecuado para niños que están aprendiendo a leer y escribir, generalmente entre las edades de 5 y 9 años. Sin embargo, los niños de todas las edades pueden disfrutar del juego y beneficiarse de la práctica de mecanografía y la asociación de sonidos con letras.

## Compilación

Este juego puede ser compilado en un archivo ejecutable utilizando PyInstaller, una herramienta que congela (empaqueta) aplicaciones Python en archivos ejecutables independientes. 

Para instalar PyInstaller, puedes usar pip, el administrador de paquetes de Python. Ejecuta el siguiente comando en tu terminal:

```bash
pip install pyinstaller
```
Una vez que PyInstaller esté instalado, puedes compilar el juego utilizando el siguiente comando:

```bash
pyinstaller --onefile --add-data 'sonidos/*;sonidos/' lluvia-de-letras.py
```
Este comando creará un archivo ejecutable en la carpeta dist.

Importante: Después de la compilación, debes copiar manualmente el directorio de la carpeta "sonidos" al mismo lugar donde se encuentra el archivo ejecutable. Esto es necesario porque el juego necesita acceder a estos archivos de sonido para funcionar correctamente.