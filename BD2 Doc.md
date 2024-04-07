
# BaseDatosLvl2

## Descripción
`BaseDatosLvl2` es parte de un sistema de base de datos para una central meteorológica en la Universidad de Burgos. Esta clase se encarga de manejar las operaciones de nivel intermedio con los datos meteorológicos, incluyendo la actualización y procesamiento de datos recopilados de diferentes fuentes como radiosondas, cámaras del cielo, y escáneres de cielo.

## Autor
Álvaro Villar Val

## Fecha de Creación
20 de febrero de 2024

## Versión
0.5.0

## Requisitos
- Python 3.x
- SQLAlchemy
- Pandas
- BaseDatosLvl1 (una clase personalizada que gestiona la base de datos de primer nivel)
- Calculadora (una clase personalizada para realizar operaciones específicas con los datos)

## Uso
Para utilizar esta clase, primero asegúrate de tener instaladas todas las dependencias y haber creado las clases `BaseDatosLvl1` y `Calculadora` mencionadas en los requisitos. Después, puedes crear una instancia de `BaseDatosLvl2` de la siguiente manera:

```python
from BaseDatosLvl2 import BaseDatosLvl2

db_lvl2 = BaseDatosLvl2()
```

### Funciones Principales

#### `__init__(self)`
Constructor de la clase. Inicializa la conexión con la base de datos y crea las tablas necesarias si no existen.

#### `crear(self)`
Crea las tablas en la base de datos para los datos procesados si aún no existen.

#### `actualizarImg(self)`
Actualiza las imágenes en la base de datos a partir de los datos obtenidos de la base de datos de primer nivel.

#### `descImg(self, date1, date2)`
Descarga imágenes de la base de datos dentro de un rango de fechas especificado.

#### `descdat(self, selec, base, cond1, cond2)`
Permite la descarga de datos específicos de la base de datos basándose en los parámetros proporcionados.

#### `actualizardatos(self)`
Actualiza y procesa los datos recién insertados en la base de datos de primer nivel, moviéndolos a la base de datos de segundo nivel.

#### `stop(self)`
Cierra las conexiones a la base de datos. Debe usarse al finalizar el programa para evitar errores en las conexiones futuras.

## Descripción de las Dependencias

### SQLAlchemy
SQLAlchemy es un toolkit de SQL y ORM para Python que permite a los desarrolladores utilizar bases de datos de manera más eficiente y segura mediante el uso de modelos de datos de alto nivel.

### Pandas
Pandas es una librería de Python que proporciona estructuras de datos y herramientas de análisis de datos diseñadas para hacer el trabajo con datos estructurados o tabulares tanto fácil como intuitivo.

## Notas
Este sistema forma parte de un proyecto más grande de la Universidad de Burgos, destinado a mejorar la recopilación y análisis de datos meteorológicos para fines de investigación y educación.
