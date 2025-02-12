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