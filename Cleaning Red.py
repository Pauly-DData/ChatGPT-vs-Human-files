import re 
import pandas as pd 

df = pd.read_csv(r'C:\Users\1948NM\Documents\Technische bedrijfskunde\Jaar 2 - 2017 -2019\Blok 1\Programmeren en visualiseren\VolgordeFinal.csv', delimiter=';')

print(df.columns)
print(df['text'][0])

df_1 = df['text'].str.startswith(('50xp', '100xp', '100XP', '50XP', '0XP', '0xp')).to_frame()
print(type(df))

questions = []
# loop through DataFrame using iterrows()
for index, row in df[df_1].iterrows():
    if True:
        #print(row['Questions'])
        questions.append(row)
        #df.drop(row, axis=0)
        #df
# convert lists to DataFrames
questions = pd.DataFrame(questions).dropna()
questions

pd.set_option('display.max_rows', None)

print(questions)

questions.reset_index()

df_1 = ~(df['text'].fillna('').str.startswith(('50xp', '100xp', '100XP', '50XP', '0XP', '0xp')).astype(bool)).to_frame()

instructions = []
for index, row in df[df_1].iterrows():
    if True:
        #print(row['text'])
        instructions.append(row['text'])
instructions

instructions = pd.DataFrame(instructions).dropna()

print(instructions)

instructions.to_csv('instructionsBeterwerktdit.csv', index=False)
