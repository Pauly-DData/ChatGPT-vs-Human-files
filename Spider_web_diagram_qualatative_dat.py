import matplotlib.pyplot as plt
import numpy as np

# Your data
labels=np.array(['Code Readability', 'PEP 8 Conformance', 'Comments and Documentation', 'Error Handling', 'Edge Cases', 'Code Efficiency (Memory Usage)', 'Generalizability', 'Modular Design and Abstraction', 'Clear Writing and Concise Code', 'Use of Libraries and Frameworks', 'Problem-solving Approach', 'Creativity - Novelty and Usefulness', 'Variance in Solutions'])
github_stats=np.array([3232,3555,2180,1902,1949,3320,2785,2781,3305,3219,3260,2010,1504])
gpt_stats=np.array([3165,3538,2356,2150,2229,3267,2793,2801,3269,3365,3231,2088,1775])

# Calculate angles
angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()

# Make the plot circular
github_stats=np.concatenate((github_stats,[github_stats[0]]))
gpt_stats=np.concatenate((gpt_stats,[gpt_stats[0]]))
angles+=angles[:1]

# Create the figure
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
plt.xticks(angles[:-1], labels)

# Plot Github data
ax.plot(angles, github_stats, color='red', linewidth=1, label='Github')
ax.fill(angles, github_stats, color='red', alpha=0.25)

# Plot GPT data
ax.plot(angles, gpt_stats, color='blue', linewidth=1, label='GPT')
ax.fill(angles, gpt_stats, color='blue', alpha=0.25)

# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

plt.show()
