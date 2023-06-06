import pandas as pd

# read the csv file into a pandas dataframe
df = pd.read_csv('outputFINALAnsw.csv')

# drop rows with all blank values
df.dropna(how='all', inplace=True)

# write the updated dataframe to a new csv file
df.to_csv('outputFINAL3_no_blanks.csv', index=False)
