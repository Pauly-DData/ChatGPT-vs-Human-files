import openai
import pandas as pd

# Set up your OpenAI API key
openai.api_key = "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"

# Load your dataset using pandas (assuming it's in Excel format)
data = pd.read_excel('dataset_ready_to_be_formatted.xlsx')

# Function to get properly formatted code from OpenAI
def reformat_code(code):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        messages=[
            {
                "role": "system",
                "content": "You are ChatGPT, a large language model trained by OpenAI. Your task is to reformat the provided Python code to its proper form and intended indentation."
            },
            {
                "role": "user",
                "content": code
            }
        ],
        max_tokens=500,  # Adjust this to your needs
        n=1,
        temperature=0.3,
    )

    # Get response
    reformatted_code = response['choices'][0]['message']['content']

    return reformatted_code

# Create a new column 'formatted_code' and apply the function to each row in the 'code' column
data['formatted_code'] = data['code'].apply(reformat_code)

# Save the dataframe with the new 'formatted_code' column to a new Excel file
data.to_excel("Randon_Version_reformatted_dataset.xlsx", index=False)
