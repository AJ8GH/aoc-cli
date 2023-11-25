#!/bin/zsh

base_dir=$(readlink -f "$(dirname "${0}")")
env_dirname="${base_dir}/envs"
source "${env_dirname}/current.env"
source "${env_dirname}/${AOC_ENV_FILE}"

_resolve_install_dir() {
  install_dir=${AOC_INSTALL_DIR}
  if [[ -z ${install_dir} ]]; then
    install_dir='/usr/local/bin/'
  fi
}

_install() {
  ln -s "${base_dir}/../aoc" "${install_dir}"
  ln -s "${base_dir}" "${install_dir}"
}

_resolve_install_dir
_install
