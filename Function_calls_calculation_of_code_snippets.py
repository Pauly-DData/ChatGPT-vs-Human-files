import ast

class FunctionCallAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.function_calls = {}

    def visit_Call(self, node):
        func_name = self._get_func_name(node)
        if func_name:
            self.function_calls[func_name] = self.function_calls.get(func_name, 0) + 1
        self.generic_visit(node)

    def _get_func_name(self, node):
        if isinstance(node.func, ast.Name):
            return node.func.id
        elif isinstance(node.func, ast.Attribute):
            return node.func.attr
        return None

def analyze_function_calls(code_snippet):
    tree = ast.parse(code_snippet)
    analyzer = FunctionCallAnalyzer()
    analyzer.visit(tree)
    return analyzer.function_calls

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

function_calls1 = analyze_function_calls(code_snippet1)
function_calls2 = analyze_function_calls(code_snippet2)

print("Function calls in code snippet 1:")
for func_name, count in function_calls1.items():
    print(f"{func_name}: {count}")

print("\nFunction calls in code snippet 2:")
for func_name, count in function_calls2.items():
    print(f"{func_name}: {count}")
