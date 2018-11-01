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

while True:

    # binary data
    data = stream.read(CHUNK, exception_on_overflow=False)

    # convert data to integers, make np array, then offset it by 127
    data_int = struct.unpack(str(2 * CHUNK) + 'B', data)

    # create np array and offset by 128
    data_np = np.array(data_int, dtype='b') + 128

    # compute FFT and update line
    yf = fft(data_int)
    line_fft.set_ydata(
        (np.abs(yf[0:CHUNK]) / (128 * CHUNK))[GRAPH_X_MIN:int(CHUNK/2)])

    try:
        fig.canvas.draw()
        fig.canvas.flush_events()
        plt.pause(0.0001)
    except Exception:
        exit(0)
