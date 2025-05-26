#!/usr/bin/env python3

import matplotlib.pyplot as pyplot
import sys

length = int(sys.argv[1])
data_karatsuba = [None] * length
data_schonhage_strassen = [None] * length

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
      exit(1)

    if length in durations["schonhage-strassen"]:
      exit(1)

    durations["karatsuba"][length] = duration_karatsuba
    durations["schonhage-strassen"][length] = duration_schonhage_strassen

x_k, y_k = zip(*durations["karatsuba"])
x_ss, y_ss = zip(*durations["schonhage-strassen"])

pyplot.yscale("log")
pyplot.plot(x_k, y_k, color="b", marker=",", linestyle=None, label="Алгоритм Карацубы")
pyplot.plot(x_ss, y_ss, color="g", marker=",", linestyle=None, label="Алгоритм Шенхаге-Штрассена")
pyplot.legend()
pyplot.xlabel("Длина операндов, биты")
pyplot.ylabel("Время вычисления произведения, наносекунды")
pyplot.show()
