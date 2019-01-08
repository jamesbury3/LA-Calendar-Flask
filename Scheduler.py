import csv

row_number = 0
column_number = 0

LAs = []                        #creates array of LA's in the csv
times = {}                      #creates dictionary with shifts as the key 
                                # and an array of LA's working at that time as the value
times_to_fill = []              #creates list of times to fill that must have at least one LA

class LA:                       #creates LA Class with a name, hours which should be a list of shift objects
    def __init__(self, name, hours, shifts):
        self.name = name
        self.hours = hours
        self.shifts = shifts
        self.worked = 0
    def subtractHours(self):
        self.hours = int(self.hours)-1

with open('csv_files/responses3.csv') as csvfile:                      #might need to change slashes to work on mac
    reader = csv.reader(csvfile, delimiter=',', quotechar='|', skipinitialspace=True)
    for row in reader:                                                  #iterates through the rows of the csv
        if row_number > 0:
            #print('row number: ' + str(row_number))
            
            for column in row:                                          #iterates through the columns of the current row
                if column != '' and column_number > 0:                  #only looks at columns that are important
                    # print('column number: ' + str(column_number))
                    # print(column.replace('"', ''))
                    column = column.replace('"', '')                    #gets rid of the "" in come of the times

                    if column_number == 1:                              #adds the LA's name into LAs array
                        LAs.append(LA(column, 0, []))

                    if column_number == 2:                               #adds the time to the LA's array of shifts
                        LAs[row_number - 1].hours = column

                    if column_number > 2:
                        #LAs[row_number - 1].shifts.append(column)

                        if not times.__contains__(column) and LAs[row_number - 1].hours > 0:  #if the dictionary of shifts doesnt have this time then 
                            times[str(column)] = []                          # it gets added with the current LA
                            times[str(column)].append(LAs[row_number - 1])
                            LAs[row_number - 1].subtractHours()

                        else:
                            if LAs[row_number - 1].hours > 0:
                                times[str(column)].append(LAs[row_number - 1])   #else it just adds the la to that shift
                                LAs[row_number - 1].subtractHours()
                                if len(times[str(column)]) > 3:
                                    least = LAs[row_number - 1]
                                    for other in times[str(column)]:
                                        if least.hours > other.hours:
                                            least =  other
                                    times[str(column)].remove(least)
                
                column_number += 1

        row_number += 1
        column_number = 0

with open('csv_files/shift_times.csv') as csvfile: 
    reader1 = csv.reader(csvfile, delimiter=',', quotechar='|', skipinitialspace=True)
    for row in reader1:
        for column in row:
            times_to_fill.append(str(column))
#prints out LA information:

#iterator = 0
# for ta in LAs:
#     print(iterator)
#     print(ta.name)
#     print(ta.shifts)
#     iterator += 1

#prints times and the la's in each slot
def getSchedule():

    s = ''
    # for server:
    for t in times:
        s += t + '</p>'
        for la in times.get(t):
            s += '<p style=\"margin-left: 40px\">' + la.name + '</p><p>'

    #for command prompt:
    # for t in times:
    #     #print(t)
    #     s += t + '\n'
    #     for la in times.get(t):
    #         s += '      '+la.name+'\n'
    #         #print('     '+la.name)
    return s

def getTimesAndLAs():
    times_and_las = {}                                          #creates dictionary with key time and value of a string of the
                                                                # la names
    for time in times:
        times_and_las[time] = ''
        i = 0

        for la in times[time]:
            if i == 0:    
                times_and_las[time] += la.name
            else:
                times_and_las[time] += ', ' + la.name
            i += 1

    return times_and_las

def getUnWorkedTimes():
    s = ''
    for t in times_to_fill:
        if str(t) not in times:
            s += str(t) + '</br>'
    return s

# print(getSchedule())
# print('Times not assigned:')
# print(getUnWorkedTimes())

print(getTimesAndLAs())
