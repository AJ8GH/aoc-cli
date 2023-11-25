#!/bin/zsh

base_dir=$(readlink -f "$(dirname "${0}")")
env_dir="${base_dir}/envs"
source "${env_dir}/current.env"
source "${env_dir}/${AOC_ENV_FILE}"

_uninstall() {
  install_dir=${AOC_INSTALL_DIR}
  rm "${install_dir}/aoc-scripts"
  rm "${install_dir}/aoc"
}
