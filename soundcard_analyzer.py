import soundcard as sc
import numpy as np
from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import flipper
import time

SAMPLERATE = 44100
CHUNKSIZE = 1024 * 2
HALF_OF_CHUNKSIZE = int(CHUNKSIZE / 2)
GRAPH_X_MIN = 800  # Cut off everything before point in the plot
CHANNELS = 1

# Get default speaker
default_speaker = sc.default_speaker()
print(default_speaker)

# Get default microphone
default_mic = sc.default_microphone()
print(default_mic)

# Create a figure to plot on
fig, ax = plt.subplots()

# Generate X points to plot the Y points with, from 0 to 20,000
xf = np.linspace(0, SAMPLERATE, CHUNKSIZE)[GRAPH_X_MIN:HALF_OF_CHUNKSIZE]


def updatePlot(i):
    """Plot the data coming from the microphone continously"""
    # with default_mic.recorder(samplerate=SAMPLERATE) as mic, default_speaker.player(samplerate=SAMPLERATE) as sp:
    data = default_mic.record(numframes=CHUNKSIZE, samplerate=SAMPLERATE)
    # sp.play(data) # Uncomment to hear chunks of audio being played as they're recorded
    plt.clf()
    yf = np.abs(fft(flipper.flattenData(data))[GRAPH_X_MIN:HALF_OF_CHUNKSIZE])
    plt.plot(xf, yf, 'orange')


# Update the figure (the line) via the updatePlot() function
a = anim.FuncAnimation(fig, updatePlot, repeat=False)
plt.show()
