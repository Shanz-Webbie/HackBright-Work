"""Functions to parse a file containing villager data."""

def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    species = open(filename)
    unique_species = set()
    for specie in species:
        result = specie.rstrip().split("|")[1]
        unique_species.add(result)

    return unique_species



def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """
    names = open(filename)
    villagers = []
    for name in names:
        name, species = name.rstrip().split("|")[:2]
        if search_string == "All" or search_string == species:
            villagers.append(name)
    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
    fitness = []
    nature = []
    education =[]
    music = []
    fashion = []
    play =[]

    csv = open(filename)

    for hobby in csv:
        #name|species|personality|hobby|motto
        name, species, personality, hobby, motto = hobby.rstrip().split("|")
        if hobby == "Fitness":
            fitness.append(name)
        elif hobby == "Nature":
            nature.append(name)
        elif hobby == "Education":
            education.append(name)
        elif hobby == "Music":
            music.append(name)
        elif hobby == "Fashion":
            fashion.append(name)
        elif hobby == "Play":
            play.append(name)
    
    return [sorted(fitness), sorted(nature), sorted(education), sorted(music), sorted(fashion), sorted(play)]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    csv = open(filename)
#all_data(filename) → list[tuple[str]]
    lst_all_data = []   
    for row in csv:
        line = row.rstrip().split("|")
        lst_all_data.append(tuple(line))

    return lst_all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """
    data = all_data(filename)
    
    for line in data:
        name, species, personality, hobby, motto = line
        if name == villager_name:
            return motto
    return None



def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
