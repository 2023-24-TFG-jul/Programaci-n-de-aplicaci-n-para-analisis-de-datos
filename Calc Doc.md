# Calculadora de Criterios de Calidad para la Central Meteorológica

## Información General

- **Nombre**: Calculadora
- **Autor**: Álvaro Villar Val
- **Fecha**: 26/03/24
- **Versión**: 0.2.3
- **Descripción**: Calculadora de los diferentes criterios de calidad de la central meteorológica.

## Dependencias

Este código depende de las siguientes librerías:

- `pysolar.solar`
- `datetime`
- `math`

## Clase Calculadora

### Variables de Clase

La clase `Calculadora` incluye las siguientes variables de clase, que representan constantes y parámetros utilizados en los cálculos:

- `dni0`: Irradiancia normal directa en W/m².
- `dnil0`: Iluminancia normal directa en lux.
- `dnp0`: PAR (Radiación fotosintéticamente activa) normal directa en W/m².
- `dnuv0`: UV (Ultravioleta) normal directa en W/m².
- `ghiclear`, `dniclear`: Parámetros para condiciones de cielo claro que están pendientes de encontrar.
- `latitude`, `longitude`: Coordenadas de la ubicación para la cual se realizan los cálculos.
- `m`: Masa de aire óptica relativa, pendiente de encontrar.

### Métodos

#### `dates(self, fecha)`
Convierte una cadena de texto en formato de fecha a un objeto `datetime`.

#### Métodos de Comprobación Física

- `physGen1(self, value, altitude, numFin, dn0, numIni, min)`: Comprueba los límites físicos generales para GH y DH.
- `physGen2(self, value, dn0, min)`: Comprueba los límites físicos generales para DN.

#### Métodos de Coherencia

- `coheGen1(self, gh, dh, dn, angle, max, min, valueMin)`: Método genérico de coherencia para irradiancia.
- `coheGen2(self, gh, dh, max, valueMin)`: Método genérico de coherencia para iluminancia y PAR.

#### Método de Comprobación de Criterios de Calidad

- `comprobar(self, valuePrin, funPhys, funSky, cohe1, cohe2, cohe3, cohe4, valueGH, valueDH, valueDN, fecha)`: Comprueba los criterios de calidad para los distintos tipos de irradiancia e iluminancia, invocando los métodos correspondientes de comprobación física, de cielo claro y de coherencia.

### Métodos Específicos de Criterios de Calidad

Para cada tipo de medida (GHI, DHI, DNI, GHIL, DHIL, DNIL, GHP, DHP, DNP, GHUV, DHUV, DNUV), existen métodos específicos para comprobar sus criterios de calidad. Estos métodos utilizan el método `comprobar` pasando los parámetros apropiados para cada tipo de medida.

## Uso

Para utilizar esta calculadora, se debe crear una instancia de la clase `Calculadora` y llamar a los métodos correspondientes a la medida que se desea evaluar, pasando los valores necesarios como argumentos.
