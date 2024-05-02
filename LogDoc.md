# Clase Log

## Información General
- **Autor**: Álvaro Villar Val
- **Fecha**: 05/03/24
- **Versión**: 1.0.0
- **Descripción**: 
  - Esta clase se encarga de gestionar el registro de eventos (log) de la aplicación. Permite añadir mensajes de error al archivo de log y limpiar el contenido del archivo de log.

## Métodos

### `__init__(self)`
Constructor de la clase. Inicializa la clase con el siguiente atributo:
- `fichero`: Nombre del archivo de log utilizado por los métodos de la clase. Por defecto, se establece en `"log.txt"`.

### `injeErr(self, error)`
Añade un mensaje de error al archivo de log.
- **Parámetros**:
  - `error`: Cadena de texto que contiene el mensaje de error a registrar.
- **Comportamiento**:
  - Abre el archivo de log en modo append (`"a"`) para agregar el mensaje de error al final del archivo.
  - Cierra el archivo tras añadir el mensaje.

### `limpiarLog(self)`
Limpia el contenido del archivo de log.
- **Comportamiento**:
  - Abre el archivo de log en modo escritura (`"w"`), lo cual borra todo contenido previo del archivo.
  - Cierra el archivo después de limpiarlo.
