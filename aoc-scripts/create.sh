#!/bin/zsh

work_dir=$(dirname "${0}")
year=${1}
day=${2}
src_path=${3}
res_path=${4}
test_path=${5}
create_skeleton_code=${6}
force=${7}
readme=${8}
example_answer=${9}
level=${10}

session="${AOC_SESSION}"
aoc_url="${AOC_URL}"
input_file="${AOC_INPUT_FILE}"
example_file="${AOC_EXAMPLE_FILE}"

_create_directories() {
  mkdir -p "${src_path}"
  mkdir -p "${test_path}"
  mkdir -p "${res_path}"
}

_create_example() {
  example="${res_path}${example_file}"
  if [[ $force == 1 || ! -f "${example}" ]]; then
    text=$(python "${work_dir}/example.py" "${res_path}README.md")
    echo "$text" >"${example}"
  fi
}

_create_readme() {
  if [[ $readme == 1 ]]; then
    md=$(node "${work_dir}/markdown.js" "${year}" "${day}" "${session}")
    echo "${md}" >"${res_path}README.md"
    python "${work_dir}/readme.py" "${res_path}/README.md"
  fi
}

_get_input() {
  input="${res_path}${input_file}"
  if [[ $force == 1 || ! -f "${input}" ]]; then
    url="${aoc_url}/20${year}/day/${day}"
    curl --cookie "session=${session}" "${url}/input" >"${input}"
  fi
}

_create_files() {
  src_file="${src_path}Day${day}.java"
  src_template="$AOC_SRC_CODE_GEN_FILE"
  if [[ ! -f "${src_file}" ]]; then
    cat "$src_template" > "${src_file}"
    sed -i.bak "s/\${year}/${year}/" "${src_file}"
    sed -i.bak "s/\${day}/${day}/" "${src_file}"
    rm "${src_file}.bak"
  fi

  test_file="${test_path}Day${day}Test.java"
  test_template="$AOC_TEST_CODE_GEN_FILE"
  if [[ ! -f "${test_file}" ]]; then
    cat "$test_template" > "${test_file}"
    sed -i.bak "s/\${year}/${year}/" "${test_file}"
    sed -i.bak "s/\${day}/${day}/" "${test_file}"
    rm "${test_file}.bak"
  fi
}

echo "Creating files for 20${year} day ${day}..."
_create_directories
_create_readme
_create_example
_get_input

if [[ ${create_skeleton_code} == 1 ]]; then
  _create_files
fi

if [[ ${example_answer} == 1 ]]; then
  python "${work_dir}/answer.py" "${res_path}README.md" "${test_path}Day${day}Test.java" "${level}"
  mv "${test_path}Day${day}Test.java1" "${test_path}Day${day}Test.java"
fi
