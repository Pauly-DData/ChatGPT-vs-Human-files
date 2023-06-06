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

# Fill NaN values with zeros
    df_nodes.fillna(0, inplace=True)

# Apply the function to each row in your column
df['parsed_nodes'] = df['github_result'].apply(parse_nodes)

# Split parsed_nodes column into separate columns
df_nodes = df['parsed_nodes'].apply(pd.Series)

pd.set_option('display.max_columns', None)  # None means unlimited
pd.set_option('display.max_rows', None)     # None means unlimited

print(df_nodes.describe())

with open("descriptive_stats.xlsx", "w") as f:
    f.write(df_nodes.describe().to_string())
    
df_nodes.describe().to_excel("descriptive_stats_ast_github.xlsx")  

# Now df_nodes contains a column for each node type with its respective counts
df_nodes.to_excel("parsed_nodes.xlsx", index=False)

# Assuming df is your DataFrame
features = df.columns

plt.figure(figsize=(10, 8))
sns.boxplot(data=df_nodes)
plt.title('Boxplot of Features')
plt.xticks(rotation=90)
plt.show()

df_nodes.hist(bins=30, figsize=(15,10), layout=(2,4))
