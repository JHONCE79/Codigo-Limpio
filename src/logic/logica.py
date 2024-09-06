# Constants
FIXED_TAX_PER_PLASTIC_BAG = 66

def calculate_item_total(price, quantity, tax_type):
    """
    Calculates the total tax and the total price of an item.

    :param price: Unit price of the item (in pesos).
    :param quantity: Quantity of the item.
    :param tax_type: Applicable tax type (can be VAT, INC, or "exempt").
    :return: A tuple with the total tax and the total price.
    """
    if price <= 0:
        raise ValueError("The unit price must be positive and greater than zero.")
    if quantity <= 0:
        raise ValueError("The quantity must be positive and greater than zero.")

    if tax_type == "exempt":
        return 0, price * quantity
    
    if tax_type == "fixed":
        total_tax = FIXED_TAX_PER_PLASTIC_BAG * quantity
    elif isinstance(tax_type, (int, float)):
        total_tax = price * quantity * (tax_type / 100)
    else:
        raise TypeError("The tax type must be a number, 'fixed' or 'exempt'.")

    total_price = price * quantity + total_tax
    return total_tax, total_price

def calculate_total_purchase(items):
    """
    Calculates the total tax and the total price of a purchase with multiple items.

    :param items: A list of tuples, each with (unit_price, quantity, tax_type).
    :return: A tuple with the total tax and the total price.
    """
    total_tax = 0
    total_price = 0
    
    for unit_price, quantity, tax_type in items:
        item_tax, item_total = calculate_item_total(unit_price, quantity, tax_type)
        total_tax += item_tax
        total_price += item_total
    
    return total_tax, total_price
