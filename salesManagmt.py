# Sales Management Program in Python

import pandas as pd


# Defining the sales data as a dictionary
sales_data = {
'product_name': ['Product 1', 'Product 2', 'Product 3', 'Product 4', 'Product 5'],
'quantity_sold': [100, 200, 150, 300, 400],
'unit_price': [10, 20, 15, 25, 30],
'total_revenue': [1000, 4000, 2250, 7500, 12000]
}

# Creating a dataframe from the sales data
sales_df = pd.DataFrame(sales_data)

# Function to calculate the total revenue for a specific product
def total_revenue(product_name):
revenue = sales_df.loc[sales_df['product_name'] == product_name, 'total_revenue'].sum()
return revenue

# Function to calculate the total quantity sold for a specific product
def total_quantity_sold(product_name):
quantity = sales_df.loc[sales_df['product_name'] == product_name, 'quantity_sold'].sum()
return quantity

# Function to calculate the average unit price for a specific product
def average_unit_price(product_name):
average_price = sales_df.loc[sales_df['product_name'] == product_name, 'unit_price'].mean()
return average_price

# Testing the functions
print("Total revenue for Product 1: ", total_revenue("Product 1"))
print("Total quantity sold for Product 2: ", total_quantity_sold("Product 2"))
print("Average unit price for Product 3: ", average_unit_price("Product 3"))
