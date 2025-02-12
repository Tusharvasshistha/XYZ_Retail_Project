# task 20
# Define customers and their total purchases
customers = {
    "John Doe": 250,
    "Jane Smith": 500,
    "Alice Johnson": 1000,
    "Bob White": 150
}

# Define the tiered points system
def calculate_loyalty_points(purchase_amount):
    if purchase_amount >= 1000:
        return purchase_amount * 2.0  # 2x multiplier
    elif purchase_amount >= 500:
        return purchase_amount * 2.0  # 2x multiplier
    elif purchase_amount >= 250:
        return purchase_amount * 1.5  # 1.5x multiplier
    else:
        return purchase_amount * 1.0  # 1x multiplier

# Print customer loyalty points
print("Customer Loyalty Points:\n")
for customer, amount in customers.items():
    points = calculate_loyalty_points(amount)
    print(f"{customer}: ${amount} Purchase, Loyalty Points: {points:.1f}")
