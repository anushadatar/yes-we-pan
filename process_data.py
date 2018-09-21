#!/usr/bin/env python3
# Quinn Kelley and Anusha Datar
# Principles of Engineering Lab 2
import serial
import time
# Substitute in port number. On unix systems, an easy way to figure
# out the port number is to unplug the device, pipe the contents of
# the /dev directory to a file, plug in the device, pipe the contents
# of the /dev directory to another file, and then take the difference
# between the files. Or just know the port numbers.
port = "/dev/ttyACM0"
# Set the baudrate. MUST match baudrate on the arduino program.
baud = 9600

serialPort = serial.Serial(port, baud, timeout=1)

while True:
    data = serialPort.readline().decode().split()
    time.sleep(1);
    try:
        if len(data)==4:
            # I live to process strings.
            spherical_point = data[1:];
            print(spherical_point)
    except:
        time.sleep(1);
        continue

# TODO Process data string to create a grid based on the format 
# the arduino outputs.
  data = serialPort.readline().decode()
  if len(data) > 0:
    print(data)
# TODO Process data string to create a grid based on the format 
# the arduino outputs.
