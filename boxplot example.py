import matplotlib.pyplot as plt

# Sample data for human-generated and AI-generated code
human_data = [10, 15, 12, 18, 20]  # Replace with your actual data
ai_data = [8, 13, 11, 16, 19]  # Replace with your actual data

# Create a list of data to be plotted
data = [human_data, ai_data]

# Create a figure and axis
fig, ax = plt.subplots()

# Create the box plot
bp = ax.boxplot(data)

# Customize the plot
ax.set_xticklabels(['Human', 'AI'])  # Set x-axis labels
ax.set_ylabel('Cyclomatic Complexity')  # Set y-axis label
ax.set_title('Comparison of Cyclomatic Complexity')  # Set plot title

# Show the plot
plt.show()
