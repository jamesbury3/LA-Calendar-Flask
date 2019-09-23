import csv
import collections

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
    def addHours(self):
        self.hours = int(self.hours)+1

with open('csv_files/fall19cohort.csv') as csvfile:                      #might need to change slashes to work on mac
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
                        LAs[row_number - 1].shifts.append(column)

                        if not times.__contains__(column) and int(LAs[row_number - 1].hours) > 0:  #if the dictionary of shifts doesnt have this time then 
                            times[str(column)] = []                          # it gets added with the current LA
                            times[str(column)].append(LAs[row_number - 1])
                            LAs[row_number - 1].subtractHours()

                        else:
                            if int(LAs[row_number - 1].hours) > 0:
                                times[str(column)].append(LAs[row_number - 1])   #else it just adds the la to that shift
                                LAs[row_number - 1].subtractHours()
                                if len(times[str(column)]) > 5:
                                    least = LAs[row_number - 1]
                                    for other in times[str(column)]:
                                        if least.hours > other.hours:
                                            least =  other
                                    times[str(column)].remove(least)
                                    least.addHours()
                
                column_number += 1

        row_number += 1
        column_number = 0




for la in LAs:
    for time in la.shifts:
        if int(la.hours)>0 and not times.__contains__(time):
            times[str(time)] = []
            times[str(time)].append(la)
            la.subtractHours()
        else:
            if int(la.hours)>0 and len(times[str(time)]) < 5 and not times[str(time)].__contains__(la):
                times[str(time)].append(la)
                la.subtractHours()        



with open('csv_files/shift_times.csv') as csvfile: 
        reader1 = csv.reader(csvfile, delimiter=',', quotechar='|', skipinitialspace=True)
        for row in reader1:
            for column in row:
                times_to_fill.append(str(column))

for t in times_to_fill:
    if t not in times:
        las_with_curr_shift = []
        for la in LAs:
            if la.shifts.__contains__(str(t)):
                las_with_curr_shift.append(la)
        for la in las_with_curr_shift:
            for s in la.shifts:
                if times.__contains__(str(s)):
                    if times[str(s)].__contains__(la):
                        if len(times[str(s)]) > 1:
                            #print(la.name, "can be redistributed from ", str(s), "to ", str(t) )
                            times[str(t)] = []
                            times[str(t)].append(la)
                            times[str(s)].remove(la)
                            #print("moved ", la.name, "from ", str(s), "to ", str(t) )
                            break
            break

for la in LAs:
    for time in la.shifts:
        if int(la.hours)>0 and not times.__contains__(time):
            times[str(time)] = []
            times[str(time)].append(la)
            la.subtractHours()
        else:
            if int(la.hours)>0 and len(times[str(time)]) < 5 and not times[str(time)].__contains__(la):
                times[str(time)].append(la)
                la.subtractHours()

for la in LAs:
    for time in la.shifts:
        if int(la.hours)>0 and not times.__contains__(time):
            times[str(time)] = []
            times[str(time)].append(la)
            la.subtractHours()
        else:
            if int(la.hours)>0 and len(times[str(time)]) < 5 and not times[str(time)].__contains__(la):
                times[str(time)].append(la)
                la.subtractHours()
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
    for t in times_to_fill:
        s += t + '</p>'
        for la in times_to_fill.get(t):
            s += '<p style=\"margin-left: 40px\">' + la.name + '</p><p>'
    return s

def getTimesAndLAs():
    times_and_las = collections.OrderedDict()                   #creates dictionary with key time and value of a string of the
                                                                # la names
    with open('csv_files/shift_times.csv') as csvfile: 
        reader1 = csv.reader(csvfile, delimiter=',', quotechar='|', skipinitialspace=True)
        for row in reader1:
            for column in row:
                if times.__contains__(column):     
                    times_and_las[column] = ''
                    i = 0
                    for la in times[column]:
                        if i == 0:    
                            times_and_las[column] += la.name
                        else:
                            times_and_las[column] += ', ' + la.name
                        i += 1  
            i = 0


        times_and_las["Thur 11-12"] += ", Amanda Gustafson"
        times_and_las["Thur 12-1"] += ", Amanda Gustafson"
        times_and_las["Fri 4-5"] += ", Andrew Wortas"
        times_and_las["Fri 10-11"] += ", Christopher Cui"
        times_and_las["Fri 3-4"] += ", Dana Rubin"
        times_and_las["Fri 4-5"] += ", Dana Rubin"
        times_and_las["Wed 3-4"] += ", Daniel Koceja"
        times_and_las["Monday 2-3"] += ", Jacob Gersfeld"
        times_and_las["Thur 4-5"] += ", Janelle Zeng"
        times_and_las["Fri 2-3"] += ", Komal Essarani"
        times_and_las["Fri 3-4"] += ", Komal Essarani"
        times_and_las["Fri 4-5"] += ", Komal Essarani"
        times_and_las["Monday 2-3"] += ", Anh Nguyen"
        times_and_las["Wed 12-1"] += ", Ruchi Sarkar"
        times_and_las["Fri 1-2"] += ", Mira Kasari"
        times_and_las["Fri 9-10"] += ", Matthew Guo"
        times_and_las["Fri 11-12"] += ", Tharun Kintali"
        times_and_las["Thur 3-4"] += ", Sam Catalano"



        times_and_las["Wed 11-12"] = times_and_las["Wed 11-12"].replace('Amanda Gustafson, ', '')
        times_and_las["Wed 11-12"] = times_and_las["Wed 11-12"].replace('Komal Essarani, ', '')
        times_and_las["Wed 2-3"] = times_and_las["Wed 2-3"].replace('Komal Essarani, ', '')
        times_and_las["Wed 12-1"] = times_and_las["Wed 12-1"].replace('Amanda Gustafson, ', '')
        times_and_las["Wed 9-10"] = times_and_las["Wed 9-10"].replace('Andrew Wortas, ', '')
        times_and_las["Tues 2-3"] = times_and_las["Tues 2-3"].replace('Christopher Cui, ', '')
        times_and_las["Wed 10-11"] = times_and_las["Wed 10-11"].replace('Dana Rubin, ', '')
        times_and_las["Wed 3-4"] = times_and_las["Wed 3-4"].replace('Dana Rubin, ', '')
        times_and_las["Wed 3-4"] = times_and_las["Wed 3-4"].replace('Komal Essarani, ', '')
        times_and_las["Monday 12-1"] = times_and_las["Monday 12-1"].replace('Daniel Koceja, ', 'Jacob Gersfeld, ')
        times_and_las["Wed 1-2"] = times_and_las["Wed 1-2"].replace('Huanran Meng, ', '')
        times_and_las["Monday 2-3"] = times_and_las["Monday 2-3"].replace('Komal Essarani, ', '')
        times_and_las["Monday 2-3"] = times_and_las["Monday 2-3"].replace('Mira Kasari, ', '')
        times_and_las["Monday 4-5"] = times_and_las["Monday 4-5"].replace('Janelle Zeng, ', '')
        times_and_las["Monday 9-10"] = times_and_las["Monday 9-10"].replace('Dana Rubin, ', '')
        times_and_las["Monday 11-12"] = times_and_las["Monday 11-12"].replace('Matthew Guo, ', '')
        times_and_las["Monday 12-1"] = times_and_las["Monday 12-1"].replace('Tharun Kintali', '')
        times_and_las["Tues 4-5"] = times_and_las["Tues 4-5"].replace('Sam Catalano, ', '')



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

#print(getTimesAndLAs())
