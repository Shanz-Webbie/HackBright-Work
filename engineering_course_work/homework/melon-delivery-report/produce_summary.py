
def process_delivery_file(file_path,day):
    """process a delivery file and print content from a given day."""
    print(f"Here is the order information for Day {day}:")
    # open a file for a given day
    the_file = open(file_path)
    # iterate over the lines in the file
    for line in the_file:
    # remove white space on a given line
        line = line.rstrip()
    # split each word that is separated with a "|"
        words = line.split('|')
    # assume melon is the first item in a given line
    melon = words[0]
     # assume count is the second item in a given line
    count = words[1]
     # assume amount is the third item in a given line
    amount = words[2]
    # print a delivery message
    print(f"Delivered {count} {melon}s for total of ${amount}\n")
    # close the file
    the_file.close()

process_delivery_file("um-deliveries-day-1.txt", 1)
process_delivery_file("um-deliveries-day-2.txt", 2)
process_delivery_file("um-deliveries-day-3.txt", 3)

# print("Day 1")
# the_file = open("um-deliveries-day-1.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()


# print("Day 2")
# the_file = open("um-deliveries-day-2.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()


# print("Day 3")
# the_file = open("um-deliveries-day-3.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()
