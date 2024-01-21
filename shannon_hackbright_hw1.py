def congratulations():
    print("congratulations")
    print(":)")


count = 5
while count > 0:
    print(count)
    count = count - 1

congratulations()


def greeting():
    user_name = input("Hello, what is your name? ")
    print(f"Hello, {user_name}")


greeting()


def ask_for_number():
    user_number = int(input("Please enter a number between 50 and 100. "))
    return user_number


def number_between_50_and_100():
    while True:
        user_number = ask_for_number()
        if (user_number > 100):
            print("Too high!")
        elif (user_number < 50):
            print("Too low!")
        else:
            print("Thank you!")
            break


number_between_50_and_100()