## AOC: CLI Utility For Advent of Code

### Requirements
- Node.js
- Python 3
- ZSH

### Set-up:

Create file `.env` in `aoc-scripts` directory with the following properties:

```
export AOC_SESSION=<your-aoc-session-token>
export AOC_URL=<aoc-url>

export AOC_YEAR=<year>
export AOC_DAY=<day>
export AOC_LEVEL=<level>

export AOC_PROJECT_DIR=<location-of-aoc-project>
export AOC_SRC_DIR=<src-directory-within-module>
export AOC_RES_DIR=<resources-directory-within-module>
export AOC_SRC_SUBDIR=<subdirectory-within-src-dir>
export AOC_RES_SUBDIR=<subdirectory-within-resources-dir>

export AOC_MODULE_PREFIX=<prefix-of-module>
export AOC_SRC_YEAR_PREFIX=<prefix-for-year-package-in-source-dir>
export AOC_RES_YEAR_PREFIX=<prefix-for-year-dir-in-resources-dir>
export AOC_DAY_PREFIX=<prefix-for-day-subdirectory>

export IDE=<ide-or-editor-to-open-project>
```

####  Note:
* Session token cookie can be found in the browser dev tools when logged in on the AoC website
* `IDE` value must be an executable in order to work
* `INSTALL_DIR` value must be in PATH for cli to work
* resulting directory structure: 
  * Source: `project-dir/module-dir/source-dir/year-subdirectory/day-subdirectory/`
  * Resources: `project-dir/module-dir/resources-dir/day-subdirectory/`
  * `year-subdirectory` == year-prefix{year}
  * `day-subdirectory` == day-prefix{day}
  * `resources-subdirectory`: leave blank to omit resources subdirectory
  * `YEAR_PREFIX`: leave blank to omit year subdirectory
  * `DAY_PREFIX`: default value: `d`

### Usage:

Run executable with `aoc` command

#### Flags

`-i`

_Install_:
* Creates necessary symlinks to make aoc executable findable on `PATH`
---

`-u`

_Uninstall_:
* Removes symlinks to `aoc` executable from `PATH`
---

`-a <answer>`

_Answer_:
* Submits parameter as answer for selected year, day and level
---

`-D <new-day>`

_New Day_:
* Overrides `DAY` environment variable
---

`-Y <new-year>`

_New Year_:
* Overrides `YEAR` environment variable
---

`-L <new-level>`

_New Level_:
* Overrides `LEVEL` environment variable
---

`-c`

_Create_:
* Creates empty src and resources directories for selected year and day
* Creates input and example files
* Gets input from AoC website to create input file
* Gets problem description from AoC website to create `README.md` and formats into Markdown
---

`-s`

_Set_:
* Sets the `YEAR`, `DAY` and `LEVEL` environment variables to the values passed to `-Y`, `-D` and `-L` respectively
* Missing parameters are left unchanged
---

`-n`

_Next_:
* Advances to the next day
* `-y`, `-d` and `-l` can be combined to advance all or some of the fields, e.g. `aoc -nydl`
---

`-O <ide>`
  
_Open_:
* Opens AoC project with chosen IDE
---

`-o`

_Open_:
* Opens AoC project with default IDE
---

`-e`

_Echo_:
* Echoes current values for `YEAR`, `DAY` and `LEVEL` to the shell
---

`-I`

_Init_:
* Initialises a new project
* Set custom structure up via cli input
---

`-h`

_Help_:
* Shows help
