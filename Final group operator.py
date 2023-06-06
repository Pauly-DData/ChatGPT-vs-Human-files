import re
import csv

input_file = 'C:/Users/1948NM/Documents/Technische bedrijfskunde/Jaar 2 - 2017 -2019/Blok 1/Programmeren en visualiseren/grouped_answers.txt'
output_file = 'grouped_answers3.csv'

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.readlines()

def write_csv(file_name, data):
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Answer Number', 'Answer'])
        for answer_number, answer in data:
            writer.writerow([answer_number, f'\n{answer}'])

def group_answers(data):
    pattern = r'^#.*'
    answers = []
    answer = []

    for index, line in enumerate(data):
        if re.match(pattern, line):
            if index > 0 and re.match(pattern, data[index - 1]):
                if answer:
                    answers.append(''.join(answer))
                answer = []
        else:
            answer.append(line)

    if answer:
        answers.append(''.join(answer))

    return [(f"Answer {i+1}", ans) for i, ans in enumerate(answers)]

def main():
    data = read_file(input_file)
    grouped_answers = group_answers(data)
    write_csv(output_file, grouped_answers)

if __name__ == '__main__':
    main()
