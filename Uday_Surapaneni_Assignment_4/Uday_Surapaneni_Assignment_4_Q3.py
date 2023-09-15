#!/usr/bin/env python
# coding: utf-8

#Q3
import pandas as pd
import os

# 1. Extract Date from file path
folder_path = "C:/Users/CZ649VD/OneDrive - EY/Training materials/Python Training/Session 7/Uday_Surapaneni_Assignments/Uday_Surapaneni_Assignment_4/Question3"

# 2. List Excel files in the folder
files = [file for file in os.listdir(folder_path) if file.endswith(".xlsx")]
dates = [file.split("_")[0] for file in files]

# Initialize empty lists for other fields
data = []

# 2. Extract Rating, Region, mu, and sigma from each file
for file in files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_excel(file_path)
    
    for index, row in df.iterrows():
        rating = row['Rating']
        for col in df.columns:
            if col.endswith("_mu"):
                region = col.split("_")[0]
                mu = row[col]
                sigma_col = col.replace("_mu", "_sigma")
                sigma = row[sigma_col]
                
                data.append({
                    'Date': file.split("_")[0],
                    'Rating': rating,
                    'Region': region,
                    'mu': mu,
                    'sigma': sigma
                })

# Create a new DataFrame with the extracted fields
df_new = pd.DataFrame(data)

# Load the existing data from the "extracted_fields.xlsx" file
try:
    df_existing = pd.read_excel("extracted_fields.xlsx")
    # Append the new data to the existing DataFrame
    df_combined = pd.concat([df_existing, df_new], ignore_index=True)
except FileNotFoundError:
    # If the file doesn't exist, use the new DataFrame
    df_combined = df_new

# Save the combined DataFrame as an Excel file
output_file = "extracted_fields.xlsx"
df_combined.to_excel(output_file, index=False, engine='openpyxl')

