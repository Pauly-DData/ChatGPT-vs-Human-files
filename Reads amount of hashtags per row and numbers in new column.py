import pandas as pd
import numpy as np

# read the CSV file into a pandas DataFrame
df = pd.read_csv(r'C:/Users/1948NM/Documents/Technische bedrijfskunde/Jaar 2 - 2017 -2019/Blok 1/Programmeren en visualiseren/outputCODE.csv', delimiter=';', dtype='object')

# create a new column with the count of '#' characters per row
df['num_hashtags'] = df.apply(lambda row: row.str.count('#').sum(), axis=1)



print(df)

df.to_csv('tryingto.csv', index=False)

