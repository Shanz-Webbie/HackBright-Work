"""Print out all the melons in our inventory."""


from melons import melon_names, melon_prices, melon_seedlessness, flesh_color, rind_color, average_weight 


def print_melon(name, price, seedless, flesh_color= None, rind_color= None, average_weight = None):
    """Print each melon with corresponding attribute information."""

    have_or_have_not = 'have'
    if seedless:
        have_or_have_not = 'do not have'

    print(f'{name}s {have_or_have_not} seeds, have a {flesh_color} flesh color, have a {rind_color} rind color, an average weight of {average_weight}, and are ${price} each')
    


for i in melon_names:
    print_melon(melon_names[i], melon_prices[i], melon_seedlessness[i], flesh_color[i], rind_color[i], average_weight[i])
