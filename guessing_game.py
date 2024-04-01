import random

"""A number-guessing game."""


def greet_user():
    print("Hello, what's your name?") #greet the player
    name = input("(type in your name) ") #players name
    print(f"I'm thinking of a number between 1 and 100. Try to guess my number.") #print game rules
    return name

def comp_pick_a_number():
    number = random.randrange(1, 101) #computer picks a number for the user to guess
    return number

def user_pick_a_number():
    guess_num = int(input("Your number guess? ")) #user inputs a guessed number
    return guess_num

def get_total_guesses():
    guess_amount = 0 #sum of guesses
    return guess_amount

def get_high_score():
    attempts = 0 #sum of attempts to guess the correct number
    return attempts

def max_guesses():
    pass

def verify_if_user_wants_to_play_again():
    play_again = input("Would you like to play again? (y/n) ") # Ask user if they want to keep playing
    if play_again.lower() == "y":
        return True
    elif play_again.lower() == "n":
        return False
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        return verify_if_user_wants_to_play_again()
    
def run_game():
    name = greet_user()
    high_score = float('inf')  # Initialize high score

    while True:
        number = comp_pick_a_number()
        guess_amount = 0

        while True:
            guess_num = user_pick_a_number()
            guess_amount += 1 

            if guess_num < number:
                print("Your guess is too low, try again.")
            elif guess_num > number:
                print("Your guess is too high, try again.")
            else:
                print(f"You got it, {name}, in {guess_amount} guesses!")
                if guess_amount < high_score:
                    high_score = guess_amount
                    print(f"Congratulations! Your new high score is {high_score}!")
                break

        play_again = input("Would you like to play again? (y/n) ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
        run_game()

        
        
        
    

