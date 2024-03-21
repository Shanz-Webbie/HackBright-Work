def greet_user():
    name = input("What's your name?: ")
    fav_ghibli_movie = input("What's your favorite Ghibli movie?: ")

    print("\nAwesome! Hi {}, {} is a great film.".format(name, fav_ghibli_movie))
    return name

def print_options(options):
    for i, option in enumerate(options, start=1):
        print(f"Option {i}: {option}")

def choose_option(options):
    while True:
        print_options(options)
        choice = input("> ")
        if choice.isdigit() and (1 <= int(choice) and int(choice) <= len(options)):
            return int(choice)
        else:
            print("\nInvalid choice. Please select a valid option.")

def catbus_adventure(name):
    print("\nYou hop aboard the Catbus, a fantastical creature with the body of a cat and the tail of a bus.")
    print("It takes you to a hidden village filled with friendly spirits and bustling markets.")
    print("As you explore, you meet new friends and uncover ancient secrets hidden within the village's walls.")
    print("\nWhat do you do next?\n")
    options = ["Join a Spirited Festival", "Help a Lost Spirit Find its Way Home"]
    choice = choose_option(options)
    if choice == 1:
        print("\nYou immerse yourself in the vibrant festivities, dancing and feasting with the villagers.")
        print("The air is filled with laughter and music, and for a moment, you forget all your worries.")
        print("As the night comes to a close, you bid farewell to your newfound friends and return home, your heart full of joy.")
    elif choice == 2:
        print("\nMoved by the spirit's plight, you offer your assistance in guiding it back to its rightful place.")
        print("With your help, the spirit reunites with its family, and you're hailed as a hero by the villagers.")
        print("Grateful for your kindness, they shower you with gifts and blessings before you depart, your spirits lifted by the experience.")

def ponyo_adventure(name):
    print("\n")
    print("You plunge into the depths of the ocean with Ponyo and Sosuke, embarking on a magical underwater adventure.")
    print("Surrounded by colorful sea creatures and breathtaking coral reefs, you discover a world teeming with life and wonder.")
    print("\n")
    print("What do you choose to do?")
    print("\n")
    options = ["Help Ponyo Regain her Human Form", "Explore the Hidden Depths of the Ocean"]
    choice = choose_option(options)
    if choice == 1:
        print("\n")
        print("You assist Ponyo in her quest to become human and reunite with Sosuke on land.")
        print("Through courage and determination, you overcome obstacles and challenges, ultimately restoring Ponyo's human form.")
        print("With tears of joy, Ponyo embraces Sosuke, and together, they embark on a new chapter of their lives.")
    elif choice == 2:
        print("\n")
        print("Intrigued by the mysteries of the ocean, you venture deeper into its depths, uncovering ancient ruins and forgotten civilizations.")
        print("Along the way, you befriend curious sea creatures and unlock the secrets of the underwater world.")
        print(" Though your journey is fraught with danger, the beauty and wonder you encounter make it all worthwhile.")

def mononoke_adventure(name):
    print("\n")
    print("You embark on a perilous journey into the heart of the forest, where the spirits of nature dwell.")
    print("Alongside Princess Mononoke and her loyal companions, you face fierce adversaries and confront the devastating impact of humanity on the natural world.")
    print("\n")
    print("What do you choose to do?")
    print("\n")
    options = ["Fight to Protect the Forest", "Seek Peaceful Resolution with the Humans"]
    choice = choose_option(options)
    if choice == 1:
        print("\n")
        print("You join Princess Mononoke in a battle against the forces threatening to destroy the forest.")
        print("With courage and determination, you stand your ground against overwhelming odds, fighting for the survival of the spirits and their home.")
        print("Though the battle is arduous, your efforts are not in vain, and the forest is saved from destruction.")
    elif choice == 2:
        print("\n")
        print("Believing in the power of diplomacy, you strive to find a peaceful solution to the conflict between humans and spirits")
        print("Through dialogue and negotiation, you bridge the gap between the two sides, fostering understanding and cooperation.")
        print("Your actions bring about a newfound harmony between humanity and nature, and the forest flourishes once more.")
    else:
        print("I don't understand that command. Please start again and read the directions over.")
        print("You can start again by running 'python adventure.py' another time at the prompt.")

def totoro(name):
    print("{} is standing in a serene forest, surrounded by whispering trees and gentle streams".format(name))
    print("\n")
    print("Suddenly, a mysterious figure appears before {} – it's Totoro, the guardian spirit of the forest.".format(name))
    print("He invites you on an extraordinary adventure through the enchanting world of Studio Ghibli.")
    options = ["Follow Totoro into the Forest", "Decline Totoro's Invitation and Return Home"]
    choice = choose_option(options)
    if choice == 1:
        print("{} accepts Totoro's invitation and follows him deeper into the forest".format(name))
        print("Along the way, you encounter various characters and creatures, each offering a different path to explore.")
        print("Who do you choose to follow?")
        character = choose_option(["Follow the Catbus to a Magical Village", "Venture into the Spirit Realm with Princess Mononoke", "Dive into the Ocean with Ponyo and Sosuke"])
        if character == 1:
            catbus_adventure(name)
        elif character == 2:
            mononoke_adventure(name)
        elif character == 3:
            ponyo_adventure(name)
    else:
        print("\nThough tempted by the allure of adventure, you decide to decline Totoro's invitation and return home.")
        print("As you journey back through the forest, you can't help but wonder about the magical world you glimpsed.")
        print("Though your adventure may have come to an end, the memories you've made will stay with you forever.")
       



def main():
    name = greet_user()
    totoro(name)

main()