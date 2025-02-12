# Task 9: Price Filtering Tool
# Given product prices
product_prices = [150, 85, 300, 120, 45, 200]
discount_threshold = 100

# Filtering products eligible for the discount campaign
discount_eligible_products = [price for price in product_prices if price < discount_threshold]

# Printing the filtered list
print("\nPrice Filtering Tool:")
print(f"Products eligible for the discount campaign: {discount_eligible_products}")