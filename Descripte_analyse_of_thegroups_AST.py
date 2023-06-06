import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel file
df = pd.read_excel('Randon_final_AST_type_full.xlsx', engine='openpyxl')

# A function to parse the node strings into a dictionary
def parse_nodes(node_string):
    node_dict = {}
    if pd.notna(node_string):  # check if the value is not NaN
        nodes = node_string.split(', ')
        for node in nodes:
            node_type, node_count = node.split(': ')
            node_dict[node_type] = int(node_count)
    return node_dict

# Apply the function to each row in your column
df['parsed_nodes'] = df['github_result'].apply(parse_nodes)

# Split parsed_nodes column into separate columns
df_nodes = df['parsed_nodes'].apply(pd.Series)

# Fill NaN values with zeros
df_nodes.fillna(0, inplace=True)

# Define node groups
node_groups = {
    'Program Structure': ['Module', 'arguments', 'arg'],
    'Import Statements': ['Import', 'ImportFrom', 'alias'],
    'Control Flow': ['If', 'For', 'While', 'Try', 'ExceptHandler', 'With', 'withitem', 'Break'],
    'Data Structures': ['Tuple', 'List', 'Dict'],
    'Comprehensions': ['ListComp', 'SetComp', 'DictComp', 'comprehension', 'GeneratorExp'],
    'Expressions': ['Expr', 'Call', 'Name', 'Constant', 'Attribute', 'Subscript', 'Index', 'Slice', 'ExtSlice', 'JoinedStr', 'FormattedValue', 'IfExp', 'Lambda', 'Yield'],
    'Assignments': ['Assign', 'AugAssign'],
    'Return Statements': ['Return'],
    'Comparison Operators': ['Compare', 'Eq', 'GtE', 'LtE', 'Gt', 'Lt', 'NotEq', 'In', 'NotIn'],
    'Binary Operators': ['BinOp', 'Add', 'Sub', 'Mult', 'Div', 'Mod', 'Pow', 'BitAnd'],
    'Unary Operators': ['UnaryOp', 'USub', 'Not'],
    'Boolean Operators': ['BoolOp', 'And', 'Or'],
    'Miscellaneous': ['Store', 'Load', 'keyword', 'Assert', 'Starred', 'Delete', 'Del', 'Nonlocal', 'Raise']
}

# Create a new DataFrame with the grouped nodes
df_grouped_nodes = pd.DataFrame()

for group, nodes in node_groups.items():
    df_grouped_nodes[group] = df_nodes[nodes].sum(axis=1)

# Boxplot
plt.figure(figsize=(10, 8))
sns.boxplot(data=df_grouped_nodes)
plt.title('Boxplot of Features')
plt.xticks(rotation=90)
plt.show()

# Correlation heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(df_grouped_nodes.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation heatmap')
plt.show()
