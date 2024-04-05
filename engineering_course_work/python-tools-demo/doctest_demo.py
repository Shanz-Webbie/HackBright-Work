#this file is for showing a doctest running
#run the command: python3 -m doctest -v doctest_demo.py
# -v for verbose, to see more detail


def calculate_order_cost(price, qty, tax):
    """Calculate and return total order cost.

    Arguments:
      - price (float, int): individual item cost
      - qty (int): number of items
      - tax (int): tax percentage as whole number (ie, 5 for 5%)

    Return:
      - (int) the total order cost in US dollars

    For example:

      >>> calculate_order_cost(10, 5, 5)
      52.5
    """
    subtotal = price * qty

    tax_on_order = subtotal / 100 * tax
    
    return subtotal + tax_on_order