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
