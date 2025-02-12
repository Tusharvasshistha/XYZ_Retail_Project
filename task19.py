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
