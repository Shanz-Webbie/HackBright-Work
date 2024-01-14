def celcius_to_fahrenheit(c_temp):
    new_temperature = 9/5 * (c_temp) + 32
    return new_temperature


conversion_test = (celcius_to_fahrenheit(10))
print(conversion_test)