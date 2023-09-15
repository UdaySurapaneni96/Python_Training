#!/usr/bin/env python
# coding: utf-8
import pandas as pd
from datetime import datetime
# Read the CSV file into a DataFrame
df = pd.read_csv('Assignment_4_Question_1.csv')

# Remove commas from the "Sale_amt" column
df['Sale_amt'] = df['Sale_amt'].str.replace(',', '')

# Convert the "Sale_amt" column to float
df['Sale_amt'] = df['Sale_amt'].astype(float)

# Group the data by region and count the number of orders in each region
region_orders = df.groupby('Region')['Sale_amt'].count()

# Find the region with the maximum number of orders
max_orders_region = region_orders.idxmax()

print("The region delivering maximum orders is:", max_orders_region)


# Group the data by manager and calculate the average sale amount for each manager
manager_performance = df.groupby('Manager')['Sale_amt'].mean()

# Divide the sales amount into 4 bins and assign ratings from A to D
bins = pd.qcut(manager_performance, q=4, labels=['D', 'C', 'B', 'A'])

# Create a DataFrame to store the manager ratings and average sales_amount
ratings_df = pd.DataFrame({'Manager': manager_performance.index, 'Rating': bins, 'Average_Sale_Amount': manager_performance.values})

# Sort the DataFrame by average sales_amount in descending order
ratings_df = ratings_df.sort_values('Average_Sale_Amount', ascending=False)

# Reset the index of the DataFrame
ratings_df = ratings_df.reset_index(drop=True)

# Print the sorted ratings
print("Sorted Manager Ratings:")
print(ratings_df)

# Check for missing values 
print(df.isnull().sum())
df.drop('Unnamed: 0',axis=1,inplace=True)
# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Convert OrderDate column to datetime
df['OrderDate'] = pd.to_datetime(df['OrderDate'],format='%m-%d-%y')

print("Data cleaning and preprocessing completed.")

# Calculate the number of days from today's date
df["DaysOld"] = (datetime.today() - df["OrderDate"]).dt.days

df.head()

# Create a Pivot table
pivot_table_1 = pd.pivot_table(df, values=["Sale_amt"], index=["Manager"], aggfunc={"Sale_amt": [len, "mean"]})

print(pivot_table_1)

# Filter the data for Manager = "Douglas"
filtered_data = df[df["Manager"] == "Douglas"]

# Create a Pivot table
pivot_table_2 = pd.pivot_table(filtered_data, values=["Sale_amt"], index=["Region", "Manager", "SalesMan"], aggfunc={"Sale_amt": sum})

print(pivot_table_2)

# Keep rows with at most two NaNs
df = df.dropna(thresh=3)

print("Rows with at most two NaNs:")
print(df)

# Group by Region, Manager, SalesMan, Item and calculate the sum of Sale_amt
grouped_data = df.groupby(["Region", "Manager", "SalesMan", "Item"])["Sale_amt"].sum()

# Sort the groups based on the sum of Sale_amt
sorted_data = grouped_data.sort_values(ascending=False)

print(sorted_data)

# Split the dataframe into groups based on region
groups = df.groupby("Region")

# Set Manager, Salesman, and Item column values into a list of values
result = groups.apply(lambda x: x[["Manager", "SalesMan", "Item"]].values.tolist())

print(result)

# Check if OrderDate is a business day
df["IsBusinessDay"] = df["OrderDate"].dt.weekday < 5

print(df[["OrderDate", "IsBusinessDay"]])


