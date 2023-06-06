import matplotlib.pyplot as plt
import numpy as np

# Define the variables and their counts
variables = ['Return']
ai_counts = [67]
github_counts = [67]

# Create the parallel plot
fig, axes = plt.subplots(figsize=(10, 6))

# Set the horizontal shift for GitHub lines
shift = 0.1

# Plot the lines for AI node types
axes.plot(variables, ai_counts, marker='o', color='blue', label='AI Node Types')

# Plot the lines for GitHub node types with a shift
axes.plot(np.arange(len(variables)) + shift, github_counts, marker='o', color='orange', label='GitHub Node Types')

# Set the x-axis and y-axis labels
axes.set_xlabel('Node Types')
axes.set_ylabel('Count')

# Rotate x-axis labels if needed
plt.xticks(rotation=45, ha='right')

# Set the title
axes.set_title('ChatGPT vs Human - Return Statements')

# Add a legend
axes.legend()

# Show the plot
plt.tight_layout()
plt.show()
