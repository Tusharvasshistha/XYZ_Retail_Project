# Task 6: Sales Report Formatting
# Given list of products sold
products_sold = ["laptop", "mouse", "keyboard", "monitor", "printer"]

# Using for loop
print("\nSales Report (Using for loop):")
for product in products_sold:
    print(product.upper())

# Using while loop
print("\nSales Report (Using while loop):")
i = 0
while i < len(products_sold):
    print(products_sold[i].upper())
    i += 1
