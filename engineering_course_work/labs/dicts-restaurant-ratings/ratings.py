


"""Restaurant rating lister."""

def get_user_input():
    while True:
        try:
            user_restaurant_name = input("Please input a restaurant name: ")
            user_restaurant_score = int(input("Please input a rating from 1 to 5: "))
            if user_restaurant_score < 1 or user_restaurant_score > 5:
                print("Rating has to be a number between 1 and 5. Restarting...")
            else:
                return user_restaurant_name, user_restaurant_score
        except ValueError:
            print(f"Rating has to be a number.")
            break


def get_ratings(file):
    the_file = open(file)
    restaurant_scores = {}

    for line in the_file:
        ratings = line.rstrip().split(":")
        restaurant, rating = ratings
        restaurant_scores[restaurant] = rating

    user_restaurant_name, user_restaurant_score = get_user_input()
    restaurant_scores[user_restaurant_name] = user_restaurant_score # {} >> Applebee = 2

    for restaurant, rating in sorted(restaurant_scores.items()):
        print(f"{restaurant} is rated at {rating}")

    return restaurant_scores

