import random
import climage
from io import BytesIO
import numpy as np
from PIL import Image
import requests

# List of fortunes that will be randomly selected.

fortunes = ["Do not be afraid of competition.",
"An exciting opportunity lies ahead of you.",
"You love peace.",
"Get your mind set…confidence will lead you on.",
"You will always be surrounded by true friends.",
"Sell your ideas-they have exceptional merit.",
"You should be able to undertake and complete anything.",
"You are kind and friendly.",
"You are wise beyond your years.",
"Your ability to juggle many tasks will take you far.",
"A routine task will turn into an enchanting adventure.",
"Be true to your work, your word, and your friend.",
"A journey of a thousand miles begins with a single step.",
"Forget injuries; never forget kindnesses.",
"Respect yourself and others will respect you.",
"Sing everyday and chase the mean blues away.",
"Attitude is a little thing that makes a big difference.",
"Experience is the best teacher.",
"Expect the unexpected.",
"Eat chocolate to have a sweeter life.",
"Once you make a decision the universe conspires to make it happen.",
"Nothing great was ever achieved without enthusiasm.",
"Dance as if no one is watching.",
"Live this day as if it were your last.",
"Your life will be happy and peaceful.",
"Reach for joy and all else will follow.",
"Move in the direction of your dreams.",
"Bloom where you are planted.",
"Appreciate. Appreciate. Appreciate.",
"Happy News is on its way."]

# Start user interaction

def ask_user_if_they_want_a_fortune():
    return input("Would you like a fortune? Y/N ")


def print_and_resize_fortune_cookie_image(response):
    """Print an image of a fortune cookie into the terminal
    :param response:
    """
    # Convert the image to RGB
    img = Image.open(BytesIO(response.content)).convert('RGB')
    # Convert the image into 50px * 40px
    smaller_img_image = img.resize((50, 40))
    arr = np.array(smaller_img_image)
    # Output the image
    output = climage.convert_array(arr, is_unicode=True)
    print(output)


def download_and_return_fortune_image():
    response = requests.get(
        'https://images.squarespace-cdn.com/content/v1/5f103e5123a13a598106a998/1594903465373-I1453DPQ758S6ORUZF5Z/fortune-cookie-21.jpg')
    return response


def run_fortune_game():

    response = download_and_return_fortune_image()

    while True:

        print(" > ")

        answer = ask_user_if_they_want_a_fortune().lower()

        if answer == 'y':

            print_and_resize_fortune_cookie_image(response)

            # Print a random fortune from the list. Continue until 'no' is selected.

            print(random.choice(fortunes))

        elif answer == "n":

            # No image is printed. Send a nice goodbye message.

            print("Have a great day!")
            break

            # Prompt the user to respond 'y' or 'n'. Loop until they quit or continue.

        else:
            print("Please input 'y' or 'n' to continue. This is not case-sensitive :)")


# Safe to import


if __name__ == "__main__":
    run_fortune_game()
