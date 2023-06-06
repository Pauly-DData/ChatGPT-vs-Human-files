import openai
import pandas as pd
import time
import numpy as np
from openai.error import RateLimitError

# Set up your OpenAI API key
openai.api_key = "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"
# Load your dataset using pandas
filename = 'Randon_final_doc.xlsx'
data = pd.read_excel(filename)

# Replace these with the appropriate column names
codegithub = 'github'
codeGPT = 'codeGPT'

# Define function to extract the scores
def extract_scores(response):
    scores = {}
    for message in response['choices'][0]['message']['content'].split("\n"):
        try:
            metric, score = message.split(":")
            scores[metric.strip()] = int(score.strip())
        except ValueError:
            pass
    return '\n'.join(f'{key}: {value}' for key, value in scores.items())

# Define function to assess the code
def assess_code(code):
    code = str(code)
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
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0301",
            messages=[
                {
                    "role": "system",
                    "content": "You are ChatGPT. Your task is to assess the provided Python code based on the criteria and give a score from 1 to 10 for each. Only note the score, no further explanation. The criteria are: " + ', '.join(criteria)
                },
                {
                    "role": "user",
                    "content": f"```python\n{code}\n```"
                }
            ],
            max_tokens=150,
            n=1,
            temperature=0.3,
        )
        return extract_scores(response)
    # In the assess_code function
    except RateLimitError:
        print("Rate limit exceeded, sleeping for 60 seconds.")
        time.sleep(60)
        return assess_code(code)
    
# Assess both github code and GPT code
data['Assessment_github'] = data[codegithub].apply(assess_code)
data['Assessment_GPT'] = data[codeGPT].apply(assess_code)

# Save the result back to excel
data.to_excel("Assessed_qualtative_test(1-60).xlsx", index=False)
