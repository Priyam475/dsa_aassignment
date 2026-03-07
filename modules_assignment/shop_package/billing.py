def calculate_total(prices):
    """Return the sum of a list of prices."""
    return sum(prices)

def apply_tax(price, tax_rate):
    """Return the price including tax based on the provided tax_rate."""
    tax_amount = price * (tax_rate / 100)
    return price + tax_amount