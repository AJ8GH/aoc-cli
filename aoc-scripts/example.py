import re
import sys

output = ''
get_example = False
found = False
regex = '^ {4}(.*\n)$'
example = re.compile(regex)
file = sys.argv[1]

f_in = open(file, "rt")
for line in f_in:
    if 'For example' in line or 'Here is an example' in line:
        get_example = True
    if get_example:
        if example.search(line):
            found = True
            result = re.search(regex, line)
            output += result.group(1)
        else:
            if found:
                get_example = False

print(output)
