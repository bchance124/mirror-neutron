# email questions and bugs to bchance1@vols.utk.edu
# Occasionally the program will fail if data has incomplete lines, once 
#   erasing these lines the program will run as expected

# Usage: python3 ~/path/to/plot6.py inputfile (optional title for graph)

# This program plots data for sensors in seperate windows, for each sensor showing
#   x, y, z, and total data 

import sys # used for input file and option title
import matplotlib.pyplot as plt

# shouldn't be changed, but included just in case
num_sensors = 6

# stores for each sensor
class Sensor(object):
    def __init__(self):
        self.x = []
        self.y = []
        self.z = []
        self.total = []

# initializes array of num_sensors sensors
sensors =  [Sensor() for _ in range (num_sensors)]

time = []

filename = sys.argv[1]

# read in the xyz data and calculate total values
with open(filename, 'r') as f:
    lines = f.read().splitlines()
    for i, line in enumerate(lines):
        if i != 0:
            vals = line.split()
            if len(vals) != 19 and len(vals) != 20: # checks for incomplete lines,
                                                    # fails occasionally anyway                                                       
                continue
            # next block checks if the line is actually the date            
            stop = 0
            for k in range(len(vals)):
                index = vals[k].find('/')
                if index != -1:
                    stop = 1
            if stop == 1:
                continue

            # adds data into objects to be printed later (float is needed to
            # convert from string)
            for j in range(num_sensors):
                sensors[j].x.append(float(vals[j*3]))
                sensors[j].y.append(float(vals[j*3+1]))
                sensors[j].z.append(float(vals[j*3+2]))
                sensors[j].total.append((float(vals[j*3])**2+float(vals[j*3+1])**2+float(vals[j*3+2])**2)**0.5)
            # if else statements allow for xyz data to be seperate from time data
            if (vals[num_sensors*3] == ','):
                time.append(int(vals[num_sensors*3+1]))
            else:
                time.append(int(vals[num_sensors*3]))

# automatically scales the x axis, maybe should add day option?
if time[len(time)-1] > (3600*5):
    for i in range(len(time)):
        time[i] /= 3600.0
        tUnit = 'Hours'
elif time[len(time)-1] > (60*5):
    for i in range(len(time)):
        time[i] /= 60.0
        tUnit = 'Minutes'
else:
    tUnit = 'Seconds'
fig = plt.figure(figsize=(20,10))
#order = [1,2,3,4,5,0] //used if running data generated 
#                      right after sensors were replaced
#                       ~week of July 17th, exact dates will be known soon
order = [1,2,3,4,5,6]

#plots the data 
for i, val in enumerate(order):
    fig.add_subplot(2,3,i+1)
    x, = plt.plot(time, sensors[i].x, 'red')
    y, = plt.plot(time, sensors[i].y, 'blue')
    z, = plt.plot(time, sensors[i].z, 'green')    
    plt.xlabel(tUnit, fontsize = 24)
    plt.ylabel('  uT', fontsize=24)
    plt.title('Sensor #%d' %(int(i) + 1), fontsize=12) #could be changed to mG if needed later
    total, = plt.plot(time, sensors[i].total, 'black')
    plt.legend([x,y,z,total], ['x','y','z','total'], bbox_to_anchor=(1.01, 1), loc='upper left',fontsize=12)
# code to add title if one is provided
graphTitle = input('Title?\n')
plt.suptitle(graphTitle, fontsize = 24)
plt.show()