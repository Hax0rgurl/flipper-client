import soundcard as sc
import numpy
import os
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
PI = numpy.pi # 3.14159... (the angle of a circle)
SAMPLERATE=44100 # A samplerate supported by nearly all devices
VOLUME = 0.5     # range [0.0, 1.0]
FS = 44100       # sampling rate, Hz, must be integer
duration = 0.1   # in seconds, may be float
f = 440.0        # sine frequency, Hz, may be float
FREQUENCY0 = 500.0 # sine frequency, Hz for 0
FREQUENCY1 = 5000.0 # sine frequency, Hz for 1
def sine_tone(frequency, duration=0.1, sample_rate=SAMPLERATE, channels=1):
	"""
	Generate a sinewave tone, given:
	`frequency` in Hertz (Hz), a measurement of cycles/oscillations per second 
	`duration` in seconds (can be a decimal), default=0.1 seconds
	`sample_rate`, the amount of samples per, default=44100
	`channels`, the amount of audio tracks, such as a left and right channel for stereo playback, default=1 (mono sound)
	"""

	data = [] # An empty array where we will store points on a graph
	
	for i in numpy.arange(sample_rate * duration):
		sample = numpy.sin((2 * PI * frequency * (i / sample_rate)))
		data.append(sample)
	
	default_speaker.play(data/numpy.max(data), samplerate=sample_rate, channels=channels)


# This is necessary!

N = 64 # Number of points
T = 1/64.0 # Spacing between points
# if T is time/distance, 1/T is frequency/wavenumber

x = numpy.linspace(0, 2*np.pi*N*T, N)
# Let's take X as time, so 1/X is frequency!
y1 = numpy.cos(20*x)
y2 = numpy.sin(10*x)
y3 = numpy.sin(5*x)

y = y1 + y2 + y3 # Produces a random signal

fy = fft(y) # Finds the FFT
xf = numpy.linspace(0.0, 1.0/(2.0*T), N/2)

plt.figure(1)
plt.plot(xf, (2.0/N)*numpy.abs(fy[0:N/2])) 
# Only half is valid. The other half is replica!

plt.figure(2)
y4 = ifft(fy) # Gets the inverse FFT
plt.plot(x, y4, 'r')
plt.plot(x, y, 'b')


print("PLAYBACK DEVICES:")
try:
	speakers = sc.all_speakers()
	print(speakers)
	pass
except Exception:
	print("Unable to list playback devices.")
	pass

print("DEFAULT PLAYBACK DEVICE:")
try:
	default_speaker = sc.default_speaker()
	print(default_speaker)
	pass
except Exception:
	print("Unable to find default playback devices.")
	pass

print() # Prints an empty line

print("RECORDING DEVICES:")
try:
	mics = sc.all_microphones()
	print(mics)
	pass
except Exception:
	print("Unable to list recording devices.")
	pass

print("DEFAULT RECORDING DEVICE:")
try:
	default_mic = sc.default_microphone()
	print(default_mic)
	pass
except Exception:
	print("Unable to find default recording device.")
	pass

print()

print("RECORD AND PLAYBACK:")
try:
	print("Recording audio for 3 seconds...")
	data = default_mic.record(samplerate=SAMPLERATE, numframes=(SAMPLERATE*3))
	print("Playing back audio...")
	default_speaker.play(data/numpy.max(data), samplerate=SAMPLERATE)
	pass
except Exception as err:
	print(err)
	if str(err).find("0x80070005") != -1:
		print("ERROR: Windows Permission denied when trying to access the mic.")
	else:
		print("ERROR: Unable to record and play back audio automatically.")
	pass

# You can explicitly set parameters to whatever you want
# However, if you enter parameters in order, you don't need to set them
# if 
	
# else
# 	sine_tone(frequency=FREQUENCY1) int = 1:

# Theres a delay here because of the time it takes to graph the sine wave for 3 seconds
sine_tone(500,0.1)
def dec_to_bin(x):
    return int(bin(x)[2:])
print ()

# There is almost no delay here because the sound is so short that the graph is created quickly
sine_tone(5000,0.1)
