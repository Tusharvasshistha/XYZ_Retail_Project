# Assigning the number of units sold
category_a = 150
category_b = 120

# Calculating sales metrics
total_units_sold = category_a + category_b
difference = abs(category_a - category_b)
ratio = round(category_a / category_b, 2)  # Rounded to 2 decimal places

# Printing the results
print("Sales Data Summary:\n")
print(f"Total Units Sold: {total_units_sold}")
print(f"Difference Between Categories: {difference}")
print(f"Ratio of Category A to Category B: {ratio}")