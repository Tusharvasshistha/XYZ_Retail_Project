Description
 Project Overview:

XYZ Retail Company, a leading retailer in the industry, is looking to enhance its data analysis capabilities. To do this, they are developing a suite of Python-based tools to analyze their business data effectively. As a junior data scientist, your task is to create and implement various Python codes to solve basic data science problems related to their operations.

 

Task 1: Sales Data Summary

Objective: XYZ Retail wants to automate the process of calculating basic sales metrics.

Ø Assign the number of units sold in two categories, `Category A` and `Category B`, to variables.

Ø Calculate the total units sold, the difference between the categories, and the ratio of units sold.

Ø Print these results clearly for the management team.

 

· Sample Input -

         Category A: 150 units             Category B: 120 units

· Sample Output -

          Sales Data Summary:

           Total Units Sold: 270

           Difference Between Categories: 30

           Ratio of Category A to Category B: 1.25           

  

Task 2: Customer Age Data

Objective: Understanding the age distribution of customers is crucial for marketing strategies.

Ø Store a customer's name and age.

Ø Convert the age into a string and create a personalized marketing message like "Dear John Doe, at 30, you’re eligible for our premium loyalty program."

   - Print the message for use in email campaigns.

· Sample Input -

         Customer Name: John Doe         Customer Age: 30     

           

· Sample Output -

         Dear John Doe, at 30, you’re eligible for our premium loyalty program.

Task 3: Product List Management

Objective: Efficient management of the product list is essential for inventory control.

Ø Given a list of product prices, extract the highest and lowest prices.

Ø Create a new list with the mid-range products.

Ø Add a new premium product price to the list and print the updated list for the inventory team.

 

· Sample Input

         product_prices = [50, 120, 30, 200, 90, 150, 180]

          premium_product_price = 250

· Sample Output

          Highest Price: 200

          Lowest Price: 30                                 

          Mid-Range Products: [50, 120, 90, 150, 180]

          Updated Product List with Premium Price: [50, 120, 30, 200, 90, 150, 180, 250]      

 

 

 Task 4: Inventory Lookup

Objective: Quick access to product details is important for customer service representatives.

Ø Create a dictionary storing key information about a product (e.g., `product_name`, `SKU`, `price`, `category`).

Ø Print the product name and SKU when queried by a customer service representative.

 

· Sample Input

product_info = { "product_name": "Wireless Mouse", "SKU": "WM-12345", "price": 25.99, "category": "Electronics" }

 

· Sample Output

        Product Name: Wireless Mouse                       Product SKU: WM-12345

Task 5: Stock Level Alert System

Objective: Ensuring that stock levels are maintained is critical to avoid stockouts.

Ø Write the code that takes the stock level as input.

Ø  If stock is below a certain threshold, print a "Reorder Now" alert. If stock is above the threshold, print "Stock is sufficient."

· Sample Input

Stock Level: 10                                       Threshold: 20

 

 

· Sample Output

         Enter stock level: 10     

          Reorder Now                                     

                                                                                     OR

         Enter stock level: 25

         Stock is sufficient

 

Task 6: Sales Report Formatting

Objective: Formatting the sales data for management reports is crucial.

Ø Given a list of products sold, print each product name in uppercase for better visibility in reports.

Ø Implement both a `for` loop and a `while` loop for this task to ensure code flexibility.

 

· Sample Input

products_sold = ["laptop", "mouse", "keyboard", "monitor", "printer"]

 

· Sample Output

        WIRELESS MOUSE

         KEYBOARD

         HEADPHONES

         MONITOR

         LAPTOP

 

 

Task 7: Area Calculation for Store Layout

Objective: Accurate area calculations are needed to plan new store layouts.

Ø Create a function that calculates the area of a section of the store based on length and width.

Ø Use this function to calculate and print the area of several store sections.

 

· Sample Input

 def main():

  length1, width1 = 20, 15

 print(f"The area of section 1 is {calculate_area(length1, width1)}  square meters.")

 

· Sample Output

         The area of section 1 is 300 square meters.

 

Task 8: Customer Feedback Analysis

Objective: Analyzing customer feedback is vital to improving service.

· Write the code to count the number of vowels in a customer feedback message.

·  Also, reverse the feedback message for a unique data presentation in reports.

 

· Sample Input

        "I loved the fast and friendly service!"

· Sample Output

         Customer Feedback Analysis:

         Original Feedback: The service was excellent and very quick!

         Number of Vowels: 13

         Reversed Feedback: !kciuq yrev dna tnellecxe saw ecivres ehT

 

