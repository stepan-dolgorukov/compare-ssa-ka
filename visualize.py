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
    length_as_string, duration_karatsuba_as_string, duration_schonhage_strassen_as_string = line.split()
    length = int(length_as_string)
    duration_karatsuba = float(duration_karatsuba_as_string)
    duration_schonhage_strassen = float(duration_schonhage_strassen_as_string)
    data_karatsuba[int(length) - 1] = (length, duration_karatsuba)
    data_schonhage_strassen[int(length) - 1] = (length, duration_schonhage_strassen)

x_k, y_k = zip(*data_karatsuba)
x_ss, y_ss = zip(*data_schonhage_strassen)

# pyplot.figure(figsize=(6,4))
pyplot.plot(x_k, y_k, marker=',', linestyle=None, label='Функция 1')
pyplot.plot(x_ss, y_ss, marker=',', linestyle=None, label='Функция 2')
pyplot.xlabel('Длина, биты')
pyplot.ylabel('Полное время выполнения программы')
pyplot.show()
