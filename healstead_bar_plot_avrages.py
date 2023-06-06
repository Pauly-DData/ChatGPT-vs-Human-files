import matplotlib.pyplot as plt
import numpy as np

# Column headers
columns = ['h1', 'h2', 'N1', 'N2', 'vocabulary', 'length', 'calculated_length', 'volume', 'difficulty', 'effort', 'time', 'bugs']

# Provided data
human_means = [0.617760618, 1.486486486, 0.951737452, 1.787644788, 2.104247104, 2.739382239, 4.272904687, 8.063255644, 0.383827826, 17.44644853, 0.969247141, 0.002687752]
ai_means = [0.613899614, 1.355212355, 0.828185328, 1.583011583, 1.969111969, 2.411196911, 3.699644071, 6.837547347, 0.368686681, 12.47079267, 0.692821815, 0.002279182]

x = np.arange(len(columns))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize=(12,6))
rects1 = ax.bar(x - width/2, human_means, width, label='Human', color='#1f77b4')
rects2 = ax.bar(x + width/2, ai_means, width, label='AI', color='#ff7f0e')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Mean Values')
ax.set_title('Mean Halstead Metrics: AI vs Human')
ax.set_xticks(x)
ax.set_xticklabels(columns)
ax.legend()

# To make it easier to see the values, we can add labels on top of the bars
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

fig.tight_layout()
plt.show()
