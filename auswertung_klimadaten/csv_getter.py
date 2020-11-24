import csv
import os
from datetime import datetime as dt
from collections import defaultdict

directory = 'data_wetter'
final_file = [["Jahr", "Temperatur-Minimum(C)", "Temperatur-Mittelwert(C)", "Temperatur-Maximum(C)", "Bodentemperatur-Minimum(C)", "Sonnenstunden(h)", "Relative Luftfeuchtigkeit(%)", "Regen(mm)", "Niederschlagsform(num)", "Schnee(cm)", "Neuschnee(cm)", "Windgeschwindigkeit-Maximum(km/h)", "Windgeschwindigkeit-Mittelwert(km/h)"]]
temp_file = defaultdict(list)
n = 0

for filename in os.listdir(directory):
    n += 1
    with open(directory + '\\' + filename) as f:
        fr = csv.reader(f)

        for line in fr:
            if line[0] == 'Produkt_Code':
                continue

            key = dt.strptime(line[2], '%Y%m%d').date()
            value = line[3]
            temp_file[key].append(value)

        for key in temp_file:
            if len(temp_file[key]) != n:
                temp_file[key].append("n/A")

for key in temp_file:
    line = []
    line.append(key)
    line = line + temp_file[key]
    final_file.append(line)

with open('clima_data.csv', 'w') as f:
    w = csv.writer(f)
    w.writerows(final_file)