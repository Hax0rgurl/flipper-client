import pyaudio
import os
import struct
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import time
import flipper

# constants
CHUNK = 1024 * 2  # samples per frame
FORMAT = pyaudio.paInt16  # audio format (bytes per sample?)
CHANNELS = 1  # single channel for microphone
RATE = 44100  # samples per second
GRAPH_X_MIN = 800
PLOT_OR_NOT = False

BIT_INTERVAL_TIME = 0.15
BETWEEN_BIT_DELAY = 0.15
BETWEEN_BYTE_WAIT_TIME = 0.0

OFFSET = 25
THRESHOLD = 0.17

FQ_START = 17800
FQ_STEP = 150

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

FREQS = [
    FQ_0,
    FQ_1,
    FQ_2,
    FQ_3,
    FQ_4,
    FQ_5,
    FQ_6,
    FQ_7,
    FQ_8,
    FQ_9,
    FQ_A,
    FQ_B,
    FQ_C,
    FQ_D,
    FQ_E,
    FQ_F,
]


def bits2string(b=None):
    """Function to convert binary to string"""
    # result = ''.join([chr(int(x, 2)) for x in b])
    result = chr(int(b, 2))
    return result


# pyaudio class instance
p = pyaudio.PyAudio()

# stream object to get data from microphone
stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK,
)

# variable for plotting
xf = np.linspace(0, RATE, CHUNK)[GRAPH_X_MIN : int(CHUNK / 2)]  # frequencies (spectrum)

if PLOT_OR_NOT:
    # create matplotlib figure and axes
    fig, ax2 = plt.subplots()

    # create semilogx line for spectrum
    line_fft, = ax2.plot(
        xf, np.random.rand(CHUNK)[GRAPH_X_MIN : int(CHUNK / 2)], "-", lw=2
    )

    # format waveform axes
    ax2.set_title("Fourier Transform of Microphone Data - PyAudio")
    ax2.set_xlabel("Frequency")
    ax2.set_ylabel("Prevalence of Frequency")

    plt.show(block=False)

timerStart = time.time()

output = []
received = ""


def findFreq(pData):
    global timerStart  # To allow us to use timerStart within this function's scope
    global received
    global output
 
    # recieved: 

    if len(received) == 2:
        # print(": " + bits2string(received))
        print(": " + chr(int(received,16)))
        timerStart = time.time()  # + BETWEEN_BIT_WAIT_TIME

        # output <- recieved 
        output.append(received) # output: ["1e"]
        received = ""

    # if enough time passes and no sound plays, run output[] and empty it
    elif np.abs(timerStart - time.time()) > 2 and len(output) > 0:
        print()
        # os.system()
        pass

    elif np.abs(timerStart - time.time()) >= BIT_INTERVAL_TIME:
        for x, y in zip(xf, pData):
            if y >= THRESHOLD:
                timerStart = time.time()

                if np.abs(FQ_0 - x) <= OFFSET:
                    print("0", end="", flush=True)
                    received += "0"
                elif np.abs(FQ_1 - x) <= OFFSET:
                    print("1", end="", flush=True)
                    received += "1"
                elif np.abs(FQ_2 - x) <= OFFSET:
                    print("2", end="", flush=True)
                    received += "2"
                elif np.abs(FQ_3 - x) <= OFFSET:
                    print("3", end="", flush=True)
                    received += "3"
                elif np.abs(FQ_4 - x) <= OFFSET:
                    print("4", end="", flush=True)
                    received += "4"
                elif np.abs(FQ_5 - x) <= OFFSET:
                    print("5", end="", flush=True)
                    received += "5"
                elif np.abs(FQ_6 - x) <= OFFSET:
                    print("6", end="", flush=True)
                    received += "6"
                elif np.abs(FQ_7 - x) <= OFFSET:
                    print("7", end="", flush=True)
                    received += "7"
                elif np.abs(FQ_8 - x) <= OFFSET:
                    print("8", end="", flush=True)
                    received += "8"
                elif np.abs(FQ_9 - x) <= OFFSET:
                    print("9", end="", flush=True)
                    received += "9"
                elif np.abs(FQ_A - x) <= OFFSET:
                    print("A", end="", flush=True)
                    received += "A"
                elif np.abs(FQ_B - x) <= OFFSET:
                    print("B", end="", flush=True)
                    received += "B"
                elif np.abs(FQ_C - x) <= OFFSET:
                    print("C", end="", flush=True)
                    received += "C"
                elif np.abs(FQ_D - x) <= OFFSET:
                    print("D", end="", flush=True)
                    received += "D"
                elif np.abs(FQ_E - x) <= OFFSET:
                    print("E", end="", flush=True)
                    received += "E"
                elif np.abs(FQ_F - x) <= OFFSET:
                    print("F", end="", flush=True)
                    received += "F"

                if PLOT_OR_NOT:
                    ax2.annotate("(%s -> %s)" % (int(x), y), xy=(x, y), textcoords="data")
                break


while True:

    # binary data
    data = stream.read(CHUNK, exception_on_overflow=False)

    # convert data to integers, make np array, then offset it by 127
    data_int = struct.unpack(str(2 * CHUNK) + "B", data)

    # create np array and offset by 128
    data_np = np.array(data_int, dtype="b") + 128
    # compute FFT and update line
    yf = fft(data_int)
    yf = np.abs(yf[0:CHUNK]) / (128 * CHUNK)

    findFreq(yf[GRAPH_X_MIN : int(CHUNK / 2)])

    if PLOT_OR_NOT:
        pass
        line_fft.set_ydata(yf[GRAPH_X_MIN : int(CHUNK / 2)])

        try:
            fig.canvas.draw()
            fig.canvas.flush_events()
            plt.pause(0.0001)
        except Exception:
            exit(0)


def hexToASCII(parameter):
    ascii = bytes.fromhex(parameter).decode("ascii")
    test = bin(parameter)
    leascii = ascii(test)
    print(leascii)
    # hex()
    return ascii

