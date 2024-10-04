# Constants
FIXED_TAX_PER_PLASTIC_BAG = 66  # Sets a fixed tax rate for plastic bags.

def calculate_item_total(price, quantity, tax_type):
    """
    Calculates the total tax and the total price of an item based on the given parameters.

    Args:
        price (float): Unit price of the item (in pesos).
        quantity (int): Quantity of the item.
        tax_type (str or float): Applicable tax type (can be 'VAT', 'INC', 'exempt', or a percentage).

    Returns:
        tuple: A tuple containing the total tax and the total price of the item.
    """
    # Attempt to convert price to float and validate it
    try:
        price = float(price)
    except ValueError:
        raise ValueError(f"Price must be a number, got {price}")

    # Validate price and tax_type inputs
    if price < 0 or (price == 0 and tax_type != "fixed"):
        raise ValueError("Invalid price.")
    
    if isinstance(tax_type, (int, float)) and tax_type < 0:
        raise ValueError("Tax rate must be non-negative.")
    
    if quantity <= 0:
        raise ValueError("The quantity must be positive and greater than zero.")

    # Calculate the total price before tax
    total_price = price * quantity
    
    # Calculate tax based on the type of tax specified
    if tax_type == "exempt":
        total_tax = 0  # No tax for exempt items
    elif tax_type == "fixed":
        total_tax = FIXED_TAX_PER_PLASTIC_BAG * quantity  # Fixed tax per item
    elif isinstance(tax_type, (int, float)):
        total_tax = total_price * (tax_type / 100)  # Percentage based tax
    else:
        raise TypeError("The tax type must be a number, 'fixed' or 'exempt'.")

    # Add the calculated tax to the total price
    total_price += total_tax

    # Return both total tax and total price
    return total_tax, total_price

def calculate_total_purchase(items):
    """
    Calculates the total tax and total price for a list of items.

    Args:
        items (list of tuples): List containing tuples of (unit_price, quantity, tax_type) for each item.

    Returns:
        tuple: A tuple containing the total tax and total price for all items.
    """
    # Initialize total tax and price counters
    total_tax = 0
    total_price = 0

    # Process each item in the list
    for unit_price, quantity, tax_type in items:
        # Calculate the tax and total for each item
        item_tax, item_total = calculate_item_total(unit_price, quantity, tax_type)
        total_tax += item_tax  # Sum up total tax
        total_price += item_total  # Sum up total price

    # Return the aggregate total tax and total price
    return total_tax, total_price