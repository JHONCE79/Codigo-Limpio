


# Programa para el Cálculo de Impuestos

Este programa está diseñado para calcular el total de impuestos y el precio total de un artículo o una compra compuesta por varios artículos, teniendo en cuenta los diferentes tipos de impuestos aplicables.

## Función `calcular_total_item(precio_unitario, cantidad, tipo_impuesto)`

Esta función se encarga de calcular el total de impuestos y el precio total de un único artículo basado en su precio unitario, cantidad y tipo de impuesto.

- **Parámetros de entrada**:
    - `precio_unitario`: Es el precio por unidad del artículo.
    - `cantidad`: Es el número de unidades del artículo que se compran.
    - `tipo_impuesto`: Puede ser un porcentaje (como 5% o 19% de IVA), un impuesto fijo, o "exento" si el artículo no está sujeto a impuestos.

- **Proceso**:
    - Se asegura que tanto el `precio_unitario` como la `cantidad` sean mayores que cero para evitar cálculos inválidos.
    - Calcula los impuestos basados en el `tipo_impuesto`:
        - Si el artículo está "exento", no se cobra ningún impuesto.
        - Si el tipo de impuesto es "fijo", se aplica un valor de 66 pesos por cada unidad.
        - Si es un porcentaje, se calcula el impuesto multiplicando el precio unitario, la cantidad y el porcentaje dividido entre 100.
    - Se calcula el precio total del artículo sumando el precio sin impuestos y el total de impuestos.

- **Salida**:
    - Devuelve una tupla con el total de impuestos y el precio total del artículo, incluyendo impuestos.

## Función `calcular_total_compra(items)`

Esta función es una extensión de la primera y permite calcular los impuestos y el precio total de una compra con múltiples artículos.

- **Parámetros de entrada**:
    - `items`: Es una lista de tuplas. Cada tupla contiene el `precio_unitario`, la `cantidad`, y el `tipo_impuesto` de un artículo.

- **Proceso**:
    - Itera sobre cada artículo de la lista `items`.
    - Para cada artículo, llama a la función `calcular_total_item` para obtener los impuestos y el precio total del artículo.
    - Suma los impuestos y precios totales de todos los artículos de la compra.

- **Salida**:
    - Devuelve una tupla con el total de impuestos y el precio total de la compra.
    - 
## Requisitos Previos

Asegúrate de tener Python instalado. Puedes descargarlo desde [python.org](https://www.python.org/).

# instrucciones para ejecutar el programa 

1. Clona el repositorio a tu máquina local:
   ```
   git clone https://github.com/JHONCE79/Codigo-Limpio.git
   ```
2. Navega al directorio del proyecto:
   ```
   cd Codigo-Limpio/
   ```
3. Ejecutar el programa en la interfaz:
   ```
   python src/console/interfaz.py

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
   python test/ImpuestosTests.py
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
