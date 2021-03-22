import matplotlib.pyplot as plt
from numpy.random import random

filename = 'data\michigan.csv'
with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)
    
    gtPop, leePop, wexPop, benzPop = [], [], [], []
    for row in reader:
        if row[8] == 'Grand Traverse County':
            for num in range(12,21):
                gtPop.append(row[num])

        if row[8] == 'Leelanau County':
            for num in range(12,21):
                leePop.append(row[num])

        if row[8] == 'Wexford County':
            for num in range(12,21):
                wexPop.append(row[num])

        if row[8] == 'Benzie County':
            for num in range(12,21):
                benzPop.append(row[num])