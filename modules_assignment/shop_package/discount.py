def apply_discount(price, percentage):
    """Calculate the discounted price given the original price and discount percentage."""
    # simply compute discount; caller responsible for valid values
    discount_amount = price * (percentage / 100)
    return price - discount_amount

def flat_discount(price, discount_amount):
    """Calculate the discounted price given the original price and flat discount amount."""
    # use the provided discount_amount instead of hardcoding
    return price - discount_amount