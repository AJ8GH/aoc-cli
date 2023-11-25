#!/bin/zsh

work_dir=$(dirname "${0}")
answer=${1}
level=${2}
year=${3}
day=${4}

session="${AOC_SESSION}"
aoc_url="${AOC_URL}"
project_dir="${AOC_PROJECT_DIR}"

_submit() {
  url="${aoc_url}/20${year}/day/${day}"
  curl --cookie "session=${session}" "${url}/answer" -X POST -d "level=${level}&answer=${answer}"
}

_submit
