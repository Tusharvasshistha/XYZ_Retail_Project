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
