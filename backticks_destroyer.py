import pandas as pd
import re
import csv 

# Function to detect the delimiter in a CSV file
def detect_delimiter(file_path):
    with open(file_path, 'r') as file:
        dialect = csv.Sniffer().sniff(file.readline())
    return dialect.delimiter

# Read the CSV file into a DataFrame
df = pd.read_csv('C:/Users/1948NM/Documents/Technische bedrijfskunde/Jaar 2 - 2017 -2019/Blok 1/Programmeren en visualiseren/Simm_cleaning_in_python.csv', delimiter=';')

def clean_content(content):
    if not isinstance(content, str):
        return ''
    regex_pattern = r'```([\s\S]*?)     '
    data = re.findall(regex_pattern, content)
    return '\n'.join(item.strip() for item in data)

# Apply the cleaning function to the 'chatgpt' column
df['chatgpt_cleaned'] = df['chatgpt'].apply(clean_content)


# Save the cleaned DataFrame as a new CSV file
df.to_csv('cleaned_data_no_backtickts.csv', index=False)

# Output the matches to an Excel file
df.to_excel('cleaned_data_no_backtickts.csv.xlsx', index=False)
