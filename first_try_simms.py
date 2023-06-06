import pandas as pd
import Levenshtein

# Load the Excel file into a Pandas dataframe
df = pd.read_excel('C:/Users/1948NM/Documents/Technische bedrijfskunde/Jaar 2 - 2017 -2019/Blok 1/Programmeren en visualiseren/test_for_simmularities.xlsx')

# Iterate over each row in the chatgpt column
for i, row1 in df.iterrows():
    # Initialize the best match and similarity score for this row
    best_match = None
    best_score = 0
    # Iterate over each row in the github column
    for j, row2 in df.iterrows():
        # Skip the current row in the chatgpt column
        if i == j:
            continue
        # Calculate the similarity score between the two values
        score = Levenshtein.distance(str(row1['chatgpt']), str(row2['github'])) / max(len(str(row1['chatgpt'])), len(str(row2['github'])))
        # Update the best match and similarity score if necessary
        if score > best_score:
            best_match = str(row2['github'])
            best_score = score
    # Add the best match and similarity score to the current row in the chatgpt column
    df.at[i, 'score'] = best_score
    df.at[i, 'match'] = best_match

# Sort the dataframe by the similarity score in descending order
sorted_df = df.sort_values(by='score', ascending=False)

# Select the most similar rows based on a threshold value
threshold = 0.8
matches = sorted_df[sorted_df['score'] >= threshold]

# Output the matches to a CSV file
matches.to_csv('output.csv', index=False)

# Output the matches to an Excel file
matches.to_excel('output.xlsx', index=False)

