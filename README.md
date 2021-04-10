[![IssuesOpen][issuesOpen-shield]][issuesOpen-url]
[![IssuesClosed][issuesClosed-shield]][issuesClosed-url]
[![lastDate][lastDate-shield]][lastDate-url]
# Proyecto Lambda λ

## Introducción
El presente documento tiene por objeto realizar la función de guía sobre el proyecto lambda, asignado como parte del grupo de trabajo de la asignatura Procesos de la Ingeniería del Software 2 al alumno Jose María Morales Miñarro.

Este repositorio contiene los archivos de un software preparado para la realización de las operaciones del Álgebra de Allen orientadas a intervalos temporales. En nuestro caso, trabajamos simplemente con la unidad más básica, segundos, mas posibles implementaciones de otras unidades temporales podrían incluirse en futuras actualizaciones.

## Herramientas utilizadas
Las herramientas de las que se ha hecho uso para la realización del proyecto son:
* [Visual Studio Code](https://code.visualstudio.com/)
* [Extensión de Python para Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
* [Python](https://www.python.org/)

## Paso 1: Instalando el proyecto
Para poder empezar a utilizar el proyecto, lo primero es completar su instalación. Hay dos métodos principales por los que se puede realizar dicho proceso:

### Método 1: Descarga manual

### Método 2: Descarga desde consola
Para ello, si trabajamos en Windows, deberemos de hacer uso de alguna herramienta especial como [Git Bash](https://gitforwindows.org/), paso que podemos saltar si trabajamos en Linux.

Haciendo uso de nuestra consola, nos ubicaremos en la posición en la que queramos clonar el repositorio con todos sus archivos, y escribiremos la siguiente línea:

```sh
   $ git clone https://github.com/PRIS2/lambda.git
   ```
Con esto, ya tendremos los archivos descargados en nuestro equipo.

## Paso 2: Ejecutar el archivo de tests/archivo propio
Si queremos comprobar la funcionalidad, lo más recomendado es usar el archivo para pruebas que ya viene incluido en el repositorio. En caso de que se quiera utilizar de otra forma, se puede crear un archivo .py a parte, e importar las clases intervalo.py y constantes.py añadiendo las siguientes líneas al comienzo del nuevo archivo:

```sh
   import constantes
   from intervalo import intervalo
   ```
En cualquier caso, para poder ejecutar el archivo de test, estando en la ubicación correcta con nuestra consola, ejecutaremos la siguiente orden:

```sh
   $ python3 test_intervalo.py
   ```
Por otro lado, si estamos haciendo uso de alguna herramienta como [Visual Studio Code](https://code.visualstudio.com/) compatible con Python, con la cual se modifiquen o construyan nuevos archivos .py, la ejecucción se simplifica; tan solo será necesario seleccionar el archivo .py a ejecutar, y se pulsará sobre el triángulo/flecha de color verde.

## Desarrollo
Para obtener más información sobre el desarrollo del software se recomienda revisar:
* [Listado de issues del proyecto](https://github.com/PRIS2/lambda/issues)
* [Historial de commits del proyecto](https://github.com/PRIS2/lambda/commits/main)

## Contacto
Jose María Morales Miñarro - jmm497@inlumine.ual.es


[issuesOpen-shield]: https://img.shields.io/github/issues-raw/PRIS2/lambda
[issuesClosed-shield]: https://img.shields.io/github/issues-closed-raw/PRIS2/lambda
[issuesOpen-url]: https://github.com/PRIS2/lambda/issues
[issuesClosed-url]: https://github.com/PRIS2/lambda/issues?q=is%3Aissue+is%3Aclosed

[lastDate-shield]: https://img.shields.io/github/last-commit/PRIS2/lambda
[lastDate-url]: https://github.com/PRIS2/lambda/commits/main
