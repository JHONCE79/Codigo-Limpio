# Funciones simuladas para calcular el total de un item y el total de una compra
def calcular_total_item(precio_unitario, cantidad, impuestos):
    if precio_unitario < 0 or cantidad < 0:
        raise ValueError("Precio unitario o cantidad no pueden ser negativos.")

    if impuestos == "exento" or impuestos == "excluido":
        total_impuestos = 0
    else:
        total_impuestos = precio_unitario * cantidad * impuestos / 100

    total_item = precio_unitario * cantidad + total_impuestos
    return total_impuestos, total_item


def calcular_total_compra(items):
    total_impuestos = 0
    total_compra = 0

    for item in items:
        precio_unitario, cantidad, impuestos = item
        impuestos_item, total_item = calcular_total_item(precio_unitario, cantidad, impuestos)
        total_impuestos += impuestos_item
        total_compra += total_item

    return total_impuestos, total_compra