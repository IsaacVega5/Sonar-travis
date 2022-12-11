Integración Travis CI con Sonar CLoud
========================

## Introducción
Este es un repositorio de pruebas para ser usado en un trabajo universitario

## Detalles
Este código incluye dos carpetas tres carpetas principales: app, tests, reports  

Estas carpetas contienen lo siguiente:
### app
Contiene la aplicación en general, tanto las funciones **"fun.py"**, como dos archivos .py independientes, el uno del otro. Uno de ellos **"app.py"** permite llamar a las funciones pero a través de la consola, el otro archivo "gui.py" hace lo mismo, pero a través de una interfaz grafica generada con la biblioteca Tkinter, incluyendo una carpeta "assets" con todo lo necesario para que está funcione.

### test
Contiene un archivo python que ejecuta pruebas unitarias que testean el archivo "fun.py", dichas pruebas luego son llamadas por el archivo **".travis.yml"** que se encuentra en la carpeta raiz.

### reports
incluye el archivo **"coverage.xml"** que le permite a **Sonar**, verificar el código para saber si está listo o no para producción.