Task 9: Price Filtering Tool

Objective: Filtering product prices helps in creating targeted discounts.

Ø Use list comprehension to filter out products priced below a certain threshold from the product list.

Ø Print the list of eligible products for a discount campaign.

 

· Sample Input

        product_prices = [150, 85, 300, 120, 45, 200]

        Discount Threshold: 100

 

· Sample Output

        Products eligible for the discount campaign: [85, 45]

 

Task 10: Sales Log File Management

Objective: Proper management of sales log files is necessary for compliance and audit purposes.

Ø Create a text file named `sales_log.txt` to store daily sales summaries.

Ø Write two lines summarizing the daily sales performance.

Ø Read and print the content of the file to ensure data integrity.

 

· Sample Input

        Daily Sales Summary Line 1: "Total sales today: $12,345."

        Daily Sales Summary Line 2: "Number of transactions: 123."

 

· Sample Output

        Content of 'sales_log.txt':

        Total sales today: $12,345.

        Number of transactions: 123.

 

Task 11: Daily Sales Average

Objective: Calculate the average daily sales for the past week.

Ø Given a list of sales figures for the last 7 days, calculate the average sales.

Ø Print the average sales to help the finance team understand the weekly performance.

 

· Sample Input

        daily_sales = [1200, 1500, 1100, 1800, 1700, 1600, 1400]

· Sample Output

       Average Daily Sales for the Past Week: $1471.43

 

Task 12: Customer Segmentation

Objective: Categorize customers based on their total spending.

Ø Create a list of customer spending amounts.

Ø Use a loop to categorize customers as "Low", "Medium", or "High" spenders based on their spending amount.

Ø Print the categorized results to assist in targeted marketing.

 

· Sample Input

        Customer Categorization Criteria:

        - Low: Spending < $500

       - Medium: $500 <= Spending < $1500

       - High: Spending >= $1500

 

         Customer Spendings: [200, 800, 1500, 3000, 450, 1200]      

 

 

· Sample Output

        Customer Spending Categories:

        Customer 1: Spending = $200 -> Category: Low

        Customer 2: Spending = $800 -> Category: Medium

        Customer 3: Spending = $1500 -> Category: High

        Customer 4: Spending = $3000 -> Category: High

        Customer 5: Spending = $450 -> Category: Low

        Customer 6: Spending = $1200 -> Category: Medium

 

Task 13: Discount Calculation

Objective: Automate the calculation of discounts for a promotional campaign.

Ø Write a code that calculates the final price after applying a discount percentage to a product’s original price.

Ø Test this function on a list of products with different discounts and print the final prices.

 

· Sample Input

 

products = [ {"name": "Product A", "original_price": 100, "discount_percentage": 10}, {"name": "Product B", "original_price": 250, "discount_percentage": 20}, {"name": "Product C", "original_price": 75, "discount_percentage": 15}, {"name": "Product D", "original_price": 150, "discount_percentage": 5} ]

 

· Sample Output

        Final Prices After Discounts:

       Product 1: Original Price = $100, Discount = 10%, Final Price = $90.00

       Product 2: Original Price = $250, Discount = 20%, Final Price = $200.00

       Product 3: Original Price = $75, Discount = 15%, Final Price = $63.75

       Product 4: Original Price = $150, Discount = 5%, Final Price = $142.50        

 

Task 14: Customer Feedback Sentiment Analysis

Objective: Basic sentiment analysis of customer feedback.

Ø Write the Python code that checks if certain positive or negative words (e.g., "good", "bad", "happy", "disappointed") are present in customer feedback.

Ø Print "Positive" or "Negative" based on the words found in the feedback.

 

· Sample Input

 

Customer Feedback: "I am very happy with the service. It was a good experience!"

Positive Words: ["good", "happy", "excellent", "great"]

Negative Words: ["bad", "disappointed", "poor", "terrible"]

· Sample Output

        Customer Feedback Sentiment: Positive

 

 Task 15: Employee Salary Increment Calculator

 

Objective: Calculate the salary increment for employees based on their performance rating.

Ø Create a dictionary that stores employee names and their performance ratings.

Ø Write the code that applies a different increment percentage based on the rating.

Ø Print the updated salary for each employee.

 

· Sample Input

 employees = { "Alice": {"current_salary": 50000, "rating": "Excellent"}, "Bob":     {"current_salary": 40000, "rating": "Good"}, "Charlie": {"current_salary": 45000, "rating": "Average"}, "David": {"current_salary": 35000, "rating": "Poor"} }

 

