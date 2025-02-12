# Task 10: Sales Log File Management
# Creating and writing to sales log file
with open("sales_log.txt", "w") as file:
    file.write("Total sales today: $12,345.\n")
    file.write("Number of transactions: 123.\n")

# Reading and printing file content
with open("sales_log.txt", "r") as file:
    print("\nContent of 'sales_log.txt':")
    print(file.read())