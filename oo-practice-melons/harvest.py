############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""
    species = "melon"

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []

        self.name = name  
        self.code = code
        self.first_harvest = first_harvest 
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings = self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []
# code, first_harvest, color, is_seedless, is_bestseller, name
    melon_dict = {'musk':
        {'code':'musk',
        'first_harvest':1998, 
        'color':'green',
        'is_seedless':True,
        'is_bestseller':True,
        'name':'Muskmelon',
        'pairings':['mint']},
        'cas':
        {'code':'cas',
        'first_harvest':2003, 
        'color':'orange',
        'is_seedless':False,
        'is_bestseller':False,
        'name':'Casaba',
        'pairings':['mint','strawberries']},
        'cren':
        {'code':'cren',
        'first_harvest':1996, 
        'color':'green',
        'is_seedless':False,
        'is_bestseller':False,
        'name':'Crenshaw',
        'pairings':['prosciutto']},
        'yw':
        {'code':'yw',
        'first_harvest':2013, 
        'color':'yellow',
        'is_seedless':False,
        'is_bestseller':True,
        'name':'Yellow Watermelon',
        'pairings':['ice cream']}
        }
    
    # musk = MelonType('musk',melon_dict['musk']['code'], 
    #                           melon_dict['musk']['first_harvest'], 
    #                           melon_dict['musk']['is_seedless'], 
    #                           melon_dict['musk']['is_bestseller'], 
    #                           melon_dict['musk']['name'])
    # print(musk.name)
    
    for melon in melon_dict:
        melon_obj = MelonType(melon, melon_dict[melon]['code'], 
                              melon_dict[melon]['first_harvest'], 
                              melon_dict[melon]['is_seedless'], 
                              melon_dict[melon]['is_bestseller'], 
                              melon_dict[melon]['name'])
        melon_obj.add_pairing(melon_dict[melon]['pairings'])
        all_melon_types.append(melon_obj)
    
    return all_melon_types

make_melon_types()


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    pass
    # Fill in the rest


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    pass
    # Fill in the rest


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
