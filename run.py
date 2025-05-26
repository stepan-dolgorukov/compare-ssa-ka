#!/usr/bin/env python3

from random import getrandbits
from subprocess import Popen, PIPE
from sys import argv
from re import findall, finditer
from time import perf_counter

program_multiplication_karatsuba = \
  "/home/sdd/programming/multiplication-karatsuba/target/release/multiplication-karatsuba"

program_multiplication_schonhage_strassen = \
  "/home/sdd/programming/multiplication-schonhage-strassen/target/release/multiplication-schonhage-strassen"

length_bit = int(argv[1])
operand_left = getrandbits(length_bit)
operand_right = getrandbits(length_bit)

# print(operand_left, operand_right)
programs = [program_multiplication_karatsuba, program_multiplication_schonhage_strassen]
durations = {}

for program in programs:
  durations[program] = 0

amount_runs = 1

for position_program, program in enumerate(programs):
  for step in range(amount_runs):
    process = Popen([program], stdin=PIPE, stdout=PIPE, text=True)
    (output_stdout, _) = process.communicate(input=f"{operand_left} {operand_right}")
    # print(output_stdout)
    equality, duration = output_stdout.split('\n')[:2]
    matches = findall(r'\d+', equality)
    numbers = [int(match) for match in matches]
    match = finditer(r'(\d+) ns', duration)
    duration = int(next(match).group(1))
    durations[program] += duration

    # print(output_stdout)

    # assert numbers[0] == operand_left
    # assert numbers[1] == operand_right
    # assert numbers[2] == operand_left * operand_right

# print(f"{length_bit} {sum(stamps[0]) / len(stamps[0])} {sum(stamps[1]) / len(stamps[1])}" )

for program in durations:
  durations[program] /= amount_runs

print(f"{length_bit} {durations[program_multiplication_karatsuba]} {durations[program_multiplication_schonhage_strassen]}")
