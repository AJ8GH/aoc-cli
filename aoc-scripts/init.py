import os

work_dir = os.path.dirname(os.path.realpath(__file__))

module = ''
source = ''
resource = ''
src_year_prefix = ''
res_year_prefix = ''
day_prefix = 'd'
inner_source = ''
inner_resource = ''

session = input('Session Token:\n')
project = input('Project Name (advent-of-code):\n')
input_file = input('Input File Name (input.txt):\n')
example_file = input('Example File Name (example.txt):\n')
env = input('Env File Name (aoc):\n')
ide = input('Editor Launcher (code):\n')
if input('Customise Directory Structure? (y/n):') == 'y':
    module = input('Module Prefix, leave blank to omit:\n')
    source = input('Source Directory, leave blank to omit:\n')
    resource = input('Resources Directory, leave blank to omit:\n')
    src_year_prefix = input('Source Year Package Prefix, leave blank to omit:\n')
    res_year_prefix = input('Resource Year Directory Prefix, leave blank to omit:\n')
    day_prefix = input('Day Directory prefix, (day-):\n')
    inner_source = input('Source Subdirectory, leave blank to omit:\n')
    inner_resource = input('Resources Subdirectory, leave blank to omit:\n')

project = 'advent-of-code' if project == '' else project
day_prefix = 'day-' if day_prefix == '' else day_prefix
input_file = 'input.txt' if input_file == '' else input_file
example_file = 'example.txt' if example_file == '' else example_file
env = 'aoc' if env == '' else env
ide = 'code' if ide == '' else ide

out = f'''export AOC_SESSION={session}
export AOC_URL=https://adventofcode.com

export AOC_YEAR=15
export AOC_DAY=1
export AOC_LEVEL=1

export AOC_PROJECT_DIR={os.getcwd()}/{project}/
export AOC_SRC_DIR={source}
export AOC_RES_DIR={resource}
export AOC_SRC_SUBDIR={inner_source}
export AOC_RES_SUBDIR={inner_resource}

export AOC_MODULE_PREFIX={module}
export AOC_SRC_YEAR_PREFIX={src_year_prefix}
export AOC_RES_YEAR_PREFIX={res_year_prefix}
export AOC_DAY_PREFIX={day_prefix}

export AOC_INPUT_FILE={input_file}
export AOC_EXAMPLE_FILE={example_file}
export AOC_ENV_FILE={env}.env

export AOC_IDE={ide}
'''

with open(f'{work_dir}/envs/{env}.env', 'wt') as f:
    f.write(out)
    f.close()

with open(f'{work_dir}/envs/current.env', 'wt') as f:
    f.write(f'export AOC_ENV_FILE={env}.env')
    f.close()
