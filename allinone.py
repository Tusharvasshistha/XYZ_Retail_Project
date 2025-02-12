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

# Task 2: Customer Age Data
# Storing customer's name and age
customer_name = "John Doe"
customer_age = 30

# Creating a personalized marketing message
message = f"Dear {customer_name}, at {customer_age}, you’re eligible for our premium loyalty program."

# Printing the message for email campaigns
print("\nCustomer Marketing Message:\n")
print(message)

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

# Task 4: Inventory Lookup
# Creating a dictionary with product details
product_info = {
    "product_name": "Wireless Mouse",
    "SKU": "WM-12345",
    "price": 25.99,
    "category": "Electronics"
}

# Printing product name and SKU
print("\nInventory Lookup:\n")
print(f"Product Name: {product_info['product_name']}")
print(f"Product SKU: {product_info['SKU']}")

# Task 5: Stock Level Alert System
# Taking stock level as input
stock_level = int(input("Enter stock level: "))
threshold = 20

# Checking stock level and printing alert
if stock_level < threshold:
    print("Reorder Now")
else:
    print("Stock is sufficient")

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

# Task 7: Area Calculation for Store Layout
def calculate_area(length, width):
    return length * width

# Using the function to calculate store sections
print("\nStore Layout Area Calculations:")
length1, width1 = 20, 15
print(f"The area of section 1 is {calculate_area(length1, width1)} square meters.")

length2, width2 = 25, 10
print(f"The area of section 2 is {calculate_area(length2, width2)} square meters.")

# Task 8: Customer Feedback Analysis
def count_vowels(feedback):
    vowels = "aeiouAEIOU"
    return sum(1 for char in feedback if char in vowels)

# Sample customer feedback
customer_feedback = "The service was excellent and very quick!"

# Analyzing feedback
vowel_count = count_vowels(customer_feedback)
reversed_feedback = customer_feedback[::-1]

# Printing analysis results
print("\nCustomer Feedback Analysis:")
print(f"Original Feedback: {customer_feedback}")
print(f"Number of Vowels: {vowel_count}")
print(f"Reversed Feedback: {reversed_feedback}")

# Task 9: Price Filtering Tool
# Given product prices
product_prices = [150, 85, 300, 120, 45, 200]
discount_threshold = 100

# Filtering products eligible for the discount campaign
discount_eligible_products = [price for price in product_prices if price < discount_threshold]

# Printing the filtered list
print("\nPrice Filtering Tool:")
print(f"Products eligible for the discount campaign: {discount_eligible_products}")

# Task 10: Sales Log File Management
# Creating and writing to sales log file
with open("sales_log.txt", "w") as file:
    file.write("Total sales today: $12,345.\n")
    file.write("Number of transactions: 123.\n")

# Reading and printing file content
with open("sales_log.txt", "r") as file:
    print("\nContent of 'sales_log.txt':")
    print(file.read())

# Task 11
# Given sales data for the last 7 days
daily_sales = [1200, 1500, 1100, 1800, 1700, 1600, 1400]

# Calculate the average sales
average_sales = sum(daily_sales) / len(daily_sales)

# Print the result with two decimal places
print(f"Average Daily Sales for the Past Week: ${average_sales:.2f}")

# Task 12
# Given customer spending data
customer_spendings = [200, 800, 1500, 3000, 450, 1200]

# Categorization function
def categorize_spending(amount):
    if amount < 500:
        return "Low"
    elif 500 <= amount < 1500:
        return "Medium"
    else:
        return "High"

# Printing categorized results
print("Customer Spending Categories:\n")
for i, spending in enumerate(customer_spendings, start=1):
    category = categorize_spending(spending)
    print(f"Customer {i}: Spending = ${spending} -> Category: {category}")

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

# task 14
# Sample input
customer_feedback = "I am very happy with the service. It was a good experience!"
positive_words = ["good", "happy", "excellent", "great"]
negative_words = ["bad", "disappointed", "poor", "terrible"]

# Convert feedback to lowercase for case-insensitive comparison
feedback_lower = customer_feedback.lower()

# Check for positive and negative words in the feedback
contains_positive = any(word in feedback_lower for word in positive_words)
contains_negative = any(word in feedback_lower for word in negative_words)

# Determine sentiment
if contains_positive and not contains_negative:
    sentiment = "Positive"
elif contains_negative and not contains_positive:
    sentiment = "Negative"
elif contains_positive and contains_negative:
    sentiment = "Mixed"
else:
    sentiment = "Neutral"

# Print result
print(f"Customer Feedback Sentiment: {sentiment}")


#task 15
# Given employee data with current salary and performance rating
employees = {
    "Alice": {"current_salary": 50000, "rating": "Excellent"},
    "Bob": {"current_salary": 40000, "rating": "Good"},
    "Charlie": {"current_salary": 45000, "rating": "Average"},
    "David": {"current_salary": 35000, "rating": "Poor"}
}

# Increment percentages based on performance rating
increments = {
    "Excellent": 20,
    "Good": 15,
    "Average": 10,
    "Poor": 5
}

# Function to calculate updated salary
def calculate_new_salary(current_salary, rating):
    increment_percentage = increments.get(rating, 0)
    increment_amount = (increment_percentage / 100) * current_salary
    return current_salary + increment_amount

# Printing updated salaries
print("Updated Salaries After Increment:\n")
for name, details in employees.items():
    updated_salary = calculate_new_salary(details["current_salary"], details["rating"])
    print(f"{name}: Current Salary = ${details['current_salary']}, "
          f"Rating = {details['rating']}, Updated Salary = ${updated_salary:.2f}")

#task 16
# Given list of daily sales for a month
daily_sales = [
    200, 250, 300, 400, 350, 500, 450, 300, 250, 400,
    200, 300, 450, 500, 400, 250, 350, 300, 450, 400,
    250, 300, 200, 400, 350, 300, 500, 450, 300, 250
]

# Calculate total and average sales
total_sales = sum(daily_sales)
average_sales = total_sales / len(daily_sales)

# Generate the report content
report_content = f"""Monthly Sales Report
---------------------
Total Sales: ${total_sales}
Average Daily Sales: ${average_sales:.2f}
"""

# Write report to a text file
with open("monthly_report.txt", "w") as file:
    file.write(report_content)

# Print confirmation
print("Monthly sales report has been generated: monthly_report.txt")

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

# task 18
# Given list of customer names with extra spaces and inconsistent capitalization
customer_names = [" john doe ", " MARY SMITH ", " aLICE JOHNSON ", "bOB WHITE"]

# Function to clean and format names
def clean_name(name):
    return name.strip().title()  # Removes spaces and capitalizes properly

# Clean all customer names
cleaned_names = [clean_name(name) for name in customer_names]

# Print cleaned names
print("Cleaned Customer Names for Database Entry:\n")
for name in cleaned_names:
    print(name)

# task 19
# Function to forecast sales based on the last 3 months' average
def forecast_sales(sales_last_3_months):
    average_sales = sum(sales_last_3_months) / len(sales_last_3_months)
    return average_sales

# Given sales data for the last 3 months
sales_last_3_months = [20000, 22000, 25000]

# Calculate forecasted sales
forecasted_sales = forecast_sales(sales_last_3_months)

# Print the forecasted sales
print(f"Forecasted Sales for Next Month: ${forecasted_sales:.2f}")


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
