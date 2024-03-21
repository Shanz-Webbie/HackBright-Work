def calibrate(frequency_changes):
    # Write your code here
    result = 0
    for change in frequency_changes:
        print(f" the change is {change}")
        result += change
        print(f" the result is {result}")
    return result

print(calibrate([1,2,3,4,5]))

# random_words = ["poop", "toots", "stink", "sphincter", "drink", "wink"]
# #
# counter = 0
# for word in random_words:
#     print("Printing next word: ")
#     print(word)
#     print(counter)
#     counter += 1
# print("------------")
#
#
# for number in range(len(random_words)):
#     print("Printing next word: ")
#     print(random_words[number])
#     print(number)
