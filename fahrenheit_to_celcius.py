def fahrenheit_to_celcius(c_temp):
    new_temperature = 5/9 * ((c_temp) - 32)
    return new_temperature


conversion_test = (fahrenheit_to_celcius(10))
print(conversion_test)