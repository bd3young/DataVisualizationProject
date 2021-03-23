import csv

filename = 'data\michiganAgeSex.csv'
with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)
    print(headerRow)

    for index, columnHeader in enumerate(headerRow):
        print(index, columnHeader)
    
    underThirteen = 0
    fifteenNineteen = 0
    twentyTwentynine= 0 
    thirtyThirtynine = 0
    fortyFortynine = 0
    fiftyFiftynine = 0
    sixtySixtynine = 0
    seventySeventynine = 0
    eightyAbove = 0
    for row in reader:
        if row[4] == 'Grand Traverse County' and row[5] == '1' or row[4] == 'Leelanau County' and row[5] == '1' or row[4] == 'Wexford County' and row[5] == '1' or row[4] == 'Benzie County' and row[5] == '1':
            underThirteen += int((row[9] + row[12]))
            fifteenNineteen += int(row[48])
            twentyTwentynine += int((row[51] + row[54]))
            thirtyThirtynine += int((row[57] + row[60]))
            fortyFortynine += int((row[63] + row[66]))
            fiftyFiftynine += int((row[69] + row[72]))
            sixtySixtynine += int((row[75] + row[78]))
            seventySeventynine += int((row[81] + row[84]))
            eightyAbove += int((row[87] + row[90]))
                    
                    

print(underThirteen)
print(fifteenNineteen)
print(twentyTwentynine)
print(thirtyThirtynine)
print(fortyFortynine)
print(fiftyFiftynine)
print(sixtySixtynine)
print(seventySeventynine)
print(eightyAbove)
    # print(gtAges)
    # print(leeAges)
    # print(wexAges)
    # print(benzAges)


            

