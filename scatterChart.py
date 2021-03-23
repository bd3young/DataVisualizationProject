import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data\\tcTemps.csv'
with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)

    dates, avergs = [], []
    for row in reader:
        currentDate = datetime.strptime(row[2], '%m/%d/%Y')
        averg = int(row[5])
        dates.append(currentDate)
        avergs.append(averg)

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, avergs, c= 'red')

    # format chart
    ax.set_title('Daily average Temps, for Traverse City 2020', fontsize = 18)
    ax.set_xlabel('Days', fontsize = 16)
    fig.autofmt_xdate()
    ax.set_ylabel('Temps (F)', fontsize = 16)
    ax.tick_params(axis = 'both', which = 'major', labelsize = 16)

    plt.show()