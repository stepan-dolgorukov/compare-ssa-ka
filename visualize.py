#!/usr/bin/env python3

import matplotlib.pyplot as pyplot
import sys

durations = {
  "karatsuba": {},
  "schonhage-strassen": {}
}

with open("run.text") as input:
  line = ""

  while line := input.readline():
    line = line.strip()

    if len(line) == 0:
      continue

    length_as_string, duration_karatsuba_as_string, duration_schonhage_strassen_as_string = line.split()
    length = int(length_as_string)
    duration_karatsuba = float(duration_karatsuba_as_string)
    duration_schonhage_strassen = float(duration_schonhage_strassen_as_string)

    if length in durations["karatsuba"]:
      print("Время выполнения алгоритма Карацубы для операндов длины {} уже известно.")
      exit(1)

    if length in durations["schonhage-strassen"]:
      print("Время выполнения алгоритма Шонхаге-Штрассена для операндов длины {} уже известно.")
      exit(1)

    durations["karatsuba"][length] = duration_karatsuba
    durations["schonhage-strassen"][length] = duration_schonhage_strassen

if durations["karatsuba"].keys() != durations["schonhage-strassen"].keys():
  print("Неравенство множеств длин")
  exit(1)

x_k = sorted(durations["karatsuba"].keys())
y_k = [None] * len(x_k)

for length in x_k:
  y_k[length - 1] = durations["karatsuba"][length]

x_ss = sorted(durations["schonhage-strassen"].keys())
y_ss = [None] * len(x_ss)

for length in x_ss:
  y_ss[length - 1] = durations["schonhage-strassen"][length]

pyplot.yscale("log")
pyplot.plot(x_k, y_k, color="b", marker=",", linestyle=None, label="Алгоритм Карацубы")
pyplot.plot(x_ss, y_ss, color="g", marker=",", linestyle=None, label="Алгоритм Шенхаге-Штрассена")
pyplot.legend()
pyplot.xlabel("Длина операндов, биты")
pyplot.ylabel("Время вычисления произведения, наносекунды")
pyplot.show()
