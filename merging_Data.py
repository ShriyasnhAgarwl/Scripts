import pandas as pd
import os

# List all CSV files in the directory
csv_files = [file for file in os.listdir() if file.endswith('.csv')]

# Initialize an empty list to store dataframes
dfs = []

# Read each CSV file and append its dataframe to the list
for file in csv_files:
    df = pd.read_csv(file)
    dfs.append(df)

# Concatenate all dataframes into one
merged_df = pd.concat(dfs, ignore_index=True)

# Write the merged dataframe to a new CSV file
merged_df.to_csv('File_Name.csv', index=False) //File Name nahi bataungaa

print("Merged file created successfully!")
