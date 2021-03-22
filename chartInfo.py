import csv

filename = 'data\michigan.csv'
with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)
    print(headerRow)

    for index, columnHeader in enumerate(headerRow):
        print(index, columnHeader)
    
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

    print(gtPop)
    print(leePop)
    print(wexPop)
    print(benzPop)


            

