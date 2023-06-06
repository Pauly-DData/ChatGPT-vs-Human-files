import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Stat': ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'],
    'Chatgpt': [559, 1.382826, 1.102356, 1, 1, 1, 1, 14],
    'Github': [552, 1.420290, 0.935771, 1, 1, 1, 1, 9]
}

# Create DataFrame
df = pd.DataFrame(data)

# Set Stat column as index for better visualization
df.set_index('Stat', inplace=True)

# Plot
df.plot(kind='bar')
plt.title('Comparison of ChatGPT and GitHub')
plt.ylabel('Values')
plt.xticks(rotation=0)
plt.show()
