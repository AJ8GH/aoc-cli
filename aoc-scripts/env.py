import re
import sys

too_high = "That's not the right answer; your answer is too high."
too_low = "That's not the right answer; your answer is too low."
wrong_level = "You don't seem to be solving the right level.  Did you already complete it?"
correct = "Congratulations, that's the correct answer!"

response = sys.argv[1]
action = sys.argv[2]
level_arg = sys.argv[3]
day_arg = sys.argv[4]
year_arg = sys.argv[5]
work_dir = sys.argv[6]
env_file = sys.argv[7]


def process():
    if too_high in response:
        print(too_high)
    elif too_low in response:
        print(too_low)
    elif wrong_level in response:
        print(wrong_level)
    else:
        edit_env()


def edit_env():
    on_next_day = day_arg == '1'
    current_day = 0
    lines = []

    f_in = open(f"{env_file}", "rt")
    for line in f_in:
        if ('AOC_LEVEL=2' in line and level_arg == '1') or (action == 'next' and day_arg == '1'):
            on_next_day = True
        if 'AOC_DAY=' in line:
            current_day = int(re.findall(r'\d+', line)[0])
        lines.append(line)
    f_in.close()
    on_next_year = (action == 'next' and year_arg == '1') or (on_next_day and current_day == 25)

    # print(f'next day: {on_next_day}, next level: {on_next_level}, next year: {on_next_year}')

    f_out = open(f"{work_dir}/envs/.env_temp", "wt")
    for line in lines:
        if 'AOC_LEVEL=' in line:
            handle_level(f_out, line)
        elif 'AOC_DAY=' in line:
            handle_day(f_out, line, current_day, on_next_day)
        elif 'AOC_YEAR=' in line:
            handle_year(f_out, line, on_next_year)
        else:
            f_out.write(line)

    f_out.close()
    if action == 'submit':
        print(correct)


def handle_level(f_out, line):
    if action == 'next' or action == 'submit':
        next_level(f_out, line)
    elif action == 'set' and level_arg != '':
        set_level(f_out)
    else:
        f_out.write(line)


def handle_day(f_out, line, current_day, on_next_day):
    if action == 'next' or action == 'submit':
        next_day(f_out, line, current_day, on_next_day)
    elif action == 'set' and day_arg != '':
        set_day(f_out)
    else:
        f_out.write(line)


def handle_year(f_out, line, on_next_year):
    if action == 'next' or action == 'submit':
        next_year(f_out, line, on_next_year)
    elif action == 'set' and year_arg != '':
        set_year(f_out)
    else:
        f_out.write(line)


def next_level(f_out, line):
    if level_arg == '1':
        switch_level(f_out, line)
    else:
        f_out.write(line)


def switch_level(f_out, line):
    if 'AOC_LEVEL=1' in line:
        f_out.write(line.replace('AOC_LEVEL=1', 'AOC_LEVEL=2'))
    elif 'AOC_LEVEL=2' in line:
        f_out.write(line.replace('AOC_LEVEL=2', 'AOC_LEVEL=1'))


def next_day(f_out, line, current_day, on_next_day):
    if on_next_day:
        new_day = 1 if current_day == 25 else current_day + 1
        f_out.write(line.replace(str(current_day), str(new_day)))
    else:
        f_out.write(line)


def next_year(f_out, line, on_next_year):
    if on_next_year:
        year = int(re.findall(r'\d+', line)[0])
        f_out.write(line.replace(str(year), str(year + 1)))
    else:
        f_out.write(line)


def set_level(f_out):
    f_out.write(f'export AOC_LEVEL={level_arg}\n')


def set_day(f_out):
    f_out.write(f'export AOC_DAY={day_arg}\n')


def set_year(f_out):
    f_out.write(f'export AOC_YEAR={year_arg}\n')


process()
