import csv
import os

# Adding comment for next branch

# ETL: Extract, Transform, Load for employees.csv
input_file = 'employees.csv'
output_file = 'employees_transformed.csv'
input_path = os.path.join(os.path.dirname(__file__), input_file)
output_path = os.path.join(os.path.dirname(__file__), output_file)

# Extract
with open(input_path, 'r', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = list(reader)

# Transform: Capitalize names in the first column (assuming header row exists)
for i, row in enumerate(rows):
    if i == 0:
        continue  # skip header
    if row and len(row) > 0:
        row[0] = row[0].capitalize()
#Test comment

# Another test comment
print("HELLO")

# Load
with open(output_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

# Another test comment
