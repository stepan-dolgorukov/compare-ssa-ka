#!/usr/bin/env bash

rm run.text

for length in $(seq 1 2048); do
  printf '%d\n' "${length}" >&2
  if ! ./run.py "${length}" >>run.text; then
    exit "${?}"
  fi
done
