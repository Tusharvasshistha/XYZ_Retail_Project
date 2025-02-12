# task 13
# Given list of products with original prices and discount percentages
products = [
    {"name": "Product A", "original_price": 100, "discount_percentage": 10},
    {"name": "Product B", "original_price": 250, "discount_percentage": 20},
    {"name": "Product C", "original_price": 75, "discount_percentage": 15},
    {"name": "Product D", "original_price": 150, "discount_percentage": 5}
]

# Function to calculate final price after discount
def calculate_final_price(original_price, discount_percentage):
    discount_amount = (discount_percentage / 100) * original_price
    return original_price - discount_amount

# Printing the final prices
print("Final Prices After Discounts:\n")
for i, product in enumerate(products, start=1):
    final_price = calculate_final_price(product["original_price"], product["discount_percentage"])
    print(f"Product {i}: Original Price = ${product['original_price']}, "
          f"Discount = {product['discount_percentage']}%, "
          f"Final Price = ${final_price:.2f}")
