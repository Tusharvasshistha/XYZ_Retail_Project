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
