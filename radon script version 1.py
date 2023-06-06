import pandas as pd
import os
import tempfile
from radon.complexity import cc_visit
from radon.raw import analyze
from radon.metrics import h_visit, mi_visit

# Read the Excel file
file_path = 'C:/Users/1948NM/Documents/Technische bedrijfskunde/Jaar 2 - 2017 -2019/Blok 1/Programmeren en visualiseren/radon_test.xlsx'
sheet_name = 'Sheet1'
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Assuming code snippets are in a column named 'code'
for index, row in df.iterrows():
    code_snippet = row['code']

    # Create a temporary Python file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as temp_file:
        temp_file.write(code_snippet)
        temp_file_name = temp_file.name

    # Analyze the temporary Python file with Radon
    with open(temp_file_name, 'r') as temp_file:
        code = temp_file.read()
        complexity = cc_visit(code)
        raw_metrics = analyze(code)
        halstead_metrics = h_visit(code)
        maintainability_index = mi_visit(code, raw_metrics)

    # Print results
    print(f'Code snippet {index}:')
    print('Cyclomatic Complexity:', complexity)
    print('Raw Metrics:', raw_metrics)
    print('Halstead Metrics:', halstead_metrics)
    print('Maintainability Index:', maintainability_index)

    # Remove the temporary file
    os.remove(temp_file_name)


