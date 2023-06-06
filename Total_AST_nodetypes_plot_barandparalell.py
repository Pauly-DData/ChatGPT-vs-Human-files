import matplotlib.pyplot as plt
import numpy as np

# Define all data
categories = [
    ('Program Structure', ['Module', 'ClassDef', 'FunctionDef', 'arguments', 'arg'], [552, 0, 54, 75, 120], [559, 2, 90, 113, 182]),
    ('Import Statements', ['Import', 'ImportFrom', 'alias'], [309, 243, 659], [225, 205, 456]),
    ('Control Flow', ['If', 'For', 'While', 'Try', 'ExceptHandler', 'With', 'withitem', 'Continue', 'Break'], [78, 149, 10, 3, 3, 26, 26, 2, 6], [83, 147, 4, 4, 4, 13, 13, 7, 7]),
    ('Data Structures', ['Tuple', 'List', 'Dict', 'Set'], [200, 336, 52, 2], [280, 336, 64, 1]),
    ('Comprehensions', ['ListComp', 'SetComp', 'DictComp', 'comprehension', 'GeneratorExp'], [29, 1, 1, 35, 4], [34, 1, 1, 39, 3]),
    ('Expressions', ['Expr', 'Call', 'Name', 'Constant', 'Attribute', 'Subscript', 'Index', 'Slice', 'ExtSlice', 'JoinedStr', 'FormattedValue', 'IfExp', 'Lambda', 'Yield'], [1687, 3115, 7805, 3676, 2389, 559, 511, 81, 33, 16, 16, 1, 21, 2], [1702, 3647, 8869, 3901, 2418, 557, 506, 109, 52, 2, 2, 1, 23, 3]),
    ('Assignments', ['Assign', 'AugAssign', 'AnnAssign'], [1590, 41, 2], [1775, 26, 0]),
    ('Return Statements', ['Return'], [53], [67]),
    ('Comparison Operators', ['Compare', 'Eq', 'GtE', 'LtE', 'Gt', 'Lt', 'NotEq', 'In', 'NotIn'], [160, 64, 13, 24, 14, 14, 6, 20, 4], [152, 51, 11, 26, 15, 12, 4, 24, 7]),
    ('Binary Operators', ['BinOp', 'Add', 'Sub', 'Mult', 'Div', 'FloorDiv', 'Mod', 'Pow', 'BitAnd'], [185, 104, 38, 35, 33, 2, 2, 11, 1], [322, 169, 48, 84, 28, 2, 8, 10, 1]),
    ('Unary Operators', ['UnaryOp', 'USub', 'Not'], [40, 33, 7], [63, 59, 4]),
    ('Boolean Operators', ['BoolOp', 'And', 'Or'], [6, 4, 2], [4, 2, 2]),
    ('Miscellaneous', ['Store', 'Load', 'keyword', 'Assert', 'IsNot', 'Is', 'Starred', 'Delete', 'Del', 'Nonlocal', 'Raise'], [2027, 9260, 948, 7, 1, 0, 2, 4, 4, 1, 1], [2248, 10214, 1111, 8, 0, 2, 3, 1, 1, 3, 6])
]

# Append all data into single lists
variables = []
ai_counts = []
github_counts = []
for category, vars, ai, github in categories:
    variables.extend(vars)
    ai_counts.extend(ai)
    github_counts.extend(github)

# Perform min-max normalization, adding a small epsilon to avoid division by zero
epsilon = 1e-10
ai_counts = [(x - min(ai_counts)) / (max(ai_counts) - min(ai_counts) + epsilon) for x in ai_counts]
github_counts = [(x - min(github_counts)) / (max(github_counts) - min(github_counts) + epsilon) for x in github_counts]

# Create the bar chart
fig, ax = plt.subplots(figsize=(20, 10))  # You might need to adjust the figure size
x = np.arange(len(variables))
width = 0.4

# Plot the AI counts
ax.bar(x - width/2, ai_counts, width, label='AI Node Types', color='blue')

# Plot the GitHub counts
ax.bar(x + width/2, github_counts, width, label='GitHub Node Types', color='orange')

# Set the x-axis and y-axis labels
ax.set_xlabel('Node Types')
ax.set_ylabel('Normalized Count')

# Set the title
ax.set_title('AST Node Types Analysis')

# Set the x-axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(variables, rotation=90, ha='right')  # You might need to adjust the rotation angle

# Add a legend
ax.legend()

# Show the plot
plt.tight_layout()
plt.show()

# Create the parallel plot
fig, axes = plt.subplots(figsize=(20, 10))  # You might need to adjust the figure size

# Set the horizontal shift for GitHub lines
shift = 0.1

# Plot the lines for AI node types
axes.plot(variables, ai_counts, marker='o', color='blue', label='AI Node Types')

# Plot the lines for GitHub node types with a shift
axes.plot(np.arange(len(variables)) + shift, github_counts, marker='o', color='orange', label='GitHub Node Types')

# Set the x-axis and y-axis labels
axes.set_xlabel('Node Types')
axes.set_ylabel('Normalized Count')

# Rotate x-axis labels if needed
plt.xticks(rotation=90, ha='right')  # You might need to adjust the rotation angle

# Set the title
axes.set_title('AST Node Types Analysis')

# Add a legend
axes.legend()

# Show the plot
plt.tight_layout()
plt.show()
