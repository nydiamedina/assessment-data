# Open "um-server-01.txt" file and store it in variable log_file
log_file = open("um-server-01.txt")

# Define function sales_reports that accepts a log_file as parameter
def sales_reports(log_file):
    # For each line in log_file, whitespaces will be removed, and the 
    # first three chars of each line are stored in day
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        # If day is equal to "Mon", line will be printed
        if day == "Mon":
            print(line)

def get_melon_orders(log_file):
    for line in log_file:
        line = line.rstrip()
        words = line.split(" ")
        quantity = int(words[2])
        item = words[3:-4]
        if quantity > 10 and "Melon" in item:
            print(line)

# Function sales_report is called with the log_file from "um-server-01.txt"
# as parameter
print("Sales report")
sales_reports(log_file)
print("Melon orders")
get_melon_orders(log_file)
