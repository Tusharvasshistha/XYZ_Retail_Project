# Task 3: Product List Management
# Given product prices
product_prices = [50, 120, 30, 200, 90, 150, 180]
premium_product_price = 250

# Extract highest and lowest prices
highest_price = max(product_prices)
lowest_price = min(product_prices)

# Extract mid-range products
mid_range_products = [price for price in product_prices if lowest_price < price < highest_price]

# Add premium product price
product_prices.append(premium_product_price)

# Printing the results
print("\nProduct List Management:\n")
print(f"Highest Price: {highest_price}")
print(f"Lowest Price: {lowest_price}")
print(f"Mid-Range Products: {mid_range_products}")
print(f"Updated Product List with Premium Price: {product_prices}")