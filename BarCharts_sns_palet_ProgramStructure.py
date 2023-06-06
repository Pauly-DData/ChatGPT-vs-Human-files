import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data_chatgpt = {
    'If': 224,
    'For': 159,
    'While': 343. 
    'Try' : ,
    
   
}

data_github = {
    'Import': 181,
    'ImportFrom': 112,
    'alias': 262
   
}

# Convert dictionaries to pandas dataframes
df_chatgpt = pd.DataFrame(list(data_chatgpt.items()), columns=['NodeType', 'Count'])
df_chatgpt['Source'] = 'ChatGPT'

df_github = pd.DataFrame(list(data_github.items()), columns=['NodeType', 'Count'])
df_github['Source'] = 'GitHub'

# Merge the two dataframes
df = pd.concat([df_chatgpt, df_github])

df.sort_values('Count', ascending=False, inplace=True)

plt.figure(figsize=(7,6), tight_layout=True)
colors = sns.color_palette('pastel')

bottom_ai = np.zeros(1)
bottom_human = np.zeros(1)

for node_type, color in zip(df['NodeType'].unique(), colors):
    data_ai = df[(df['NodeType'] == node_type) & (df['Source'] == 'ChatGPT')]['Count']
    data_human = df[(df['NodeType'] == node_type) & (df['Source'] == 'GitHub')]['Count']
    
    plt.bar('ChatGPT', data_ai, bottom=bottom_ai, color=color, label=node_type)
    plt.bar('GitHub', data_human, bottom=bottom_human, color=color)
    
    bottom_ai += data_ai.values
    bottom_human += data_human.values

# Set the title and labels
plt.title('Comparison of Node Types for "Control Flow" Category between ChatGPT (AI) and Human code')
plt.ylabel('Count')
plt.xlabel('Source')

# Add legend outside of plot
plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left')

# Show the plot
plt.show()
