# Programa para el Cálculo de Impuestos

Este programa calcula el total de impuestos y el precio total de un artículo o una compra compuesta por varios artículos, teniendo en cuenta diferentes tipos de impuestos aplicables según las normativas colombianas.

## Funciones

### `calculate_item_total(price, quantity, tax_type)`

Calcula el total de impuestos y el precio total de un solo artículo.

- **Parámetros de entrada**:
  - `price`: Precio unitario del artículo.
  - `quantity`: Cantidad de artículos.
  - `tax_type`: Tipo de impuesto (porcentaje, fijo, o "exempt" para exento).

- **Proceso**:
  - Calcula impuestos según el tipo especificado.
  - Devuelve el total de impuestos y el precio total.

- **Salida**:
  - Tupla con el total de impuestos y el precio total del artículo.

### `calculate_total_purchase(items)`

Calcula el total de impuestos y el precio total de una compra con múltiples artículos.

- **Parámetros de entrada**:
  - `items`: Lista de tuplas, cada una con `(precio_unitario, cantidad, tipo_impuesto)`.

- **Proceso**:
  - Itera sobre cada artículo y suma impuestos y precios totales.

- **Salida**:
  - Tupla con el total de impuestos y el precio total de la compra.

## Requisitos

- Python 3.12 o superior.
- Kivy 2.1.0 o superior

# Instalación de Kivy en Windows

Kivy es un marco de trabajo de código abierto diseñado para crear aplicaciones multitáctiles que son compatibles con diversas plataformas, incluida Windows. A continuación, se presentan los pasos para instalar Kivy en un sistema operativo Windows.

## Requisitos Previos

Asegúrate de tener Python instalado. Puedes descargarlo desde [python.org](https://www.python.org/).

## Pasos para la Instalación

### 1. Actualiza pip y herramientas asociadas
Abre la terminal de comandos como administrador y ejecuta:
```bash
python -m pip install --upgrade pip wheel setuptools
```
### Paso 2: Instalar las dependencias de Kivy

Para garantizar que Kivy funcione adecuadamente en tu sistema, es necesario instalar ciertas dependencias. Abre la terminal de comandos con privilegios de administrador y ejecuta el siguiente comando para instalar estas dependencias esenciales:

```bash
python -m pip install docutils pygments pypiwin32 kivy_deps.sdl2 kivy_deps.glew kivy_deps.gstreamer
```
### Paso 3: Instalar Kivy

Después de haber instalado todas las dependencias necesarias, puedes continuar con la instalación de Kivy. Este potente framework facilita el desarrollo de aplicaciones multitáctiles y multiplataforma. Para instalar Kivy, abre la terminal de comandos con privilegios de administrador y ejecuta el siguiente comando:

```bash
pip install kivy
```

## Instalación y Ejecución

1. **Clona el repositorio a tu máquina local**:
   ```bash
   git clone https://github.com/JHONCE79/Codigo-Limpio.git

2. Navega al directorio del proyecto:
   ```
   cd Codigo-Limpio/
   ```
3. Ejecutar el programa en la interfaz:
   ```
   python src/console/interface.py

   ```

# instrucciones para ejecutar los casos de prueba

Proporciona instrucciones claras sobre cómo instalar y configurar el proyecto. Por ejemplo:
1. Clona el repositorio a tu máquina local:
   ```
   git clone https://github.com/JHONCE79/Codigo-Limpio.git
   ```
2. Navega al directorio del proyecto:
   ```
   cd Codigo-Limpio/
   ```
3. Ejecutar casos de prueba:
   ```
   python test/TaxesTests.py
   ```

## Licencia MIT

Copyright (c) 2024 JHONCE79

Se concede permiso, de forma gratuita, a cualquier persona que obtenga una copia
de este software y los archivos de documentación asociados (el "Software"), para tratar
en el Software sin restricciones, incluidos, entre otros, los derechos
utilizar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar y / o vender
copias del Software, y permitir a las personas a quienes se les proporcione el Software lo hagan
lo mismo, sujeto a las siguientes condiciones:

El aviso de derechos de autor anterior y este aviso de permiso se incluirán en todos
copias o partes sustanciales del Software.

EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O
IMPLÍCITO, INCLUYENDO PERO NO LIMITADO A LAS GARANTÍAS DE COMERCIABILIDAD,
ADECUACIÓN PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO
LOS AUTORES O TITULARES DE LOS DERECHOS DE AUTOR SERÁN RESPONSABLES DE NINGÚN RECLAMO, DAÑO U OTRO
RESPONSABILIDAD, YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O DE OTRO MODO, DERIVADO DE,
FUERA DE O EN CONEXIÓN CON EL SOFTWARE O EL USO U OTROS NEGOCIOS EN EL