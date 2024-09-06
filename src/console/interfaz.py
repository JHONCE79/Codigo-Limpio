import sys
import os

# Add the path to the project directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logic.logica import calculate_item_total, calculate_total_purchase 

# Constants
FIXED_TAX_AMOUNT = 66

def show_menu():
    """
    Displays the main menu options.
    """
    options = [
        "--- Menú de Cálculo de Impuestos ---",
        "1. Calcular Total Item",
        "2. Calcular Total Compra",
        "3. Salir"
    ]
    print("\n" + "\n".join(options))

def show_tax_menu():
    """
    Displays the tax type options.
    """
    taxes = [
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
    print("\n" + "\n".join(taxes))

def get_tax_type():
    """
    Prompts the user to select a tax type and returns the corresponding value.
    """
    show_tax_menu()
    tax_option = input("Seleccione el tipo de impuesto (1-7): ").strip()

    taxes = {
        '1': 8,
        '2': 25,
        '3': 40,
        '4': 20,
        '5': 20,
        '6': "fixed",
        '7': get_vat_type
    }

    if tax_option in taxes:
        return taxes[tax_option]() if tax_option == '7' else taxes[tax_option]
    else:
        raise ValueError("Opción de impuesto inválida.")

def get_vat_type():
    """
    Prompts the user to select a VAT type and returns the corresponding value.
    """
    suboption = input("Seleccione: 1 para tasa general (19%), 2 para tasa reducida (5%), o 3 para Exento: ").strip()
    vat = {
        '1': 19,
        '2': 5,
        '3': 'exempt'
    }
    if suboption in vat:
        return vat[suboption]
    else:
        raise ValueError("Opción inválida para IVA.")

def get_item_data():
    """
    Collects and returns data for a single item.
    """
    try:
        unit_price = float(input("Ingrese el precio unitario del artículo (en pesos): "))
        quantity = int(input("Ingrese la cantidad del artículo: "))
        tax_type = get_tax_type()
        return unit_price, quantity, tax_type
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

def get_purchase_data():
    """
    Collects and returns data for multiple items.
    """
    items = []
    print("Ingrese los datos para cada artículo. Escriba 'fin' para terminar.")
    
    while True:
        try:
            print("\n--- Artículo ---")
            unit_price = float(input("Ingrese el precio unitario del artículo (en pesos): "))
            quantity = int(input("Ingrese la cantidad del artículo: "))
            tax_type = get_tax_type()
            items.append((unit_price, quantity, tax_type))
        except ValueError as e:
            print(f"Error: {e}")
            continue

        another = input("¿Desea agregar otro artículo? (si/no): ").strip().lower()
        if another != 'si':
            break
    
    return items

def main():
    """
    Main function to drive the menu and option selection.
    """
    while True:
        show_menu()
        option = input("Seleccione una opción (1, 2, 3): ").strip()

        options = {
            '1': handle_item_calculation,
            '2': handle_purchase_calculation,
            '3': exit_program
        }
        
        if option in options:
            options[option]()
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def handle_item_calculation():
    """
    Handles the calculation for a single item.
    """
    unit_price, quantity, tax_type = get_item_data()
    try:
        total_tax, total_item = calculate_item_total(unit_price, quantity, tax_type)
        print(f"\nTotal de Impuestos: {total_tax:.2f}")
        print(f"Precio Total del Ítem: {total_item:.2f}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

def handle_purchase_calculation():
    """
    Handles the calculation for multiple items in a purchase.
    """
    items = get_purchase_data()
    try:
        total_tax, total_purchase = calculate_total_purchase(items)
        print(f"\nTotal de Impuestos en la Compra: {total_tax:.2f}")
        print(f"Valor Total a Pagar: {total_purchase:.2f}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

def exit_program():
    """
    Exits the program with a thank you message.
    """
    print("¡Gracias por usar la aplicación!")
    sys.exit(0)

if __name__ == '__main__':
    main()
