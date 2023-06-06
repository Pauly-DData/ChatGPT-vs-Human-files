import pandas as pd
from radon.metrics import h_visit


def calculate_max_indent(code):
    # Check if code is a string
    if not isinstance(code, str):
        return None
    # Remove comments
    code = "\n".join(line for line in code.splitlines() if not line.strip().startswith("#"))
    # Split the code into lines and compute the indentation level of each line
    lines = code.split('\n')
    indent_levels = [len(line) - len(line.lstrip()) for line in lines]
    # The maximum indentation level is the maximum depth of nested blocks
    max_indent = max(indent_levels)
    return max_indent

# Load the Excel file
df = pd.read_excel('Randon_final_doc.xlsx')

# Assume 'Code' is the column containing the code snippets
df['Nested Depth'] = df['code'].apply(calculate_max_indent)

# Save the result back to the Excel file
df.to_excel('output_with_nested_depth_github.xlsx', index=False)
