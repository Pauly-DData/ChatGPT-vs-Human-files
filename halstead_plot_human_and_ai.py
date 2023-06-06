import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

# Load the dataset
df = pd.read_excel('output_with_halstead_github.xlsx')

def parse_halstead(halstead_str):
    # Ensure halstead_str is a string
    if pd.isna(halstead_str) or not isinstance(halstead_str, str):
        return None
    halstead_str = halstead_str[halstead_str.find("(")+1:halstead_str.find(")")]
    return dict(item.split("=") for item in halstead_str.split(", "))

# Parse the AI and human Halstead metrics
halstead_AI = df['ai_Halstead'].apply(parse_halstead)
halstead_Human = df['human_Halstead'].apply(parse_halstead)

# Filter out None values and convert dictionaries to dataframes
halstead_AI = pd.DataFrame([x for x in halstead_AI if x is not None])
halstead_Human = pd.DataFrame([x for x in halstead_Human if x is not None])

# Add a new 'Type' column to distinguish between AI and Human
halstead_AI['Type'] = 'AI'
halstead_Human['Type'] = 'Human'

# Concatenate the dataframes
data = pd.concat([halstead_AI, halstead_Human])

# Plot the data using parallel coordinates
plt.figure(figsize=(15,10))
parallel_coordinates(data, 'Type', color=['#1f77b4','#ff7f0e'], alpha=0.5)
plt.title("Halstead Metrics Comparison: AI vs Human")
plt.show()