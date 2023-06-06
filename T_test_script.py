import numpy as np
import scipy.stats as stats

chatgpt_counts = [1119, 429, 2519, 2803, 910, 12471, 5236, 3073, 3960, 6013, 15094, 1786, 864, 787, 350, 523, 157, 150, 78, 16, 16, 54, 93, 142, 213, 53, 83, 39, 9, 21, 297, 72, 76, 73, 66, 69, 362, 74, 26, 26, 2, 46, 54, 48, 8, 5, 7, 1, 129, 2, 3, 3, 2, 41, 21, 5, 5, 15, 7, 27, 23, 24, 3, 10, 6, 6, 2, 4, 2, 4, 2, 2, 2, 1, 1, 1, 2, 2]
github_counts = [567, 120, 929, 1116, 251, 4666, 2121, 1046, 1571, 2337, 5834, 838, 305, 276, 187, 76, 18, 18, 22, 2, 53, 8, 112, 37, 24, 31, 119, 150, 41, 25, 15, 33, 33, 1, 1, 1, 19, 1, 3, 9, 10, 2, 1, 1, 1, 4, 17, 19, 2, 1, 2, 1, 1]

# Bereken gemiddelde en standaarddeviatie
chatgpt_mean = np.mean(chatgpt_counts)
github_mean = np.mean(github_counts)
chatgpt_std = np.std(chatgpt_counts, ddof=1)  # Gebruik Bessel's correctie (ddof=1)
github_std = np.std(github_counts, ddof=1)

# Bereken t-statistiek en p-waarde
t_stat, p_value = stats.ttest_ind_from_stats(chatgpt_mean, chatgpt_std, len(chatgpt_counts), github_mean, github_std, len(github_counts), equal_var=False)

print(f"T-statistiek: {t_stat}")
print(f"P-waarde: {p_value}")
