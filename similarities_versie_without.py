import pandas as pd
import Levenshtein

# Load the Excel file into a Pandas dataframe
df = pd.read_excel('C:/Users/1948NM/Documents/Technische bedrijfskunde/Jaar 2 - 2017 -2019/Blok 1/Programmeren en visualiseren/Simm_cleaning_in_python.xlsx')

# Create a new DataFrame to store the matched answers
matched_df = pd.DataFrame(columns=['chatgpt', 'github', 'score'])

# Iterate over each row in the ChatGPT column
for i, row1 in df.iterrows():
    # Initialize the best match and similarity score for this row
    best_match = None
    best_score = 0
    best_match_index = -1

    # Iterate over each row in the GitHub column
    for j, row2 in df.iterrows():
        # Calculate the similarity score between the two values
        score = 1 - Levenshtein.distance(str(row1['chatgpt']), str(row2['github'])) / max(len(str(row1['chatgpt'])), len(str(row2['github'])))
        # Update the best match and similarity score if necessary
        if score > best_score:
            best_match = str(row2['github'])
            best_score = score
            best_match_index = j

    # Add the best match and similarity score to the current row in the matched_df
    matched_df = matched_df.append({'chatgpt': row1['chatgpt'], 'github': best_match if best_match is not None else '', 'score': best_score}, ignore_index=True)

    # Remove the matched GitHub answer to speed up the process for the next iterations
    if best_match_index != -1:
        df.at[best_match_index, 'github'] = ''

# Sort the dataframe by the similarity score in descending order
sorted_df = matched_df.sort_values(by='score', ascending=False)

# Output the matches to a CSV file
sorted_df.to_csv('output_simm_cleaning_in_python.csv', index=False)

# Output the matches to an Excel file
sorted_df.to_excel('output_simm_cleaning_in_python.xlsx', index=False)  
