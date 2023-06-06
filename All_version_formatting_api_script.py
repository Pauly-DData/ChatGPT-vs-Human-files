import openai
import pandas as pd
import time
import requests.exceptions


# Set up your OpenAI API key
openai.api_key = "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"

# Load your dataset using pandas (assuming it's in Excel format)
data = pd.read_excel('dataset_ready_to_be_formatted.xlsx')

# Function to get properly formatted code from OpenAI
def assess_code(code):
    criteria = [
        "Code Readability",
        "PEP 8 Conformance",
        "Comments and Documentation",
        "Error Handling",
        "Edge Cases",
        "Code Efficiency (Memory Usage)",
        "Generalizability",
        "Modular Design and Abstraction",
        "Clear Writing and Concise Code",
        "Use of Libraries and Frameworks",
        "Problem-solving Approach",
        "Creativity - Novelty and Usefulness",
        "Variance in Solutions",
    ]

    prompt = "Rate the following code based on these criteria on a scale from 1 to 10:\n\n"
    for criterion in criteria:
        prompt += criterion + ": \n"
    prompt += code

    base_delay = 0.01  # Set initial delay to 10ms
    max_delay = 60.0   # Set max delay to 60s
    delay = base_delay
    while True:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0301",
                messages=[
                    {
                        "role": "system",
                        "content": "You are ChatGPT, a large language model trained by OpenAI. Your task is to assess the provided Python code based on specific criteria and give a score from 1 to 10 for each."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                max_tokens=500,  # Adjust this to your needs
                n=1,
                temperature=0.3,
            )

            # If successful, break the loop
            break
        except RateLimitError:
            # If rate limit error, sleep for delay seconds and then double the delay
            time.sleep(delay)
            delay = min(delay * 2, max_delay)

    # Get response
    assessment = response['choices'][0]['message']['content']

    return assessment

# Apply the function to each row in the 'codeGPT' and 'codeGithub' columns separately and store the results in the corresponding assessment columns
data['Assessment_GPT'] = data['codeGPT'].apply(assess_code)
data['Assessment_Github'] = data['codeGithub'].apply(assess_code)

# Save the dataframe with the new 'Assessment_GPT' and 'Assessment_Github' columns to a new Excel file
data.to_excel("Randon_Version_assessed_dataset.xlsx", index=False)

