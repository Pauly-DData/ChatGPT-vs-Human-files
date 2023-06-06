import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import parallel_coordinates

# Load the dataset
df = pd.read_excel('full_halstead_all_variables.xlsx')

# List of common metrics
metrics = ['h1', 'h2', 'N1', 'N2', 'vocabulary', 'length', 'calculated_length', 'volume', 'difficulty', 'effort', 'time', 'bugs']

# Create a dictionary to rename AI columns
ai_columns = {'ai_Halstead_'+metric: metric for metric in metrics}
# Create a dictionary to rename human columns
human_columns = {'human_Halstead_'+metric: metric for metric in metrics}

# Split the dataframe into human and AI sections
human_df = df.filter(regex='^human_Halstead').rename(columns=human_columns)
ai_df = df.filter(regex='^ai_Halstead').rename(columns=ai_columns)

# Add a new 'Type' column to distinguish between AI and Human
human_df['Type'] = 'Human'
ai_df['Type'] = 'AI'

# Concatenate the dataframes
data = pd.concat([human_df, ai_df])

# Normalize the data
data_norm = (data.drop(columns=['Type']) - data.drop(columns=['Type']).min()) / (data.drop(columns=['Type']).max() - data.drop(columns=['Type']).min())

# Add the 'Type' column back into the normalized dataframe
data_norm['Type'] = data['Type']

# Calculate the mean values
mean_values = data_norm.groupby('Type').mean()

# Set a better color palette
colors = sns.color_palette("Set3", len(metrics))

# Plot the data using parallel coordinates
plt.figure(figsize=(15, 10))
parallel_coordinates(data_norm, 'Type', colormap='Greys', alpha=0.20)

# Plot the mean lines with better visibility
plt.plot(mean_values.columns, mean_values.loc['AI'], color='red', linewidth=3.0, label='Mean (AI)')
plt.plot(mean_values.columns, mean_values.loc['Human'], color='green', linewidth=3.0, label='Mean (Human)')

plt.title("Halstead Metrics Comparison: AI vs Human")
plt.legend()
plt.show()
