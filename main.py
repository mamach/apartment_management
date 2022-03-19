import csv
import numpy

month = 'APRIL-2022'

file = open('params.csv')

csvreader = csv.reader(file)

header = []
header = next(csvreader)

rows = []
for row in csvreader:
    water_userd_liters = int(row[3])-int(row[2])
    water_charges=0
    if water_userd_liters <= 20000:
        water_charges = water_userd_liters*0.03
    else:
        water_charges = (20000 * 0.03) + (water_userd_liters-20000)*0.03
    past_dues = int(row[6])
    total = int(row[4]) + water_charges + past_dues
    row.append(water_charges)
    row.append(total)
    row.append('')
    row.append('')
    row.append('')
    row.append('')
    row.append('')
    rows.append(row)

file.close()

rowsHeader = ['FLAT', 'NAME','PREVIOUS','PRESENT','MAINTAINANCE','ARREARS','PAST DUES','WATER CHARGES','TOTAL', 'PAYMENT MODE', 'AMOUNT PAID', 'DATE PAID', 'SIGNATURE', 'PAID BY']

rows.insert(0, rowsHeader)

a = numpy.array(rows)


with open( month +'.csv', 'w', newline='') as file:
    mywriter = csv.writer(file, delimiter=',')
    mywriter.writerows(a)