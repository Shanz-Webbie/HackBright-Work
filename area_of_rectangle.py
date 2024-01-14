def area_of_rectangle(width, length):
    area = width * length
    return area


user_input_width = int(input("What is the width of your rectangle?"))
user_input_length = int(input("What is the length of your rectangle?"))
user_rectangle_area = area_of_rectangle(user_input_width, user_input_length)
print(user_rectangle_area)