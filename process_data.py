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
# A list of all the cartesian points we generate.
points = []
serialPort = serial.Serial(port, baud, timeout=10)

while True:
    try:
        data = serialPort.readline().decode().split()
        time.sleep(1);
        if len(data)==4:
            spherical_point = data[1:]
            print(spherical_point)
            cartesian_point = spherical_to_cartesian(cartesian_point)
            print(cartesian_point)
    except:
        # Ignore weird serial port errors.
        time.sleep(1);
        continue




def spherical_to_cartesian(point):
    """
    Converts spherical points from pan/tilt mechanism
    """
    distance = point[0]
    theta = point[1]
    phi = point[2]
    x = distance*math.sin(math.radians(phi))*math.cos(math.radians(theta))
    y = distance*math.sin(math.radians(phi))*math.sin(math.radians(theta))
    z = distance*math.cos(phi)
    cartesian_point = [x, y, z]
    return cartesian_point

