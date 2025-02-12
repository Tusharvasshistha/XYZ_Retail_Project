# Task 5: Stock Level Alert System
# Taking stock level as input
stock_level = int(input("Enter stock level: "))
threshold = 20

# Checking stock level and printing alert
if stock_level < threshold:
    print("Reorder Now")
else:
    print("Stock is sufficient")