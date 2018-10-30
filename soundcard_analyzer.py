import soundcard as sc
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
import os
import random
import time
import flipperServer as flpr
import sys


PI = np.pi  # 3.14159... (the angle of a circle)
SAMPLERATE = 44100  # A samplerate supported by nearly all devices
data = []  # Recorded data will be stored here
CHUNK = 2048

print("DEFAULT PLAYBACK DEVICE:")
try:
	default_speaker = sc.default_speaker()
	print(default_speaker)
	pass
except Exception:
	print("Unable to find default playback devices.")
	pass


emptyData = [0.0] * 4096

# create matplotlib figure and axes
fig, ax = plt.subplots(1, figsize=(15, 7))

"""
PLOT DATA AND FFT
"""
print('Plotting...')
# plt.figure(1)
# plt.plot(flpr.getXPoints(emptyData), flpr.getYPoints(emptyData), 'black')

# plt.figure(2)
# plt.plot(flpr.getXPoints(emptyData), flpr.getYPoints(emptyData), 'orange')

print("DEFAULT RECORDING DEVICE:")
try:
	default_mic = sc.default_microphone()
	print(default_mic)
	pass
except Exception:
	print("Unable to find default recording device.")
	pass

# variable for plotting
x = np.arange(0, 2 * CHUNK, 2)

# create a line object with random data
line, = ax.plot(x, np.random.rand(CHUNK), 'orange', lw=2)

plt.setp(ax, xticks=[0, CHUNK, 2 * CHUNK], yticks=[0, 50, 100, 150, 200, 250])

plt.show(block=False)  # Show all figures


# for measuring frame rate
frame_count = 0
start_time = time.time()

while True:

	data = default_mic.record(samplerate=SAMPLERATE, numframes=(SAMPLERATE))
	line.set_ydata(flpr.flattenData(data))
	   
	# update figure canvas
	fig.canvas.draw() 
	fig.canvas.flush_events()
	frame_count += 1
		

# # Store microphone data for 2 seconds into data array
# try:
# 	data = flpr.recordAndPlay(default_mic, default_speaker, 2)
# except ValueError as err:
# 	sys.exit(err)

# flatData = flpr.flattenData(data)
# dataFFT = flpr.FFT(data)

# print('Plotting...')
# plt.figure(1)
# plt.plot(flpr.getXPoints(flatData), flpr.getYPoints(flatData), 'black')

# plt.figure(2)
# plt.plot(flpr.getXPoints(dataFFT), flpr.getYPoints(dataFFT), 'orange')
# plt.title('FFT of data')
# plt.xlabel('Actual Frequency')
# plt.ylabel('Prevalence of Frequency')

# flpr.plotDataAndFFT(data)




# Plot data BEFORE loading file containing ambient sounds
# flpr.plotDataAndFFT(data)

# load from file
# data = np.load(os.path.join("data", 'ambient18000.npy'))

#Store in file
#np.save(os.path.join("data", 'test1.npy'), data)



# TODO: Create a function that will play the data, when it is given as a parameter


# Plot data AFTER loading file containing ambient sounds
# flpr.plotDataAndFFT(data)

# dataFFT = flpr.FFT(data)

# #checks if frequency is between 9900 and 10000
# index = 9900
# while index < 10000:
# 	index = index + 1
# 	if dataFFT[index] >= 10:
# 		print ("0")
# 		break

# #checks if frequency is between 17900 and 18000
# index = 17900
# while index < 18000:
# 	index = index + 1
# 	if dataFFT[index] >= 10:
# 		print(dataFFT[index])
# 		print ("1")
# 		break
