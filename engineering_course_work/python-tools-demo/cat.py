"""It's like the cat command but written in Python!"""

melon_file = open('melon-data.txt')
for melon_data in melon_file:
    print(melon_data)
melon_file.close()

### or use with:
# with open('melon-data.txt') as melon_file:
#     for melon_data in melon_file:
#         print(melon_data)

### more flexibility with argv:
# import sys

# filename = sys.argv[1]   # first real argument
# for melon_data in open(filename):
#     print(melon_data)