"""Generate sales report showing total melons each salesperson sold."""

# create an empty list of sales peoples' names that have sold melons
salespeople = []
# create an empty list of the number of melons each sales person sold
melons_sold = []

# open the sales-report.txt file as and refer to it as "f"
f = open('sales-report.txt')

# iterate over every line in sales-report.txt
for line in f:
    # strip the whitespace to the right
    line = line.rstrip()
    # divide each line by the "|" sign to get individual sales entries
    entries = line.split('|')
    # automate the extraction of each entry as the first item of the file
    salesperson = entries[0]
    # convert the number of melons (third item) into a number
    melons = int(entries[2])
    # if a given sales person is in the sales people list already
    # increment that number of melons they have sold
    if salesperson in salespeople:
        # find the position where the salesperson is
        position = salespeople.index(salesperson)
        # reference that position to index the num of melons sold
        melons_sold[position] += melons
    # otherwise add a given salesperson to the list as well as how many
    # melons that given salesperson has sold    
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

# iterate over the entire list of sales people
for i in range(len(salespeople)):
    # repeatedly print the final num of each unique person and 
    # how many melons that person has sold
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')