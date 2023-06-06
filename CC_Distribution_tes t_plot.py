import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the new data
df_cc = pd.read_excel('Cyclomatic Complexity__ChatGPT_results.xlsx')

# Define custom colors
colors = ['blue', 'green']


# Create a new figure
plt.figure(figsize=(10, 6))

# Plot the KDE for Github
sns.kdeplot(df_cc['CC_github'], color=colors[1], label='Github', 
            fill=True)

# Plot the KDE for ChatGPT
sns.kdeplot(df_cc['CC_chatgpt'], color=colors[0], label='ChatGPT', 
            fill=True)

# Draw vertical lines representing the mean values of each distribution
plt.axvline(df_cc['CC_github'].mean(), color=colors[1], linestyle='dashed', linewidth=1)
plt.axvline(df_cc['CC_chatgpt'].mean(), color=colors[0], linestyle='dashed', linewidth=1)

plt.legend(title='Legend')
plt.title('Normal Distribution of Cyclomatic Complexity')
plt.xlabel('Cyclomatic Complexity')
plt.ylabel('Density')
plt.show()

