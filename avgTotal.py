# email questions and bugs to bchance1@vols.utk.edu
# usage: python3 /path/to/avgTotal.py input_file1 inputfile2 ... (>> outputfile)
# writing to a file is optional, but useful as can be put into excel for more calculations
# Any number of input files can be used

# This file is used to show the avg x,y,z and total for each sensor for any number
#   of files


# This file needs a lot to be added to is such as stddev, sigma, and other ways
#   to calculate errors

import sys
from statistics import pstdev
# shouldn't need to be changed, included just in case
num_sensors = 6

class Sensor(object):
    def __init__(self):
        self.x = []
        self.y = []
        self.z = []
        self.total = []

# initializes an array of sensors num_sensors long
sensors =  [Sensor() for _ in range (num_sensors)]

time = []

# start at 1 because sys.argv[0] is the python file (avgTotal.py)
for k in range(1, len(sys.argv)):
    # prevents data between files being combined
    for i in range(num_sensors):
        sensors[i].x.clear()
        sensors[i].y.clear()
        sensors[i].z.clear()
        sensors[i].total.clear()    
    filename = sys.argv[k]
    print(filename)
    # read in the file
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        for i, line in enumerate(lines):
            if i != 0:
                vals = line.split()
                # allows data to be comma seperated with time(20) or not(19)
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
    
# prints the formatted data to standard output
    print("{:>11}{:>11}{:>11}{:>11}{:>11}{:>11}{:>11}{:>11}{:>11}".format('Sensor', 'AvgX', 
          'StDevX', 'AvgY', 'StDevY', 'AvgZ', 'StDevZ', 'AvgTotal', 'StDevTotal'))
    for i in range(len(sensors)):
        print('{:11d}{: 11.2f}{: 11.2f}{: 11.2f}{: 11.2f}{: 11.2f}{: 11.2f}{: 11.2f}{: 11.2f}'\
        .format(i+1,sum(sensors[i].x)/float(len(sensors[i].x)),pstdev(sensors[i].x),
        sum(sensors[i].y)/float(len(sensors[i].y)), pstdev(sensors[i].y),
        sum(sensors[i].z)/float(len(sensors[i].z)), pstdev(sensors[i].z),
        sum(sensors[i].total)/float(len(sensors[i].total)), pstdev(sensors[i].total)))