# def testEqual(actual,expected,places=5):
#     '''
#     Does the actual value equal the expected value?
#     For floats, places indicates how many places, right of the decimal, must be correct
#     '''
#     if isinstance(expected,float):
#         if abs(actual-expected) < 10**(-places):
#             print('\tPass')
#             return True
#     else:
#         if actual == expected:
#             print('\tPass')
#             return True
#     print('\tTest Failed: expected {} but got {}'.format(expected,actual))
#     return False

# def get_name():
#     """Gets the user's name and returns it"""
#
#     name = input("What is your name? ")
#     return name
#
# print(get_name())

# def get_name():
#   """Gets the user's name and returns it"""
#
#   name = input("What is your name? ")
#   return name
#
# print(name)