# open the "um-server-01" text file and save it to a log_file variable
log_file = open("um-server-01.txt")

# define a function that takes the log_file variable and passes it in as a parameter
def generate_sales_reports(log_file):
# iterate over each line withing the log_file
    for line in log_file:
# use the strip method to remove the whitespace on the right of each line and 
# save the result to the line variable
        line = line.rstrip()
# slice the first item (index 0) to the second item (index 3) contained within line
# save the result of the slice into a day variable
        day = line[0:3]
# if the day variable is on a Tuesday
        if day == "Tue":
# print the information stored in the line variable
            print(line)

# call the function and pass in the text file stored in the "log_file" from line 2
generate_sales_reports(log_file)
