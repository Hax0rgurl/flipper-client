import pyaudio
import os
import struct
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import time

# constants
CHUNK = 1024 * 2             # samples per frame
FORMAT = pyaudio.paInt16     # audio format (bytes per sample?)
CHANNELS = 1                 # single channel for microphone
RATE = 44100  # samples per second
GRAPH_X_MIN = 800
# create matplotlib figure and axes
fig, ax2 = plt.subplots()

# pyaudio class instance
p = pyaudio.PyAudio()

# stream object to get data from microphone
stream = p.open(
	format=FORMAT,
	channels=CHANNELS,
	rate=RATE,
	input=True,
	output=True,
	frames_per_buffer=CHUNK
)

# variable for plotting
xf = np.linspace(0, RATE, CHUNK)[GRAPH_X_MIN:int(
	CHUNK/2)]     # frequencies (spectrum)

# create a line object with random data
# line, = ax1.plot(x, np.random.rand(CHUNK), '-', lw=2)

# create semilogx line for spectrum
line_fft, = ax2.plot(xf, np.random.rand(
	CHUNK)[GRAPH_X_MIN:int(CHUNK/2)], '-', lw=2)


# format waveform axes
ax2.set_title('Fourier Transform of Microphone Data - PyAudio')
ax2.set_xlabel('Frequency')
ax2.set_ylabel('Prevalence of Frequency')

plt.show(block=False)


OFFSET = 5
THRESH = 0.7
FQ_0 = 17800
FQ_1 = 17950
FQ_2 = 18100
FQ_3 = 18250
FQ_4 = 18400
FQ_5 = 18550
FQ_6 = 18700
FQ_7 = 18850
FQ_8 = 19000
FQ_9 = 19150
FQ_A = 19300
FQ_B = 19450
FQ_C = 19600
FQ_D = 19750
FQ_E = 19900
FQ_F = 20050

timerStart = time.time()

def findFreq(pData):

	for x,y in zip(xf, pData):
		if y >= THRESH:
			print(x)
			ax2.annotate('(%s, %s)' % (x,y), xy=(x,y), textcoords='data')

	# global timerStart # To allow us to use timerStart within this function's scope

	# # Frequency 0
	# for i in pData[FQ_0 - OFFSET:FQ_0 + OFFSET]:
	# 	if i >= THRESH:
	# 		# print(i)
	# 		print("Found a freq at " + FQ_0)
	# 		timerStart = time.time() # Reset the timer because we found a new beep

	# # Frequency 1
	# for i in pData[FQ_1 - OFFSET:FQ_1 + OFFSET]:
	# 	if i >= THRESH:
	# 		# print(i)
	# 		print("Found a freq at " + FQ_1)
	# 		timerStart = time.time() # Reset the timer because we found a new beep

	# # Frequency 2
	# for i in pData[FQ_2 - OFFSET:FQ_2 + OFFSET]:
	# 	if i >= THRESH:
	# 		# print(i)
	# 		print("Found a freq at " + FQ_2)
	# 		timerStart = time.time() # Reset the timer because we found a new beep

	# # Frequency 3
	# for i in pData[FQ_3 - OFFSET:FQ_3 + OFFSET]:
	# 	if i >= THRESH:
	# 		# print(i)
	# 		print("Found a freq at " + FQ_3)
	# 		timerStart = time.time() # Reset the timer because we found a new beep

	# # Frequency 4
	# for i in pData[FQ_4 - OFFSET:FQ_4 + OFFSET]:
	# 	if i >= THRESH:
	# 		# print(i)
	# 		print("Found a freq at " + FQ_4)
	# 		timerStart = time.time() # Reset the timer because we found a new beep

	# # Frequency 5
	# for i in pData[FQ_5 - OFFSET:FQ_5 + OFFSET]:
	# 	if i >= THRESH:
	# 		# print(i)
	# 		print("Found a freq at " + FQ_5)
	# 		timerStart = time.time() # Reset the timer because we found a new beep

	# # Frequency 6
	# for i in pData[FQ_6 - OFFSET:FQ_6 + OFFSET]:
	# 	if i >= THRESH:
	# 		# print(i)
	# 		print("Found a freq at " + FQ_6)
	# 		timerStart = time.time() # Reset the timer because we found a new beep

	# # Frequency 7
	# for i in pData[FQ_7 - OFFSET:FQ_7 + OFFSET]:
	# 	if i >= THRESH:
	# 		# print(i)
	# 		print("Found a freq at " + FQ_7)
	# 		timerStart = time.time() # Reset the timer because we found a new beep

	# # Frequency 8
	# for i in pData[FQ_8 - OFFSET:FQ_8 + OFFSET]:
	# 	if i >= THRESH:
	# 		# print(i)
	# 		print("Found a freq at " + FQ_8)
	# 		timerStart = time.time() # Reset the timer because we found a new beep

	# # Frequency 9
	# for i in pData[FQ_9 - OFFSET:FQ_9 + OFFSET]:
	# 	if i >= THRESH:
	# 		# print(i)
	# 		print("Found a freq at " + FQ_9)
	# 		timerStart = time.time() # Reset the timer because we found a new beep

	# # Frequency A
	# for i in pData[FQ_A - OFFSET:FQ_A + OFFSET]:
	# 	if i >= THRESH:
	# 		# print(i)
	# 		print("Found a freq at " + FQ_A)
	# 		timerStart = time.time() # Reset the timer because we found a new beep

	# # Frequency B
	# for i in pData[FQ_B - OFFSET:FQ_B + OFFSET]:
	# 	if i >= THRESH:
	# 		# print(i)
	# 		print("Found a freq at " + FQ_B)
	# 		timerStart = time.time() # Reset the timer because we found a new beep

	# # Frequency C
	# for i in pData[FQ_C - OFFSET:FQ_C + OFFSET]:
	# 	if i >= THRESH:
	# 		# print(i)
	# 		print("Found a freq at " + FQ_C)
	# 		timerStart = time.time() # Reset the timer because we found a new beep

	# # Frequency D
	# for i in pData[FQ_D - OFFSET:FQ_D + OFFSET]:
	# 	if i >= THRESH:
	# 		# print(i)
	# 		print("Found a freq at " + FQ_D)
	# 		timerStart = time.time() # Reset the timer because we found a new beep

	# # Frequency E
	# for i in pData[FQ_E - OFFSET:FQ_E + OFFSET]:
	# 	if i >= THRESH:
	# 		# print(i)
	# 		print("Found a freq at " + FQ_E)
	# 		timerStart = time.time() # Reset the timer because we found a new beep

	# # Frequency F
	# for i in pData[FQ_F - OFFSET:FQ_F + OFFSET]:
	# 	if i >= THRESH:
	# 		# print(i)
	# 		print("Found a freq at " + FQ_F)
	# 		timerStart = time.time() # Reset the timer because we found a new beep



while True:

	# binary data
	data = stream.read(CHUNK, exception_on_overflow=False)

	# convert data to integers, make np array, then offset it by 127
	data_int = struct.unpack(str(2 * CHUNK) + 'B', data)

	# create np array and offset by 128
	data_np = np.array(data_int, dtype='b') + 128
	# compute FFT and update line
	yf = fft(data_int)
	yf = (np.abs(yf[0:CHUNK]) / (128 * CHUNK))

	findFreq(yf[GRAPH_X_MIN:int(CHUNK/2)])
	line_fft.set_ydata(yf[GRAPH_X_MIN:int(CHUNK/2)])

	try:
		fig.canvas.draw()
		fig.canvas.flush_events()
		plt.pause(0.0001)
	except Exception:
		exit(0)
