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
	
	Y.append(float(sum(rssi)/i))
	X.append(t[count])
	print rssi
	count = count + 1
	f.close()

filenames = ['0degree','45degree','90degree','135degree','180degree']

for a in filenames:
	extract(a)
analytic_signal = hilbert(Y)
#plt.plot(X,analytic_signal)
amplitude_envelope = np.abs(analytic_signal)
print amplitude_envelope
#plt.plot(X,amplitude_envelope)
plt.plot(X,Y)
plt.show()
#fig = plt.figure()
#ax0 = fig.add_subplot(211)
#ax0.plot(X, Y, label='signal')
#ax0.plot(X, amplitude_envelope, label='envelope')
#ax0.set_xlabel("time in seconds")
#ax0.legend()
