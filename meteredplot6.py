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
num_meters = len(sys.argv) - 1

class Meter(object):
    def __init__(self):
        self.sensors = [Sensor() for _ in range (num_sensors)]
        self.time = []


# stores for each sensor
class Sensor(object):
    def __init__(self):
        self.x = []
        self.y = []
        self.z = []
        self.total = []

# initializes array of num_sensors sensors
#sensors =  [Sensor() for _ in range (num_sensors)]
#time = []
filenames = []
meters = [Meter() for _ in range(num_meters)]
for i in range(1, len(sys.argv)):
    filenames.append(sys.argv[i])

for m, filename in enumerate(filenames):
    
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
                    meters[m].sensors[j].x.append(float(vals[j*3]))
                    meters[m].sensors[j].y.append(float(vals[j*3+1]))
                    meters[m].sensors[j].z.append(float(vals[j*3+2]))
                    meters[m].sensors[j].total.append((float(vals[j*3])**2+float(vals[j*3+1])**2+float(vals[j*3+2])**2)**0.5)
                # if else statements allow for xyz data to be seperate from time data
                if (vals[num_sensors*3] == ','):
                    meters[m].time.append(int(vals[num_sensors*3+1]))
                else:
                    meters[m].time.append(int(vals[num_sensors*3]))

#plots the data 
for i in range(num_sensors):
    fig = plt.figure(figsize=(20,10))
    for m in range(num_meters):
        fig.add_subplot(3,3,m+1)
        x, = plt.plot(meters[m].time, meters[m].sensors[i].x, 'red')
        y, = plt.plot(meters[m].time, meters[m].sensors[i].y, 'blue')
        z, = plt.plot(meters[m].time, meters[m].sensors[i].z, 'green')    
        plt.xlabel('Seconds')
        plt.ylabel('uT')
        plt.title('Meter #{:d}'.format(int(m) + 1)) #could be changed to mG if needed later
        total, = plt.plot(meters[m].time, meters[m].sensors[i].total, 'black')
        plt.legend([x,y,z,total], ['x','y','z','total'])
    # code to add title if one is provided
    graphTitle = 'Sensor #{:d}'.format(i)
    plt.suptitle(graphTitle, fontsize = 20)
    plt.show()