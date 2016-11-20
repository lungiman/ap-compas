import matplotlib.pyplot as plt
import numpy as np
import math
#import statistics
from scipy.signal import hilbert, chirp

t=[0,45,90,135,180,225]
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
	
#	Y.append(float(sum(rssi)/i))
#	X.append(t[count])
	s = len(rssi)
	s = s/ 90
	cnt = 0
	i = 0
	for val	in rssi:
		Y.append(val)
		i = i + 1
		if i > s:
			i = 0
			cnt = cnt + 1
		X.append(cnt)
		print "%d %d" %(val,cnt)
	
	count = count + 1
	f.close()

filenames = ['0degree']
#filenames = ['0degree','90degree']

for a in filenames:
	extract(a)
analytic_signal = hilbert(Y)
#plt.plot(X,analytic_signal)
amplitude_envelope = np.abs(analytic_signal)
#print amplitude_envelope
#plt.plot(X,amplitude_envelope)
plt.plot(X,Y)
plt.show()
#fig = plt.figure()
#ax0 = fig.add_subplot(211)
#ax0.plot(X, Y, label='signal')
#ax0.plot(X, amplitude_envelope, label='envelope')
#ax0.set_xlabel("time in seconds")
#ax0.legend()
