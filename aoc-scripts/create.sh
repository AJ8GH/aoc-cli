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
  if [[ ! -f "${src_file}" ]]; then
    cat >"${src_file}" <<EOL
package io.github.aj8gh.aoc.y${year}.d${day};

import java.util.List;

public class Day${day} {

  public int part1(List<String> input) {
    return 0;
  }

  public int part2(List<String> input) {
    return 0;
  }
}
EOL
  fi

  test_file="${test_path}Day${day}Test.java"
  if [[ ! -f "${test_file}" ]]; then
    cat >"${test_file}" <<EOL
package io.github.aj8gh.aoc.y${year}.d${day};

import static org.junit.jupiter.api.Assertions.assertEquals;

import io.github.aj8gh.aoc.util.InputProvider;
import java.util.List;
import java.util.stream.Stream;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

class Day${day}Test extends InputProvider {

  private Day${day} classUnderTest;

  @BeforeEach
  void setUp() {
    classUnderTest = new Day${day}();
  }

  @ParameterizedTest
  @MethodSource(value = INPUT_PROVIDER_PART_1)
  void part1(List<String> input, int expected) {
    var actual = classUnderTest.part1(input);
    assertEquals(expected, actual);
  }

  @ParameterizedTest
  @MethodSource(value = INPUT_PROVIDER_PART_2)
  void part2(List<String> input, int expected) {
    var actual = classUnderTest.part2(input);
    assertEquals(expected, actual);
  }

  private static Stream<Arguments> inputProviderPart1() {
    return getInput(0, 0);
  }

  private static Stream<Arguments> inputProviderPart2() {
    return getInput(0, 0);
  }

  private static Stream<Arguments> getInput(int example, int result) {
    return Stream.of(
        Arguments.of(reader().getExample(DAY_${day}).asStringList(), example),
        Arguments.of(reader().getInput(DAY_${day}).asStringList(), result)
    );
  }
}
EOL
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
