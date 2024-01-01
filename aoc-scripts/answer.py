import re
import sys

level_1_answers = []
level_2_answers = []
written = False
writing_1 = False
writing_2 = False
regex = '`_(.*)_`'
pattern = re.compile(regex)
readme_file = sys.argv[1]
test_file = sys.argv[2]
level = int(sys.argv[3])
PART_2_HEADER = '--- Part Two ---'
LINE = 'getInput(0, 0)'
PART_1 = 'inputProviderPart1'
PART_2 = 'inputProviderPart2'

f_in = open(readme_file, "rt")
current_answers = level_1_answers
for line in f_in:
    if pattern.search(line):
        result = re.search(regex, line)
        current_answers.append(result.group(1))
    if PART_2_HEADER in line:
        current_answers = level_2_answers

level_1_found = len(level_1_answers) >= 1
level_2_found = len(level_2_answers) >= 1

answer1 = None
answer2 = None

if level_1_found:
    answer1 = level_1_answers[len(level_1_answers) - 1]
if level_2_found:
    answer2 = level_2_answers[len(level_2_answers) - 1]

f_in = open(test_file, "rt")
f_out = open(f'{test_file}1', "wt")

for line in f_in:
    if PART_1 in line:
        writing_1 = True
    if PART_2 in line:
        writing_2 = True
        writing_1 = False
    if written or LINE not in line:
        f_out.write(line)
    else:
        if writing_1 and level_1_found:
            f_out.write(line.replace(LINE, f'getInput({answer1}, 0)'))
        elif writing_2 and level_2_found:
            f_out.write(line.replace(LINE, f'getInput({answer2}, 0)'))
        else:
            f_out.write(LINE)
        written = True
