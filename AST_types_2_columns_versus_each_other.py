import ast
import pandas as pd
from collections import Counter

# Read the excel file
def read_excel_file(file_name, column_names):
    df = pd.read_excel(file_name, engine='openpyxl')
    return df[column_names]

# Analyze the code snippet based on AST node types
def analyze_code_snippet(code_snippet):
    try:
        tree = ast.parse(code_snippet)
        node_types = [type(node).__name__ for node in ast.walk(tree)]
        return Counter(node_types)
    except Exception as e:
        print(f"Error in parsing code snippet: {code_snippet}\nError: {e}")
        return Counter()

# Main function
def analyze_code_in_excel(file_name, column_names, output_file_name):
    data = read_excel_file(file_name, column_names)

    results = []

    for index, row in data.iterrows():
        result_row = {}
        for column_name in column_names:
            code_snippet = row[column_name]

            if pd.isna(code_snippet):  # Ignore empty rows
                continue

            code_snippet = str(code_snippet)  # Convert to string
            node_types = analyze_code_snippet(code_snippet)

            result_row[f"{column_name}_result"] = ", ".join(f"{node_type}: {count}" for node_type, count in node_types.items())
        
        results.append(result_row)

    result_df = pd.DataFrame(results)
    result_df.to_excel(output_file_name, index=False)

# Usage
file_name = "Randon_final_doc.xlsx"
output_file_name = "Randon_final_AST_type_full.xlsx"
column_names = ["github", "chatgpt"]
analyze_code_in_excel(file_name, column_names, output_file_name)
