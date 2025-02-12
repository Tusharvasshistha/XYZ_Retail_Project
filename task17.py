# task 17
# Given list of products with stock levels
products = [
    {"product_name": "Product A", "stock": 50},
    {"product_name": "Product B", "stock": 150},
    {"product_name": "Product C", "stock": 30},
    {"product_name": "Product D", "stock": 75},
    {"product_name": "Product E", "stock": 20}
]

# Stock threshold for replenishment
threshold = 40

# Find products that need replenishment
replenishment_list = [product["product_name"] for product in products if product["stock"] < threshold]

# Print the result
print("Products that need replenishment:\n")
for product in replenishment_list:
    print(product)
