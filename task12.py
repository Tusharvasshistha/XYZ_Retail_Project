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

