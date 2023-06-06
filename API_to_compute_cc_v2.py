import openai
import pandas as pd

# Set up your OpenAI API key
openai.api_key = " "

# Load your dataset using pandas (assuming it's in Excel format)
data = pd.read_excel('Randon_Version_reformatted_dataset.xlsx')
# Function to get cyclomatic complexity from OpenAI
def get_complexity(code):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        
        messages=[
            {
                "role": "system",
                "content": "You are ChatGPT, a large language model trained by OpenAI. Your task is to compute the cyclomatic complexity for the provided Python code. Only state the final answer (a number)"
            },
            {
                "role": "user",
                "content": code
            }
        ],
        max_tokens=200,  # Adjust this to your needs
        n=1,
        temperature=0.7,
    )

    # Get response and try to extract just the number, assuming the response is in the format "The cyclomatic complexity of the given code is X."
    try:
        complexity = int(response['choices'][0]['message']['content'].split()[-1])
    except ValueError:
        complexity = "Error computing complexity"

    return complexity

# Create a new column 'complexity' and apply the function to each row in the 'code' column
data['complexity'] = data['code'].apply(get_complexity)

# Save the dataframe with the new complexity column to a new Excel file
data.to_excel("Randon_Version_updated_dataset.xlsx", index=False)
