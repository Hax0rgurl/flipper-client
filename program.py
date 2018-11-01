import soundcard as sc
import numpy
import os
import flipper as flpr
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
PI = numpy.pi  # 3.14159... (the angle of a circle)
SAMPLERATE = 44100  # A samplerate supported by nearly all devices
VOLUME = 0.5     # range [0.0, 1.0]
FS = 44100       # sampling rate, Hz, must be integer
duration = 0.1   # in seconds, may be float
f = 440.0        # sine frequency, Hz, may be float
FREQUENCY0 = 500.0  # sine frequency, Hz for 0
FREQUENCY1 = 5000.0  # sine frequency, Hz for 1

FREQ_0 = 19

sine_tone = FREQUENCY0
sine_tone = FREQUENCY1
N = 64  # Number of points
T = 1/64.0  # Spacing between points
# if T is time/distance, 1/T is frequency/wavenumber

# x = numpy.linspace(0, 2*np.pi*N*T, N)
# Let's take X as time, so 1/X is frequency!
# y1 = numpy.cos(20*x)
# y2 = numpy.sin(10*x)
# y3 = numpy.sin(5*x)

# y = y1 + y2 + y3 # Produces a random signal

# fy = fft(y) # Finds the FFT
# xf = numpy.linspace(0.0, 1.0/(2.0*T), N/2)

# plt.figure(1)
# plt.plot(xf, (2.0/N)*numpy.abs(fy[0:N/2]))
# # Only half is valid. The other half is replica!

# plt.figure(2)
# y4 = ifft(fy) # Gets the inverse FFT
# plt.plot(x, y4, 'r')
# plt.plot(x, y, 'b')


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

print()  # Prints an empty line

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


# checks if frequency is between 9900 and 10000
index = 9900
while index < 10000:
    index = index + 1
    if dataFFT[index] >= 10:
        print("0")
        break

# checks if frequency is between 17900 and 18000
index = 17900
while index < 18000:
    index = index + 1
    if dataFFT[index] >= 10:
        print(dataFFT[index])
        print("1")
        break


# sine_tone(500,0.1)
def dec_to_bin(x):
    return int(bin(x)[2:])
