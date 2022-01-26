# Read Sample.txt file and send line by line
# Analyzer program

import serial
import time

comport = "/dev/ttyS0"
bdrate = 9600
ser1 = serial.Serial(port=comport, baudrate=bdrate, timeout=2)

while True:
    file1 = open('sample.txt', 'rb')
    Lines = file1.readlines()
    file1.close()
    for line in Lines:
        print(line)
        ser1.write(line)
        time.sleep(0.03)
    time.sleep(2)
