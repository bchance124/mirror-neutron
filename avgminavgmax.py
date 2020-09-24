# email questions and bugs to bchance1@vols.utk.edu
# usage: python3 /path/to/avgminmax.py inputfile1 inputfile2 (>> outputfile)

# This file is used to output the average min and average max across all sensors 
#   for each axis
import sys

# shouldn't be changed, but included just in case
num_sensors = 6

class Sensor(object):
    def __init__(self):
        self.x = []
        self.y = []
        self.z = []
        self.total = []
# initialize num_sensors sensors
sensors =  [Sensor() for _ in range (num_sensors)]

#stores the mins and maxs for each sensor in x, y, and z
minsx = []
maxsx = []
minsy = []
maxsy = []
minsz = []
maxsz = []

# time isn't used in calculations at the moment but may be needed in the further
time = []


for k in range (len(sys.argv)):
    # sys.avgv[0] is the name of the python file, namely avgminmax.py    
    if k == 0:
        continue
    # makes sure all values are empty before starting next file
    minsx.clear()
    maxsx.clear()
    minsy.clear()
    maxsy.clear()
    minsz.clear()
    maxsz.clear()
    for i in range(num_sensors):
        sensors[i].x.clear()
        sensors[i].y.clear()
        sensors[i].z.clear()
        sensors[i].total.clear()

    filename = sys.argv[k]
    with open(filename, 'r') as f:
        print(filename)
        lines = f.read().splitlines()
        for i, line in enumerate(lines):
            if i != 0:
                vals = line.split()
                # allows either comma seperated time(20) or not (19) 
                if len(vals) != 19 and len(vals) != 20:
                    continue
                for j in range(num_sensors):
                    sensors[j].x.append(float(vals[j*3]))
                    sensors[j].y.append(float(vals[j*3+1]))
                    sensors[j].z.append(float(vals[j*3+2]))
                    sensors[j].total.append((float(vals[j*3])**2+float(vals[j*3+1])**2+float(vals[j*3+2])**2)**0.5)
                if (vals[num_sensors*3] == ','):
                    time.append(int(vals[num_sensors*3+1]))
                else:
                    time.append(int(vals[num_sensors*3]))
    
    # takes min and max values for each axis of each sensor
    for i in range(len(sensors)): 
        minsx.append(min(sensors[i].x))
        maxsx.append(max(sensors[i].x))    
        minsy.append(min(sensors[i].y))
        maxsy.append(max(sensors[i].y))
        minsz.append(min(sensors[i].z))
        maxsz.append(max(sensors[i].z))
    
    # averages the min/max for each axis across all sensors
    avgminx = sum(minsx)/float(len(minsx))
    avgmaxx = sum(maxsx)/float(len(maxsx))
    avgminy = sum(minsy)/float(len(minsy))
    avgmaxy = sum(maxsy)/float(len(maxsy))
    avgminz = sum(minsz)/float(len(minsz))
    avgmaxz = sum(maxsz)/float(len(maxsz))
    
    print("\"The average x min is: \"", avgminx, "\" uT\"")
    print("\"The average x max is: \"", avgmaxx, "\" uT\"")
    print("\"The average y min is: \"", avgminy, "\" uT\"")
    print("\"The average y max is: \"", avgmaxy, "\" uT\"")
    print("\"The average z min is: \"", avgminz, "\" uT\"")
    print("\"The average z max is: \"", avgmaxz, "\" uT\"")
    
    print("") #prints a newline