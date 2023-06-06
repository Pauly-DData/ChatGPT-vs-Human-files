import pandas as pd
from scipy import stats

# Load the data from your Excel file
df = pd.read_excel('full_halstead_all_variables.xlsx')

# Calculate descriptive statistics
desc_stats = df.describe()

# Print the descriptive statistics
pd.set_option('display.max_columns', None)  # or number of columns


print(desc_stats)

# Identify all metrics by removing 'human_' and 'ai_' prefixes
metrics = set(col.replace('human_', '').replace('ai_', '') for col in df.columns)

# For each metric, perform a t-test on the human and AI columns
for metric in metrics:
    human_col = 'human_' + metric
    ai_col = 'ai_' + metric

    # Perform the t-test
    t_stat, p_val = stats.ttest_ind(df[human_col], df[ai_col])

    # Print the result
    print(f'For {metric}, t-statistic: {t_stat}, p-value: {p_val}')
