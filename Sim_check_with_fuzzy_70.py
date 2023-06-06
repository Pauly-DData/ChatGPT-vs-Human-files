import re
import pandas as pd
from fuzzywuzzy import fuzz

def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove special characters
    text = re.sub(r'[^a-z0-9\s]', '', text)
    
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

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

    # Preprocess the ChatGPT text
    chatgpt_text = preprocess_text(str(row1['chatgpt']))

    # Iterate over each row in the GitHub column
    for j, row2 in df.iterrows():
        # Preprocess the GitHub text
        github_text = preprocess_text(str(row2['github']))

        # Calculate the similarity score between the two values
        score = fuzz.token_set_ratio(chatgpt_text, github_text) / 100

        # Update the best match and similarity score if necessary
        if score > best_score:
            best_match = str(row2['github'])
            best_score = score
            best_match_index = j

    # Add the best match and similarity score to the current row in the matched_df
    matched_df.loc[len(matched_df)] = {'chatgpt': row1['chatgpt'], 'github': best_match, 'score': best_score}

    # Remove the matched GitHub answer to speed up the process for the next iterations
    if best_match_index != -1:
        df.at[best_match_index, 'github'] = ''

# Sort the dataframe by the similarity score in descending order
sorted_df = matched_df.sort_values(by='score', ascending=False)

# Select the most similar rows based on a threshold value
threshold = 0.7  # Lower the threshold value to include more records in the output
matches = sorted_df[sorted_df['score'] >= threshold]

# Output the matches to a CSV file
matches.to_csv('output_importing_into_py_part_1.csv', index=False)

# Output the matches to an Excel file
matches.to_excel('output_importing_into_py_part_1.xlsx', index=False)
