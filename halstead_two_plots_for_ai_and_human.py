import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

# Load the dataset
df = pd.read_excel('full_halstead_all_variables.xlsx')

# Split the dataframe into human and AI sections
human_df = df.filter(regex='^human')
ai_df = df.filter(regex='^ai')

# Add a new 'Type' column to distinguish between AI and Human
human_df['Type'] = 'Human'
ai_df['Type'] = 'AI'

# Concatenate the dataframes
data = pd.concat([human_df, ai_df])

# Normalize the data
data_norm = (data.drop(columns=['Type']) - data.drop(columns=['Type']).min()) / (data.drop(columns=['Type']).max() - data.drop(columns=['Type']).min())

# Add the 'Type' column back into the normalized dataframe
data_norm['Type'] = data['Type']

# Plot the data using parallel coordinates
plt.figure(figsize=(15,10))
parallel_coordinates(data_norm, 'Type', color=['#1f77b4','#ff7f0e'], alpha=0.5)
plt.title("Halstead Metrics Comparison: AI vs Human")
plt.show()
