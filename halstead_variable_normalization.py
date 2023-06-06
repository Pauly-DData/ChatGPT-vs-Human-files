import pandas as pd
import re

# Read the file into a DataFrame
df = pd.read_excel('output_with_halstead_github.xlsx')

# Function to parse HalsteadReport and create columns for each variable
def parse_halstead(df, column):
    halstead_metrics = ['h1', 'h2', 'N1', 'N2', 'vocabulary', 'length', 'calculated_length', 'volume', 'difficulty', 'effort', 'time', 'bugs']
    for metric in halstead_metrics:
        df[f'{column}_{metric}'] = df[column].apply(lambda x: float(re.search(f'{metric}=(\d*\.?\d+)', x).group(1)) if pd.notnull(x) else None)
    return df

# Parse 'Column b' and 'Column d'
df = parse_halstead(df, 'human_Halstead')
df = parse_halstead(df, 'ai_Halstead')

# Print the transformed DataFrame
print(df.head())

# Export the DataFrame to a new Excel file

