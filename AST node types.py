import ast
from collections import Counter

code_snippet1 = """
import pandas as pd

df = pd.read_csv('dob_job_application_filings_subset.csv')

print(df.head())

print(df.tail())

print(df.shape)

print(df.columns)
"""

code_snippet2 = """ 

# Import pandas
import pandas  as pd
# Read the file into a DataFrame: df
df = pd.read_csv('dob_job_application_filings_subset.csv')
# Print the head of df
print(df.head())
# Print the tail of df
print(df.tail())
# Print the shape of df
print(df.shape)
# Print the columns of df
print(df.columns)
# Print the head and tail of df_subset
print(df_subset.head())
print(df_subset.tail())
#Further diagnosis      

"""

def analyze_code_structure(code_snippet):
    node_types = []

    try:
        tree = ast.parse(code_snippet)
        for node in ast.walk(tree):
            node_types.append(type(node).__name__)
    except Exception as e:
        print(f"Error processing snippet: {e}")

    return Counter(node_types)

counter1 = analyze_code_structure(code_snippet1)
counter2 = analyze_code_structure(code_snippet2)

print("Code snippet 1 AST node types:")
for node_type, count in counter1.items():
    print(f"{node_type}: {count}")

print("\nCode snippet 2 AST node types:")
for node_type, count in counter2.items():
    print(f"{node_type}: {count}")
