import csv
import matplotlib.pyplot as plt

filename = 'data\michiganAgeSex.csv'
with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)
    
    underfifteen = 0
    fifteenNineteen = 0
    twentyTwentynine= 0 
    thirtyThirtynine = 0
    fortyFortynine = 0
    fiftyFiftynine = 0
    sixtySixtynine = 0
    seventySeventynine = 0
    eightyAbove = 0
    ageGroups = []
    for row in reader:
        if row[4] == 'Grand Traverse County' and row[5] == '1' or row[4] == 'Leelanau County' and row[5] == '1' or row[4] == 'Wexford County' and row[5] == '1' or row[4] == 'Benzie County' and row[5] == '1':
            underfifteen += int(row[9])
            underfifteen += int(row[12])

            fifteenNineteen += int(row[48])

            twentyTwentynine += int(row[51])
            twentyTwentynine += int(row[54])

            thirtyThirtynine += int(row[57])
            thirtyThirtynine += int(row[60])

            fortyFortynine += int(row[63])
            fortyFortynine += int(row[66])

            fiftyFiftynine += int(row[69])
            fiftyFiftynine += int(row[72])

            sixtySixtynine += int(row[75])
            sixtySixtynine += int(row[78])

            seventySeventynine += int(row[81])
            seventySeventynine += int(row[84])

            eightyAbove += int(row[87])
            eightyAbove += int(row[90])
                    
    ageGroups.append(underfifteen)
    ageGroups.append(fifteenNineteen)   
    ageGroups.append(twentyTwentynine)
    ageGroups.append(thirtyThirtynine) 
    ageGroups.append(fortyFortynine)
    ageGroups.append(fiftyFiftynine) 
    ageGroups.append(sixtySixtynine)
    ageGroups.append(seventySeventynine) 
    ageGroups.append(eightyAbove)            

print(ageGroups)

labels = 'Under 15', '15 - 19', '20 - 29', '30 - 39', '40-49', '50 - 59', '60 - 69', '70 - 79', '80 Above'
explode = (.1, 0, 0, 0, 0, 0, 0, 0, 0)  # only "explode" the 1st wedge
wedgeColors=('green','blue','yellow','orange', 'purple', 'pink', 'turquoise', 'salmon', 'lavender')

fig1, ax1 = plt.subplots()
ax1.pie(ageGroups, explode=explode, labels=labels, autopct='%3.1f%%', shadow=True, startangle=0, colors=wedgeColors)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.suptitle("Age Groups in Grand Traverse, Benzie, Wexford, Leelanau Counties")

plt.show()