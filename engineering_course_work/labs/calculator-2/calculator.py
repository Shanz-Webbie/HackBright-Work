"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod)


# Replace this with your code
while True:
    user_input = input("What math operation would you like to perform? Input operator followed by numbers.")
    user_equation = user_input.split(' ')
    operator = user_equation[0]

    if user_input.lower() == "q" or user_input.lower() == "quit":
        print("Goodbye!")
        break
    # elif len(user_equation) < 2:
        # print("Error. Insufficient input.")
    # def compute_equation(operator,selected_equation):
    #     if operator == selected_equation(num1,num2)
    # result = operations[operator](num1,num2)
    # dict ={'+':add, '-':subtract}
        
    elif len(user_equation) <= 3:
        try:
            num1 = float(user_equation[1])
            num2 = float(user_equation[-1])
            if operator == "+":
                result = add(num1,num2)
            if operator == "-":
                result = subtract(num1,num2)
            if operator == "*":
                result = multiply(num1,num2)
            if operator == "/":
                result = divide(num1,num2)
            if operator == "square":
                result = square(num1)
            if operator == "cube":
                result = cube(num1)
            if operator == "pow":
                result = power(num1, num2)
            if operator == "mod":
                result = mod(num1, num2)
                
            
            
            print(result)            
        except:
            print("There was an error with your input.")
    else:
        print("Too many numbers.")
    