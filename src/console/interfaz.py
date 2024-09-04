import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logic.logica import calcular_total_item, calcular_total_compra 

def mostrar_menu():
    opciones = [
        "--- Menú de Cálculo de Impuestos ---",
        "1. Calcular Total Item",
        "2. Calcular Total Compra",
        "3. Salir"
    ]
    print("\n" + "\n".join(opciones))

def mostrar_menu_impuestos():
    impuestos = [
        "--- Tipos de Impuestos ---",
        "1. Vehículo mayor a 200cc (8%)",
        "2. Licores con grado de alcohol menor al 35% (25%)",
        "3. Licores con grado de alcohol superior al 35% (40%)",
        "4. Vinos y aperitivos menor al 14% de grado de alcohol (20%)",
        "5. Vinos y aperitivos superior al 14% de grado de alcohol (20%)",
        "6. Cargo por bolsas plásticas (66 COP por bolsa)",
        "7. IVA:",
        "   - Tasa general (19%)",
        "   - Tasa reducida (5%)",
        "   - Exento o Excluido"
    ]
    print("\n" + "\n".join(impuestos))

def obtener_tipo_impuesto():
    mostrar_menu_impuestos()
    opcion_impuesto = input("Seleccione el tipo de impuesto (1-7): ").strip()

    impuestos = {
        '1': 8,
        '2': 25,
        '3': 40,
        '4': 20,
        '5': 20,
        '6': "fijo",
        '7': obtener_tipo_iva
    }

    if opcion_impuesto in impuestos:
        if opcion_impuesto == '7':
            return impuestos[opcion_impuesto]()
        return impuestos[opcion_impuesto]
    else:
        raise ValueError("Opción de impuesto inválida.")

def obtener_tipo_iva():
    subopcion = input("Seleccione: 1 para tasa general (19%), 2 para tasa reducida (5%), o 3 para Exento o Excluido: ").strip()
    iva = {
        '1': 19,
        '2': 5,
        '3': obtener_exento_excluido
    }
    if subopcion in iva:
        if subopcion == '3':
            return iva[subopcion]()
        return iva[subopcion]
    else:
        raise ValueError("Opción inválida para IVA.")

def obtener_exento_excluido():
    subsubopcion = input("¿Exento o Excluido? (e para Exento, x para Excluido): ").strip().lower()
    opciones = {
        'e': 'exento',
        'x': 'excluido'
    }
    if subsubopcion in opciones:
        return opciones[subsubopcion]
    else:
        raise ValueError("Opción inválida para Exento o Excluido.")

def obtener_datos_item():
    try:
        precio_unitario = float(input("Ingrese el precio unitario del artículo (en pesos): "))
        cantidad = int(input("Ingrese la cantidad del artículo: "))
        tipo_impuesto = obtener_tipo_impuesto()
        return precio_unitario, cantidad, tipo_impuesto
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

def obtener_datos_compra():
    items = []
    print("Ingrese los datos para cada artículo. Escriba 'fin' para terminar.")
    
    while True:
        try:
            print("\n--- Artículo ---")
            precio_unitario = float(input("Ingrese el precio unitario del artículo (en pesos): "))
            cantidad = int(input("Ingrese la cantidad del artículo: "))
            tipo_impuesto = obtener_tipo_impuesto()
            items.append((precio_unitario, cantidad, tipo_impuesto))
        except ValueError as e:
            print(f"Error: {e}")
            continue

        otra = input("¿Desea agregar otro artículo? (si/no): ").strip().lower()
        if otra != 'si':
            break
    
    return items

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1, 2, 3): ").strip()

        opciones = {
            '1': manejar_calculo_item,
            '2': manejar_calculo_compra,
            '3': salir
        }
        
        if opcion in opciones:
            opciones[opcion]()
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def manejar_calculo_item():
    precio_unitario, cantidad, tipo_impuesto = obtener_datos_item()
    try:
        total_impuestos, total_item = calcular_total_item(precio_unitario, cantidad, tipo_impuesto)
        print(f"\nTotal de Impuestos: {total_impuestos:.2f}")
        print(f"Precio Total del Ítem: {total_item:.2f}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

def manejar_calculo_compra():
    items = obtener_datos_compra()
    try:
        total_impuestos, total_compra = calcular_total_compra(items)
        print(f"\nTotal de Impuestos en la Compra: {total_impuestos:.2f}")
        print(f"Valor Total a Pagar: {total_compra:.2f}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

def salir():
    print("¡Gracias por usar la aplicación!")
    sys.exit(0)

if __name__ == '__main__':
    main()