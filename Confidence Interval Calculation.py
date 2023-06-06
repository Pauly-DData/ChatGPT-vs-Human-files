# Your data
data = {
    "group": ["github", "gpt"],
    "mean": [6.13, 6.41],
    "sem": [0.07, 0.05]
}

# Calculate the confidence intervals
for i in range(2):
    ci_lower = data["mean"][i] - 1.96 * data["sem"][i]
    ci_upper = data["mean"][i] + 1.96 * data["sem"][i]
    print(f"The 95% confidence interval for {data['group'][i]} is ({ci_lower:.2f}, {ci_upper:.2f})")
