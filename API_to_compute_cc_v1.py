import openai
import pandas as pd

# Set up your OpenAI API key
openai.api_key = ""

# Load your dataset using pandas (assuming it's in Excel format)
data = pd.read_excel('Randon_test_script_v2_output.xlsx')

# Assuming your code samples are in a column named 'code'
code_samples = data['code']

# Create a new column for complexity results
data['complexity'] = ''

# Function to get cyclomatic complexity from OpenAI
def get_complexity(code):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are ChatGPT, a large language model trained by OpenAI. Your task is to compute the cyclomatic complexity for the provided Python code."
            },
            {
                "role": "user",
                "content": code
            }
        ],
        max_tokens=60,  # Adjust this to your needs
        n=1,
        temperature=0.7,
    )

    # Get response and try to extract just the number, assuming the response is in the format "The cyclomatic complexity of the given code is X."
    try:
        complexity = int(response['choices'][0]['message']['content'].split()[-1])
    except ValueError:
        complexity = "Error computing complexity"

    return complexity

# Iterate through the code samples and compute complexity
for idx, code in enumerate(code_samples):
    complexity = get_complexity(code)
    data.loc[idx, 'complexity'] = complexity

# Save the dataframe with the new complexity column to a new Excel file
data.to_excel("Randon_Version_updated_dataset.xlsx", index=False)

