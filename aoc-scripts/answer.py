import re
import sys

answers = []
written = False
writing_1 = False
writing_2 = False
regex = '`_(.*)_`'
pattern = re.compile(regex)
readme_file = sys.argv[1]
test_file = sys.argv[2]
level = int(sys.argv[3])
LINE = '    return getInput(0, 0);\n'
PART_1 = 'inputProviderPart1'
PART_2 = 'inputProviderPart2'

f_in = open(readme_file, "rt")
for line in f_in:
    if pattern.search(line):
        result = re.search(regex, line)
        answers.append(result.group(1))

if len(answers) < level:
    raise Exception("Example answer not found")

answer = answers[level - 1]

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
        if level == 1 and writing_1 or level == 2 and writing_2:
            f_out.write(line.replace(LINE, f'    return getInput({answer}, 0);\n'))
        else:
            f_out.write(LINE)
        written = True
