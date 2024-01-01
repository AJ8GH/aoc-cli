import re
import sys

file = sys.argv[1]
complete = 'Both parts of this puzzle are complete! They provide two gold stars:'
star = '\U00002B50'

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
                line = line.replace('stars:\\s+\\*\\*', f'stars: {star} {star}')
                f.write(line)
            elif complete in line:
                f.write(f'{complete} {star} {star}')
            elif 'star:\\s+\\*' in line:
                line = line.replace('star:\\s+\\*', f'stars: {star}')
                f.write(line)
            else:
                f.write(line)
