import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the data
df = pd.read_excel('full_halstead_all_variables.xlsx')  # Replace 'your_data.xlsx' with your actual file name

# Normalize the data (excluding non-numeric columns if any exist)
df = (df - df.min()) / (df.max() - df.min())

# Get the variable names (column names)
variables = df.columns

# Define two groups for comparison
group1_counts = df.loc[:, variables.str.contains("human")].mean().values
group2_counts = df.loc[:, variables.str.contains("ai")].mean().values

# Set figure size
plt.figure(figsize=(20,10))

# Define width of a bar 
width = 0.3       

# Set position of bar on X axis
bar1 = np.arange(len(group1_counts))
bar2 = [x + width for x in bar1]

# Make the plot
plt.bar(bar1, group1_counts, color ='b', width = width, label ='Human')
plt.bar(bar2, group2_counts, color ='r', width = width, label ='AI')

# Add xticks on the middle of the group bars
plt.xlabel('Halstead Metrics', fontweight ='bold')
plt.ylabel('Normalized Mean Values', fontweight ='bold')
plt.xticks([r + width / 2 for r in range(len(group1_counts))], [var.split("_")[2] for var in variables[::2]], rotation = 45)
plt.title('Halstead Metrics: Human vs AI')

# Create legend & Show graphic
plt.legend()
plt.show()


# Parallel plot
plt.figure(figsize=(20,10))
plt.plot(variables[::2], group1_counts, marker='o', color='blue', label='Human Halstead Metrics')
plt.plot(variables[::2], group2_counts, marker='o', color='red', label='AI Halstead Metrics')
plt.xlabel('Halstead Metrics', fontweight ='bold')
plt.ylabel('Normalized Mean Values', fontweight ='bold')
plt.title('Halstead Metrics: Human vs AI')
plt.xticks(ticks=np.arange(len(variables[::2])), labels=[var.split("_")[2] for var in variables[::2]], rotation=45)
plt.legend()
plt.show()
