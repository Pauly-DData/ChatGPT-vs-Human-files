import pandas as pd
from radon.metrics import h_visit

# Define the Halstead complexity calculation function
def calculate_halstead(code):
    # Check if code is a string
    if not isinstance(code, str):
        return None
    # Remove comments
    code = "\n".join(line for line in code.splitlines() if not line.strip().startswith("#"))
    # Wrap the code in a function definition
    wrapped_code = "def func():\n" + "\n".join("\t" + line for line in code.splitlines())
    try:
        h = h_visit(wrapped_code)
        return h.total
    except:
        return None

# Load the Excel file
df = pd.read_excel('Randon_final_doc.xlsx')

# Assume 'Code' is the column containing the code snippets
df['Halstead'] = df['code'].apply(calculate_halstead)

# Save the result back to the Excel file
df.to_excel('output_with_halstead_github.xlsx', index=False)
