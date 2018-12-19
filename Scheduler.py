import csv

row_number = 0
column_number = 0

LAs = []

class LA:                       #creates LA Class with a name, hours which should be a list of shift objects
    def __init__(self, name, hours, shifts):
        self.name = name
        self.hours = hours
        self.shifts = shifts
        self.worked = 0

with open('csv_files\\responses3.csv') as csvfile:                      #might need to change slashes to work on mac
    reader = csv.reader(csvfile, delimiter=',', quotechar='|', skipinitialspace=True)
    for row in reader:
        if row_number > 0:
            print('row number: ' + str(row_number))
            
            for column in row:
                if column != '' and column_number > 0:
                    print('column number: ' + str(column_number))
                    print(column.replace('"', ''))

                    if column_number == 1:          #adds the LA's name into LAs
                        LAs.append(LA(column, 0, []))
                    
                    if column_number == 2:
                        LAs[row_number - 1].hours = column

                    if column_number > 2:
                        LAs[row_number - 1].shifts.append(column)
                
                column_number += 1

        row_number += 1
        column_number = 0

iterator = 0

for ta in LAs:
    print(iterator)
    print(ta.name)
    print(ta.shifts)
    iterator += 1
