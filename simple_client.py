import pyaudio
import socket

chunk = 16000  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 1
sr = 16000  # Record at 44100 samples per second

p = pyaudio.PyAudio()  # Create an interface to PortAudio

print('Recording')

stream = p.open(format=sample_format,
                channels=channels,
                rate=sr,
                frames_per_buffer=chunk,
                input=True)

s = socket.socket()
s.connect(("localhost", 43007))

try:
    while True:
        print("sending data...")
        data = stream.read(chunk)
        s.send(data)
except KeyboardInterrupt:
    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')
