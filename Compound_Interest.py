def compound_interest(principal_amount, annual_interest, number_of_compounds_per_year, number_of_years):
    A = principal_amount * (1 + (annual_interest/number_of_compounds_per_year)) ** (number_of_compounds_per_year * number_of_years)
    return A


user_input = int(input("How many years has it been since you deposited money in this account?"))
total_interest = compound_interest(10000, .08, 12, user_input)
print(total_interest)