increments = { "Excellent": 20, "Good": 15, "Average": 10, "Poor": 5 }

 

· Sample Output

        Updated Salaries After Increment:

        Alice: Current Salary = $50000, Rating = Excellent, Updated Salary = $60000.00

        Bob: Current Salary = $40000, Rating = Good, Updated Salary = $46000.00

        Charlie: Current Salary = $45000, Rating = Average, Updated Salary = $49500.00

        David: Current Salary = $35000, Rating = Poor, Updated Salary = $36750.00

 

Task 16: Monthly Sales Report Generator

 

Objective: Generate a simple text-based monthly sales report.

Ø Create a list of daily sales figures for a month.

Ø Calculate the total and average sales for the month.

Ø Write these statistics to a text file named monthly_report.txt.

 

· Sample Input

daily_sales = [ 200, 250, 300, 400, 350, 500, 450, 300, 250, 400, 200, 300, 450, 500, 400, 250, 350, 300, 450, 400, 250, 300, 200, 400, 350, 300, 500, 450, 300, 250 ]

 

· Sample Output

        Monthly Sales Report

         ---------------------

        Total Sales: $10500                                 Average Daily Sales: $350.00

 

Task 17: Stock Replenishment Planning

 

Objective: Determine which products need replenishment based on sales data.

Ø Given a list of products and their current stock levels, compare these against a predefined threshold.

Ø Print a list of products that need to be reordered to maintain adequate stock levels.

 

· Sample Input

products = [ {"product_name": "Product A", "stock": 50}, {"product_name": "Product B", "stock": 150}, {"product_name": "Product C", "stock": 30}, {"product_name": "Product D", "stock": 75}, {"product_name": "Product E", "stock": 20} ]

threshold = 40

 

· Sample Output

        Products that need replenishment:

        Product C

        Product E

 

Task 18: Data Cleaning Utility

 

Objective: Create a utility to clean customer names for better data consistency.

Ø Write the code that takes a list of customer names with extra spaces and inconsistent capitalization.

Ø Clean the names by trimming spaces and standardizing the capitalization (e.g., "JOHN DOE" -> "John Doe").

Ø Print the cleaned names for database entry.

 

· Sample Input

customer_names = [ " john doe ", " MARY SMITH ", " aLICE JOHNSON ", "bOB WHITE" ]

 

· Sample Output

      Cleaned Customer Names for Database Entry:

        John Doe

        Mary Smith

        Alice Johnson

        Bob White



Task 19: Simple Sales Forecasting

 

Objective: Implement a basic forecasting model for next month’s sales.

Ø Based on the average sales of the last 3 months, predict next month’s sales using a simple average.

Ø Print the forecasted sales figures for budget planning.

 

· Sample Input

Def main():

sales_last_3_months = [20000, 22000, 25000]

 

· Sample Output

        Forecasted Sales for Next Month: $12950.00

 

Task 20: Customer Loyalty Points Calculator

 

Objective: Calculate loyalty points for customers based on their purchases.

Ø Write a code that assigns loyalty points to customers based on their total purchase amount.

Ø Implement a tiered system where different spending levels earn different point multipliers.

Ø Print the loyalty points for a list of customers.

 

· Sample Input

Customers and Their Total Purchases:

 - John Doe: $250

- Jane Smith: $500

 - Alice Johnson: $1000

 - Bob White: $150

 

· Sample Output

       Customer Loyalty Points:

       John Doe: $250 Purchase, Loyalty Points: 375.0

       Jane Smith: $500 Purchase, Loyalty Points: 1000.0

       Alice Johnson: $1000 Purchase, Loyalty Points: 2000.0

       Bob White: $150 Purchase, Loyalty Points: 150.0



Project Submission Guidelines:

- Create a Python notebook file and have all the questions answered.

- Ensure that the scripts are well-commented and follow coding best practices.

- Submit all scripts in a single compressed folder named `XYZ_Retail_Project.zip`.

Evaluation Criteria:

- Correctness and functionality of the scripts.

- Code readability and documentation.

- Relevance and accuracy of the output generated by the scripts.

Submission Instructions:
To submit your assignment, please follow these guidelines:

- Ensure that your assignment is fully completed.

- Push your assignment to a GitHub repository.

- Share the repository link by including it in a text, Word, or PDF file format.

Submit the file/text containing the repository link via Vlearn.
