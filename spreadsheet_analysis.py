# Basic data analysis on a spreadsheet. The project will use a csv file that
# contains sales data.

# 1. Read the data from the spreadsheet
# 2. Collect all of the sales from each month into a single list
# 3. Output the total sales across all months

import csv

with open('sales.csv', 'r') as sales:
    spreadsheet = csv.DictReader(sales)
    for column in spreadsheet:
        list_of_sales = column['sales']
        print(list_of_sales)
