import pandas as pd
from radon.complexity import cc_visit

# Define the cyclomatic complexity calculation function
def calculate_cc(code):
    # Remove comments
    code = "\n".join(line for line in code.splitlines() if not line.strip().startswith("#"))
    # Wrap the code in a function definition
    wrapped_code = "def func():\n" + "\n".join("\t" + line for line in code.splitlines())
    try:
        blocks = cc_visit(wrapped_code)
        cc_scores = [b.complexity for b in blocks]
        return sum(cc_scores)
    except:
        return None

# Load the Excel file
df = pd.read_excel('Randon_final_doc.xlsx')
# Assume 'Code' is the column containing the code snippets
df['CC'] = df['code'].apply(calculate_cc)

# Save the result back to the Excel file
df.to_excel('Cyclomatic Complexity__ChatGPT_results.xlsx', index=False)
