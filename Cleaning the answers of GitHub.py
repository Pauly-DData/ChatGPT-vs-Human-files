import re
import openpyxl

input_file = 'C:/Users/1948NM/Documents/Technische bedrijfskunde/Jaar 2 - 2017 -2019/Blok 1/Programmeren en visualiseren/AntwoordenVanuitGitHub_deep_learning_in_Pyhton.csv'
output_file = 'grouped_answers_cdeep_learning_in_python.csv'

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.readlines()

def write_excel(file_name, data):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(['Answer Number', 'Answer'])

    for answer_number, answer in data:
        ws.append([answer_number, answer])

    wb.save(file_name)

def replace_multiple_quotes(text):
    quote_pattern = r'"{2,}'
    return re.sub(quote_pattern, '"', text)

def group_answers(data):
    pattern = r'^#.*'
    unwanted_pattern = r'^#-+[\w\s]*-+#$|^#\*+[\w\s]*\*+#$'  # Unwanted patterns
    answers = []
    answer = []

    for index, line in enumerate(data):
        line = line.lstrip()  # Remove leading whitespaces before the first word
        line = replace_multiple_quotes(line)  # Replace two or more quotes with one quote

        if re.match(unwanted_pattern, line):  # Skip the line if it matches any of the unwanted patterns
            continue
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
    write_excel(output_file, grouped_answers)

if __name__ == '__main__':
    main()

