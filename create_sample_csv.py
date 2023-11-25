import csv
import random

# Create a list of groups (A-J) and variables (v1-v10)
groups = [chr(65 + i) for i in range(10)]  # A-J
variables = [f'v{i}' for i in range(1, 11)]  # v1-v10

# Create a list of dictionaries with 'group', 'variable', and 'value' columns
data = [{'group': group, 'variable': variable, 'value': random.randint(0, 100)} for group in groups for variable in variables]

# Define the CSV file name
csv_file = 'data.csv'

# Write the data to the CSV file
with open(csv_file, 'w', newline='') as file:
    fieldnames = ['group', 'variable', 'value']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(data)

print(f'CSV file "{csv_file}" has been created.')
