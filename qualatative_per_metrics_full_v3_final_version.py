import pandas as pd

def parse_assessment(text):
    """Parse assessment string into dictionary."""
    metrics = {}
    if pd.isnull(text):  # handle NaN values
        return metrics
    lines = text.split("\n")
    for line in lines:
        parts = line.split(":")
        if len(parts) == 2:
            metric, score = parts
            metrics[metric.strip()] = int(score.strip())
    return metrics

# Read the Excel file
df = pd.read_excel('Assessed_qualtative_test(full).xlsx', engine='openpyxl')

# Parse 'Assessment_github' and 'Assessment_GPT' columns
github_metrics_df = df['Assessment_github'].apply(parse_assessment).apply(pd.Series)
gpt_metrics_df = df['Assessment_GPT'].apply(parse_assessment).apply(pd.Series)

# Rename columns to avoid name clashes
github_metrics_df.columns = [f'github_{col}' for col in github_metrics_df.columns]
gpt_metrics_df.columns = [f'gpt_{col}' for col in gpt_metrics_df.columns]

# Concatenate the original dataframe with the new dataframes
df = pd.concat([df, github_metrics_df, gpt_metrics_df], axis=1)

# Output the dataframe
print(df)

# Saving the updated dataframe to a new Excel file
df.to_excel("qualatative_per_metrics_full_v3.xlsx", index=False)
