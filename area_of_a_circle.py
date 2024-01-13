def area_of_circle(radius):
    pi = 3.14
    area = pi * (radius) ** 2
    return area

user_input = int(input("What is the radius of your circle?"))
user_circle_area = area_of_circle(user_input)
print(user_circle_area)