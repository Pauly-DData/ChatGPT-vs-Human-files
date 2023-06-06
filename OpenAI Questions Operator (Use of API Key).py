import openai
import pandas as pd

# Set up your OpenAI API key
openai.api_key = "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"

# Load your dataset using pandas (assuming it's in CSV format)
# Load your CSV file using pandas
data = pd.read_csv(r'C:/Users/1948NM/Documents/Technische bedrijfskunde/Jaar 2 - 2017 -2019/Blok 1/Programmeren en visualiseren/3 vragen uit de grote file ivm tokens.csv', delimiter=';')

# Assuming your questions are in a column named 'questions'
questions = data['Questions,Instructions']

# Create a new column for answers
data['Answers'] = ''

# Function to get answer from ChatGPT
def get_answer(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0].text.strip()

# Iterate through the questions and generate answers
for idx, question in enumerate(questions):
    answer = get_answer(question)
    data.loc[idx, 'answers'] = answer

# Save the dataframe with the new answers column to a new CSV file
data.to_csv("your_updated_dataset_file2.csv", index=False)

data.to_excel("your_updated_dataset_file2.xlsx", index=False)
