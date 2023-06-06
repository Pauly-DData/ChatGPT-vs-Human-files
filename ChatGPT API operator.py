import openai
import pandas as pd

# Set up your OpenAI API key
openai.api_key = ""

# Load your dataset using pandas (assuming it's in CSV format)
data = pd.read_csv(r'C:/Users/1948NM/Documents/Technische bedrijfskunde/Jaar 2 - 2017 -2019/Blok 1/Programmeren en visualiseren/final_file_versie_3.csv', delimiter=';')

# Assuming your questions are in a column named 'questions'
questions = data['Questions,Instructions']

# Create a new column for answers
data['answers'] = ''

# Function to get answer from ChatGPT
def get_answer(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=250,
        n=1,
        temperature=0.7,
    )

    return response['choices'][0]['message']['content'].strip()

# Iterate through the questions and generate answers
for idx, question in enumerate(questions):
    answer = get_answer(question)
    data.loc[idx, 'answers'] = answer

# Save the dataframe with the new answers column to a new CSV file
data.to_csv("your_updated_dataset_file3.2.csv", index=False)

data.to_excel("your_updated_dataset_file3.2.xlsx", index=False)





