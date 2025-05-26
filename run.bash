#!/usr/bin/env bash

rm run.text

for length in $(seq 1 2048); do
  ./run.py "${length}" >>run.text

  if [ "$?" -ne 0 ]; then
    exit 1
  fi
done
