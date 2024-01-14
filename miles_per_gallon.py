def total_mpg(miles_traveled, number_of_gallons_of_gas_used):
    miles_per_gallon = miles_traveled / number_of_gallons_of_gas_used
    return miles_per_gallon


user_input_miles_traveled = int(input("How many miles did you travel?"))
user_input_number_of_gallons_used = int(input("How many gallons did you need to refill your car with at the gas station?"))
user_mpg = total_mpg(user_input_miles_traveled, user_input_number_of_gallons_used)
print(user_mpg)