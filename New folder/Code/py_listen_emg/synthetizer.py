import pyaudio
import math

import struct
import ctypes
import binascii
import sys
from time import sleep
import socket
import threading
import Queue

CHUNK = 128
WIDTH = 1
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 2


SOURCE_RATE = 1.0 * RATE / CHUNK
gIndex = 0

gEmgQueue = Queue.Queue()
global gEmg
gEmg = 0.0

my_ip = "0.0.0.0"
my_port = 8899

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((my_ip, my_port))

def UDP_receiver():
    global gEmg
    try:
        print "Listening"
        while True:
            data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
            temg = float(data) 
            #print temg
            gEmgQueue.put(temg)
            gEmg = temg
    except KeyboardInterrupt, errr:
        pass
       


f = 440.0;

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)

print("Chunk interval = ", 1.0 / SOURCE_RATE)

frames = []
buf = ctypes.create_string_buffer(2*CHUNK)
VOLUME = 20000

try:

    ### Start the UDP thread
    
    udp_thread = threading.Thread(target=UDP_receiver)
    #udp_thread.daemon = True
    udp_thread.start()    
    
    while True:            
        ### Assemble a buf[CHUNK] for play-back
        data = []
        for j in xrange(CHUNK):
            t = 1.0 * (j + gIndex * CHUNK)/float(RATE)
            #data.append(VOLUME * math.sin(2.0*math.pi*f*t))
            #t_sound = max(-32767, min(32767, VOLUME * gEmgQueue.get()))
            t_sound = max(-32767, min(32767, VOLUME * gEmg))
            #print t_sound
            data.append(t_sound)
        
        struct.pack_into("="+"h"*CHUNK, buf, 0,*data)
        
        
        ### Write the new buffer data to output
        stream.write(buf, CHUNK)

        sleep(1.0 / SOURCE_RATE)
        gIndex += 1
        
except KeyboardInterrupt, e:
    print "Stopped"
    stream.stop_stream()
    stream.close()

    p.terminate()
    del sock
    sys.exit(0)

