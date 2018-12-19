import csv
with open('csv_files\\responses1.csv') as csvfile:                      #might need to change slashes to work on mac
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        print('\n'.join(row))