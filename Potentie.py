import pandas as pd

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(r'C:/Users/1948NM/Documents/Technische bedrijfskunde/Jaar 2 - 2017 -2019/Blok 1/Programmeren en visualiseren/outputCODE.csv', sep='\t')


# Initialize variables to store the questions and answers
questions = []
answers = []

# Initialize a variable to keep track of the current state (question or answer)
state = None

# Iterate over the rows of the DataFrame
for index, row in df.iterrows():
    # Check if the row starts with two #
    if row['code'].startswith('#'):
        # If the row starts with two #, assume it marks the start of a new question-answer pair
        # Save the current question and start a new answer
        questions.append(row['code'])
        answers.append('')
        state = 'answer'
    elif state == 'answer':
        # If the current state is 'answer', assume the row belongs to the current answer
        # Add the row to the current answer
        answers[-1] += row['code'] + '\n'
    elif state is None:
        # If the current state is None, assume the row is not part of a question-answer pair
        pass
    else:
        # If the current state is 'question', assume the row marks the end of the current question-answer pair
        state = None

# Combine the questions and answers into a DataFrame
df_qa = pd.DataFrame({'Question': questions, 'Answer': answers})

# Write the questions and answers to a file
df_qa.to_csv('file_qa.csv', index=False)

print(df_qa)
