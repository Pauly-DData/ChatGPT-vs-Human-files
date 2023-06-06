import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import numpy as np

# Load the data
df = pd.read_excel('T-test_cc_AI_and_Github.xlsx')

# Set the style and context of the plots
sns.set(style='whitegrid')

# Define custom colors
colors = ['blue', 'green']

# Create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Plot the histogram for ChatGPT
axs[0].hist(df['CC_chatgpt'], bins=range(1, 15), alpha=0.7, color=colors[0])
axs[0].set_xlabel('Cyclomatic Complexity')
axs[0].set_ylabel('Frequency')
axs[0].set_title('ChatGPT')

# Plot the histogram for Github
axs[1].hist(df['CC_github'], bins=range(1, 10), alpha=0.7, color=colors[1])
axs[1].set_xlabel('Cyclomatic Complexity')
axs[1].set_ylabel('Frequency')
axs[1].set_title('Github')

# Adjust spacing between subplots
plt.tight_layout()

# Show the plot
plt.show()

# Create a box plot
plt.figure(figsize=(10, 6))

data_to_plot = [df['CC_chatgpt'], df['CC_github']]
labels = ['ChatGPT', 'Github']

plt.boxplot(data_to_plot, labels=labels)
plt.ylabel('Cyclomatic Complexity')
plt.title('Box Plot of Cyclomatic Complexity')

plt.show()

# Perform t-test
t_statistic, p_value = stats.ttest_ind(df['CC_chatgpt'], df['CC_github'])

print("T-statistic:", t_statistic)
print("p-value:", p_value)



# Calculate Cohen's d
mean_diff = np.mean(df['CC_chatgpt']) - np.mean(df['CC_github'])
pooled_std = np.sqrt(((len(df['CC_chatgpt']) - 1) * np.var(df['CC_chatgpt']) + (len(df['CC_github']) - 1) * np.var(df['CC_github'])) / (len(df['CC_chatgpt']) + len(df['CC_github']) - 2))

cohen_d = mean_diff / pooled_std

print("Cohen's d:", cohen_d)
