#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis

# Task 1: Load the dataset
sales_data=pd.read_csv('sales_data.csv')
sales_data.shape
sales_data.info()
sales_data.head()

# Task 2: Data cleaning
#Null values check
(sales_data.isnull().sum()/len(sales_data))*100
#No null values on the dataset
#Duplicate values check
sales_data.nunique()
sales_data.drop_duplicates(inplace=True)
sales_data.info()
#22 duplicate rows were removed

# Splitting the Customer column into city, state, and zipcode
split_data = sales_data['Customer'].str.split(', ', expand=True)
sales_data['Address'] = split_data[0]
sales_data['City'] = split_data[1].apply(lambda x: x.split(', ')[0])
sales_data[['State', 'Zipcode']] = split_data[2].str.split(' ', expand=True)
sales_data.head()

#New features like address,city,state and zipcode was added as part of feature engineering.Sales Revenue feature was also added as a part of the data analysis
# Mean, median, and standard deviation of Quantity and Price columns
summary_stats = sales_data[['Quantity', 'Price']].describe()
print(summary_stats)

# Skewness and kurtosis of Quantity distribution
quantity_skewness = skew(sales_data['Quantity'])
quantity_kurtosis = kurtosis(sales_data['Quantity'])
print("Quantity Skewness:",quantity_skewness)
print("Quantity Kurtosis:",quantity_kurtosis)

# Total sales revenue
sales_data['Sales Revenue'] = sales_data['Quantity'] * sales_data['Price']
total_revenue = sales_data['Sales Revenue'].sum()
print("Total sales revenue:",total_revenue)


# Task 4: Data visualization
# Histogram and Density plot of Quantity column
sns.histplot(sales_data['Quantity'], kde=True)
plt.title("Distribution of Sales Quantities")
plt.xlabel("Quantity")
plt.ylabel("Density")
plt.text(0.7, 0.9, f"Skewness: {quantity_skewness:.2f}\nKurtosis: {quantity_kurtosis:.2f}", transform=plt.gca().transAxes)
plt.show()

# Scatter plot of Price vs. Quantity
sns.scatterplot(x='Quantity', y='Price', data=sales_data)
plt.title("Price vs. Quantity")
plt.xlabel("Quantity")
plt.ylabel("Price")
correlation_coefficient = sales_data['Quantity'].corr(sales_data['Price'])
plt.text(0.7, 0.9, f"Correlation Coefficient: {correlation_coefficient:.2f}", transform=plt.gca().transAxes)
plt.show()

"""Insights from graph:
1.The quantity distribution is positively skewed with heavier tails(Leptokurtic) in nature
2.There is no significant relationship between Quantity and Price as the correlation between these 2 features are negligible.(Correlation coefficient=-0.15)"""
# Task 5: Categorical analysis
# Group the data by Product and compute total quantity sold and average price for each product
product_sales = sales_data.groupby('Product').agg({'Quantity': 'sum', 'Price': 'mean'})
product_sales['Sales_Revenue']=product_sales['Quantity']*product_sales['Price']
product_sales = product_sales.sort_values(by='Sales_Revenue', ascending=False)
print(product_sales)
# Visualize product-wise sales using a horizontal bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x='Sales_Revenue',y=product_sales.index, data=product_sales, order=product_sales.index)
plt.title("Product-wise Sales")
plt.xlabel("Total Sales")
plt.ylabel("Product")
plt.show()

"""Insights from Bar Graph:
We observe that Macbook Pro Laptop has the highest sales according to the data provided."""
# Task 6: Identify outliers
# Use z-score method to detect potential outliers in Price column
z_scores = (sales_data['Price'] - sales_data['Price'].mean()) / sales_data['Price'].std()
outliers = sales_data[abs(z_scores) > 3]

# Skewness and kurtosis of Price distribution
price_skewness = skew(sales_data['Price'])
price_kurtosis = kurtosis(sales_data['Price'])
print("Price Skewness:",price_skewness)
print("Price Kurtosis:",price_kurtosis)

# Visualize outliers using a vertical box plot
sns.boxplot(x=sales_data['Price'])
plt.title("Price distribution")
plt.xlabel("Price")
plt.text(0.7, 0.9, f"Skewness: {price_skewness:.2f}\nKurtosis: {price_kurtosis:.2f}", transform=plt.gca().transAxes)
plt.show()

"""Insights from Box-plot:
We observe the high number of outliers in price variable which means there are premium products sold as well and price distribution is positively skewed with heavier tails(Leptokurtic distribution)"""

# Task 7: Additional Analysis

# Convert 'Date' column to datetime type
sales_data['Order Date'] = pd.to_datetime(sales_data['Order Date'])

# Calculate weekly sales by aggregating data based on 'Date' column
weekly_sales = sales_data.resample('W', on='Order Date').sum()

# Change the index to "Week 1", "Week 2", etc.
weekly_sales.index = ["Week " + str(i) for i in range(1, len(weekly_sales) + 1)]
print(weekly_sales)

# Visualize weekly sales trend over time using a line plot
plt.plot(weekly_sales.index, weekly_sales['Sales Revenue'])
plt.xlabel('Week')
plt.ylabel('Sales Revenue')
plt.title('Weekly Sales Trend')
plt.show()

"""Insights from Line-plot:
We noticed a decline in total sales revenue during week 2, followed by a rebound in sales revenue during week 3. Sales growth remained stagnant in week 4, and there was an abrupt revenue drop in week 5"""