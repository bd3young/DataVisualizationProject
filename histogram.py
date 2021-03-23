import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data\\tcTempsYears.csv'
with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)

    dates, avergs = [], []
    for row in reader:
        currentDate = datetime.strptime(row[2], '%m/%d/%Y')
        if row[2] == '1/1/2010'or row[2] == '1/1/2011' or row[2] == '1/1/2012' or row[2] == '1/1/2013' or row[2] == '1/1/2014' or row[2] == '1/1/2015' or row[2] == '1/1/2016' or row[2] == '1/1/2017' or row[2] == '1/1/2018' or row[2] == '1/1/2019' or row[2] == '1/1/2020' or row[2] == '1/1/2021' :
            averg = int(float(row[5]))
            dates.append(currentDate)
            avergs.append(averg)
        
plt.hist(avergs, bins= 5, color= 'green')
plt.ylabel('Frequency')
plt.xlabel('Temp (F)')
plt.title('Tempuratures of January 1st for 11 years')
plt.show()