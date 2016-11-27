import matplotlib.pyplot as plt
import numpy as np
import math
import sqlite3


#import statistics
from scipy.signal import hilbert, chirp

t=[0,45,90,135,180,225,270,315]
count = 0

Y = []
X = []


def extract(filename):
	global count
	global Y
	global X
	i = 0.00
	f = open(filename,"r")
	rssi = []
	for line in iter(f):
		if "QDATA" not in line:
			continue
		arr = line.split(",")
		if( int(arr[5]) != 0):
			rssi.append(int(arr[5]))
			i = i + 1
#			Y.append(int(arr[5]))
#			X.append(t[count])
	
	Y.append(float(sum(rssi)/i))
	X.append(t[count])
#	print rssi
	count = count + 1
	f.close()

filenames = ['0degree','45degree','90degree','135degree','180degree','225degree','270degree','315degree']

for a in filenames:
	extract(a)

#analytic_signal = hilbert(Y)
#plt.plot(X,analytic_signal)
#amplitude_envelope = np.abs(analytic_signal)
#print amplitude_envelope
#plt.plot(X,amplitude_envelope)
plt.plot(X,Y)
plt.savefig("plot.png")
#plt.show()
maxrssi = max(Y)
#print maxrssi
apdir = 0
for a,b in zip(X,Y):
    if(b == maxrssi):
        apdir = a
print apdir
conn = sqlite3.connect('results.db')
c = conn.cursor()
c.execute('INSERT INTO Results (Sector,Condition,Distance) VALUES (%d,"LOS","far")'%(apdir))
conn.commit()
conn.close()
