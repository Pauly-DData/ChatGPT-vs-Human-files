import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import numpy as np

# Load the data
df = pd.read_excel('nested_depth_outcomes_of_an_and_humab.xlsx')

# Set the style and context of the plots
sns.set(style='whitegrid')

# Define custom colors
colors = ['blue', 'green']

# Create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Plot the histogram for Github
axs[1].hist(df['Nested Depth Github'], bins=range(1, 15), alpha=0.7, color=colors[1])
axs[1].set_xlabel('Nested Depth')
axs[1].set_ylabel('Frequency')
axs[1].set_title('Github')

# Plot the histogram for ChatGPT
axs[0].hist(df['Nested Depth ChatGPT'], bins=range(1, 15), alpha=0.7, color=colors[0])
axs[0].set_xlabel('Nested Depth')
axs[0].set_ylabel('Frequency')
axs[0].set_title('ChatGPT')


# Adjust spacing between subplots
plt.tight_layout()

# Show the plot
plt.show()

# Create a box plot
plt.figure(figsize=(10, 6))

data_to_plot = [df['Nested Depth Github'], df['Nested Depth ChatGPT']]
labels = ['Github', 'ChatGPT']

plt.boxplot(data_to_plot, labels=labels)
plt.ylabel('Nested Depth')
plt.title('Box Plot of Nested Depth')

plt.show()

# Perform t-test
t_statistic, p_value = stats.ttest_ind(df['Nested Depth Github'], df['Nested Depth ChatGPT'])

print("T-statistic:", t_statistic)
print("p-value:", p_value)



# Calculate Cohen's d
mean_diff = np.mean(df['Nested Depth Github']) - np.mean(df['Nested Depth ChatGPT'])
pooled_std = np.sqrt(((len(df['Nested Depth Github']) - 1) * np.var(df['Nested Depth Github']) + (len(df['Nested Depth ChatGPT']) - 1) * np.var(df['Nested Depth ChatGPT'])) / (len(df['Nested Depth Github']) + len(df['Nested Depth ChatGPT']) - 2))

cohen_d = mean_diff / pooled_std

print("Cohen's d:", cohen_d)


# Add import for scipy.stats.norm
from scipy.stats import norm

# Create a new figure
plt.figure(figsize=(10, 6))

# Plot the KDE for Github
sns.kdeplot(df['Nested Depth Github'], color=colors[1], label='Github', 
            fill=True)

# Plot the KDE for ChatGPT
sns.kdeplot(df['Nested Depth ChatGPT'], color=colors[0], label='ChatGPT', 
            fill=True)

# Draw vertical lines representing the mean values of each distribution
plt.axvline(df['Nested Depth Github'].mean(), color=colors[1], linestyle='dashed', linewidth=1)
plt.axvline(df['Nested Depth ChatGPT'].mean(), color=colors[0], linestyle='dashed', linewidth=1)

plt.legend(title='Legend')
plt.title('Normal Distribution of Nested Depth')
plt.xlabel('Nested Depth')
plt.ylabel('Density')
plt.show()
