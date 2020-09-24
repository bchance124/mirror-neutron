# email questions and bugs to bchance1@vols.utk.edu
# Occasionally the program will fail if data has incomplete lines, once 
#   erasing these lines the program will run as expected

# Usage: python3 ~/path/to/plot6.py inputfile (optional title for graph)

# This program plots data for sensors in seperate windows, for each sensor showing
#   x, y, z, and total data 

import sys # used for input file and option title
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d

num_sensors = 6
num_meters = int(sys.argv[2])

filename = sys.argv[1]

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


meters = [Meter() for _ in range(num_meters)]


stdevs = []

m = -1
with open(filename, 'r') as f:
    lines = f.read().splitlines()
    for i, line in enumerate(lines):
        vals = line.split()
        if len(vals) == 1:
          m += 1          
        if len(vals) != 9: # checks for incomplete lines,
                                                # fails occasionally anyway                                                       
            continue
        try:
            s = int(vals[0]) - 1
        except:
            continue
        
        try:
            meters[m].sensors[s].x.append(float(vals[1]))
        except:
            continue
        try:
            meters[m].sensors[s].y.append(float(vals[3]))
        except:
            continue
        try: 
            meters[m].sensors[s].z.append(float(vals[5]))
        except:
            continue
        try:
            meters[m].sensors[s].total.append(float(vals[7]))
        except:
            continue
        





fig = plt.figure()
ax = fig.gca(projection='3d')
pos1 = np.arange(0, num_meters)
pos2 = np.arange(0.5, num_meters + 0.5)
pos3 = np.arange(1, num_meters + 1)
left = np.full(num_meters, -0.5)
right = np.full(num_meters, 0.5)
lr = np.append(left, right)
height = np.zeros(num_meters)


leg = []
corder = ['blue', 'red', 'green', 'cyan', 'yellow', 'magenta']
for i in range(num_meters):
    for j in range(num_sensors):
        x = meters[i].sensors[j].x
        y = meters[i].sensors[j].y
        z = meters[i].sensors[j].z
        if j == 1 or j == 2 or j == 4:
            lr = left
        else:
            lr = right
        if j == 1 or j == 3:
            pos = pos1
        elif j == 2 or j == 5:
            pos = pos2
        else:
            pos = pos3
            
        leg.append(ax.quiver(lr, pos, height, np.asarray(x),np.asarray(y),np.asarray(z), length=0.1, color = corder[j]))
plt.xlabel("<--West East--> (m)")
plt.ylabel("<--South North--> (m)")
plt.zlabel('Height (m)')
plt.title(input("Title?\n"))
for i in range(num_sensors):
    plt.quiverkey(leg[i], 0.5,0.9-(i/15),25, "Sensor {}".format(i+1))

plt.show()