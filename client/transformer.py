import numpy as np
import pandas as pd
import json

# Read the CSV file
df = pd.read_csv('data.csv', encoding='latin-1')

# Convert InvoiceDate to datetime with dayfirst set to True
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format="%m/%d/%y %H:%M", errors='coerce')

# Check for any invalid dates and handle them if necessary
if df['InvoiceDate'].isnull().any():
    print("Warning: Some dates could not be parsed. Check the 'InvoiceDate' column for invalid entries.")

# Format the InvoiceDate to the desired string format
df['InvoiceDate'] = df['InvoiceDate'].dt.strftime("%d/%m/%Y %H:%M")

# Convert the DataFrame to JSON format
df['json'] = df.to_json(orient='records', lines=True).splitlines()

# Remove backslashes from the JSON strings
df['json'] = df['json'].str.replace(r'\\/', '/', regex=True)

# Just take the json column of the dataframe
dfjson = df['json']
print(dfjson)

# Print out the dataframe to a file
np.savetxt(r'./output.txt', dfjson.values, fmt='%s')