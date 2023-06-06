import pandas as pd

# read the CSV file into a pandas DataFrame
df = pd.read_csv(r'C:/Users/1948NM/Documents/Technische bedrijfskunde/Jaar 2 - 2017 -2019/Blok 1/Programmeren en visualiseren/outputCODE.csv', delimiter=';', dtype='object')

# create a new column with the count of '#' characters per row
df['num_hashtags'] = df.apply(lambda row: row.str.count('#').sum(), axis=1)

# Create a new column that shifts the 'num_hashtags' column up by one row
df['prev_hashtags'] = df['num_hashtags'].shift()

print(df)

# Create a new column that identifies rows where the current and previous rows both have the value 1
df['consecutive_ones'] = (df['num_hashtags'] == 1) & (df['prev_hashtags'] == 1)

# print the new DataFrame with the count of '#' characters per row
print(df)

df.to_csv('begin.csv', index=False)
