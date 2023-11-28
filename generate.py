import csv
import json

# Read pizza data from CSV file
# Read CSV file
with open('pizza_data.csv', 'r') as f:
    data = list(csv.reader(f))
    headers = data[0]
    data = data[1:]

# Create prompt and completion pairs
pairs = []
for row in data:
    prompt = f"Generate a summary for the following pizza:\nCompany: {row[headers.index('Company')]}\nPizza Name: {row[headers.index('Pizza Name')]}\nType: {row[headers.index('Type')]}\nSize: {row[headers.index('Size')]}\nPrice: {row[headers.index('Price')]}"
    completion = f"{row[headers.index('Company')]} offers a '{row[headers.index('Pizza Name')]}' pizza, which is a '{row[headers.index('Type')]}' type, available in '{row[headers.index('Size')]}' size, priced at {row[headers.index('Price')]}."
    pairs.append({"prompt": prompt, "completion": completion})

# Export to JSON file
with open('prompt_completion_pairs.json', 'w') as f:
    json.dump(pairs, f)


