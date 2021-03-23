import csv
import matplotlib.pyplot as plt
import numpy as np
filename = 'data\michigan.csv'
with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)
    
    years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
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

barWidth = .25

# position of bar on x axis
br1 = np.arange(len(years))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
br4 = [x + barWidth for x in br3]

plt.xticks([r + barWidth for r in range(len(years))], years)

plt.bar(br1, benzPop, color= 'blue', width= barWidth, label = "Benzie")
plt.bar(br2, wexPop, color= 'purple', width= barWidth, label = "Wexford")
plt.bar(br3, leePop, color= 'green', width= barWidth, label = "Leelanau")
plt.bar(br3, gtPop, color= 'orange', width= barWidth, label = "Grand Traverse")

plt.xlabel('Years')
plt.ylabel('Population')
plt.title('Estimated population', c='Purple', fontfamily='Comic Sans MS', fontsize= '25')
plt.legend(loc= 'best')

plt.show() 