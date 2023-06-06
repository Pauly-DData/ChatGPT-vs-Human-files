import pandas as pd
from collections import defaultdict

# Read the Excel file
filename = "Randon_final_AST_type_full.xlsx"
sheet_name = "chatgpt"

# Load the data into a pandas DataFrame
df = pd.read_excel(filename, sheet_name=sheet_name)

# Process the data
result = defaultdict(int)
for _, row in df.iterrows():
    for entry in row:
        if pd.notna(entry):
            entry = str(entry)  # Convert numeric values to strings
            pairs = entry.split(", ")
            for pair in pairs:
                word, count = pair.split(": ")
                result[word] += int(count)

# Print the total count per word
for word, count in result.items():
    print(f"{word}: {count}")

