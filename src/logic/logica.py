def calcular_total_item(precio_unitario, cantidad, tipo_impuesto):
    """
    Calcula el total de impuestos y el precio total de un artículo.
    
    :param precio_unitario: Precio unitario del artículo (en pesos).
    :param cantidad: Cantidad del artículo.
    :param tipo_impuesto: Tipo de impuesto aplicable (puede ser IVA, INC, o "exento").
    :return: Una tupla con el total de impuestos y el precio total.
    """
    
    # Verificar que los valores de precio y cantidad sean positivos
    if precio_unitario <= 0 or cantidad <= 0:
        raise ValueError("El precio y la cantidad deben ser positivos y mayores a cero.")
    
    # Inicializar el total de impuestos
    total_impuestos = 0

    # Calcular el impuesto según el tipo
    if tipo_impuesto == "exento":
        total_impuestos = 0
    elif tipo_impuesto == "fijo":
        total_impuestos = 66 * cantidad
    elif isinstance(tipo_impuesto, (int, float)):
        # Aplica el porcentaje del impuesto al precio unitario
        total_impuestos = precio_unitario * cantidad * (tipo_impuesto / 100)
    else:
        raise TypeError("El tipo de impuesto debe ser un número, 'fijo' o 'exento'.")

    # Calcular el precio total del artículo
    precio_total = precio_unitario * cantidad + total_impuestos
    
    return total_impuestos, precio_total

def calcular_total_compra(items):
    """
    Calcula el total de impuestos y el precio total de una compra con múltiples artículos.
    
    :param items: Una lista de tuplas, cada una con (precio_unitario, cantidad, tipo_impuesto).
    :return: Una tupla con el total de impuestos y el precio total.
    """
    total_impuestos = 0
    precio_total = 0
    
    for item in items:
        # Desempaquetar los valores de cada artículo
        precio_unitario, cantidad, tipo_impuesto = item
        # Calcular los impuestos y el precio total de cada artículo
        item_impuestos, item_total = calcular_total_item(precio_unitario, cantidad, tipo_impuesto)
        # Sumar al total acumulado
        total_impuestos += item_impuestos
        precio_total += item_total
    
    return total_impuestos, precio_total