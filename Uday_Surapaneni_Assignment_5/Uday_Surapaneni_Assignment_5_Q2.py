#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis


# Load the dataset
supermarket_sales = pd.read_csv('supermarket_sales.csv')

supermarket_sales.shape
supermarket_sales.info()
supermarket_sales.head()

# Task 2: Data cleaning
#Null values check as percentage
(supermarket_sales.isnull().sum()/len(supermarket_sales))*100

#No null values on the dataset
#Duplicate values check
supermarket_sales.nunique()
supermarket_sales.drop_duplicates(inplace=True)
supermarket_sales.info()

#No duplicate values on the dataset
#Q1: What does the customer rating look like and is it skewed?
#Answer - The customer rating exhibits a nearly symmetrical distribution with a tendency toward being flat or less peaked in its nature.

# Skewness and kurtosis of Customer Ratings distribution
ratings_skewness = skew(supermarket_sales['Rating'])
ratings_kurtosis = kurtosis(supermarket_sales['Rating'])
print("Customer Ratings Skewness:", ratings_skewness)
print("Customer Ratings Kurtosis:", ratings_kurtosis)

# Plot the distribution of customer ratings
sns.histplot(supermarket_sales['Rating'], kde=True)
plt.title('Distribution of Customer Ratings')
plt.xlabel('Rating')
plt.ylabel("Density")
plt.text(0.7, 0.9, f"Skewness: {ratings_skewness:.2f}\nKurtosis: {ratings_kurtosis:.2f}", transform=plt.gca().transAxes)
plt.show()

#Q2: Is there any difference in aggregate sales across branches?
#Answer- The aggregrate sales in 3 branches are consistent among branchs.Branch C having slightly higher sales than other 2 branches.

# Group the data by branch and calculate the total sales
branch_sales = supermarket_sales.groupby('Branch')['Total'].sum()
print(branch_sales)
# Plot the aggregate sales across branches
sns.barplot(x=branch_sales.index, y=branch_sales.values)
plt.title('Aggregate Sales across Branches')
plt.xlabel('Branch')
plt.ylabel('Total Sales')
plt.show()

#Q3: Which is the most popular payment method used by customers?
#Answer-The most popular payment method in this dataset is Ewallet mode of payment followed by Cash payment.Infact both the payment methods were used consistently to purchase the product.

# Count the occurrences of each payment method
payment_counts = supermarket_sales['Payment'].value_counts()
print(payment_counts)

# Plot the payment method popularity
sns.barplot(x=payment_counts.index, y=payment_counts.values)
plt.title('Payment Method Popularity')
plt.xlabel('Payment Method')
plt.ylabel('Count')
plt.show()

#Q4: Does gross income affect the ratings that the customers provide?
#Answer- Gross income doesn't affect customer ratings as there is no correlation between each other.Impact of Gross income can have various other factors like COGS,quantity sold etc.

# Plot the relationship between gross income and ratings
sns.scatterplot(x=supermarket_sales['gross income'], y=supermarket_sales['Rating'])
plt.title('Gross Income vs Rating')
plt.xlabel('Gross Income')
plt.ylabel('Rating')
correlation_coefficient = supermarket_sales['gross income'].corr(supermarket_sales['Rating'])
plt.text(0.9, 0.9, f"Correlation Coefficient: {correlation_coefficient:.2f}", transform=plt.gca().transAxes)
plt.show()

#Q5: Which branch is the most profitable?
#Answer-The gross income in 3 branches are consistent among branchs.Branch C having slightly higher gross income than other 2 branches.

# Group the data by branch and calculate the total gross income
branch_income = supermarket_sales.groupby('Branch')['gross income'].sum()
print(branch_income)

# Plot the total gross income across branches
sns.barplot(x=branch_income.index, y=branch_income.values)
plt.title('Total Gross Income across Branches')
plt.xlabel('Branch')
plt.ylabel('Total Gross Income')
plt.show()

#Q6: Is there any time trend in gross income?
#Answer-There is no discernible pattern over time in relation to gross income.

# Convert the Date column to datetime format
supermarket_sales['Date'] = pd.to_datetime(supermarket_sales['Date'])

# Group the data by date and calculate the total gross income
date_income = supermarket_sales.groupby('Date')['gross income'].sum()

# Plot the time trend of gross income
plt.plot(date_income.index, date_income.values)
plt.title('Time Trend of Gross Income')
plt.xlabel('Date')
plt.ylabel('Gross Income')
plt.xticks(rotation=45)
plt.show()

#Q7: Which product line generates most income?
#Answer- The product line which generates most income was "Food and Beverages" followed by "Electronic accessories" and "Fashion accessories".

# Group the data by product line and calculate the total gross income
product_income = supermarket_sales.groupby('Product line')['gross income'].sum()
print(product_income)
# Plot the total gross income by product line
sns.barplot(x=product_income.index, y=product_income.values)
plt.title('Total Gross Income by Product Line')
plt.xlabel('Product Line')
plt.ylabel('Total Gross Income')
plt.xticks(rotation=45)
plt.show()

#Q8: Show the correlation between all variables
#Answer- Heatmap is the visual representation of correlation matrix between all the variables.There was strong correlation between quantity and gross income.

# Calculate the correlation matrix
supermarket_sales.drop('gross margin percentage',axis=1,inplace=True)
numeric_columns = supermarket_sales.select_dtypes(include='number')
correlation_matrix = numeric_columns.corr()

# Plot the correlation matrix using a heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

