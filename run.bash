#!/usr/bin/env bash

rm run.text

for length in $(seq 1 2048); do
  if ! ./run.py "${length}" >>run.text; then
    exit "${?}"
  fi
done
