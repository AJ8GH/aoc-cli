import re
import sys

file = sys.argv[1]

with open(file) as f:
    lines = f.readlines()

input_pattern = re.compile('\\[get your puzzle input\\]')
cal_pattern = re.compile('\\[return to your Advent calendar\\]')

with open(file, 'w') as f:
    do_write = False
    for line in lines:
        if '--- Day' in line:
            do_write = True
        if 'Answer:' in line or 'Shareon' in line:
            do_write = False
        if do_write and not input_pattern.search(line) and not cal_pattern.search(line):
            if 'stars:\\s+\\*\\*' in line:
                line = line.replace('stars:\\s+\\*\\*', 'stars: \U00002B50 \U00002B50')
                f.write(line)
            elif 'star:\\s+\\*' in line:
                line = line.replace('star:\\s+\\*', 'stars: \U00002B50')
                f.write(line)
            else:
                f.write(line)
