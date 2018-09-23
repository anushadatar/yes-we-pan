#!/usr/bin/env python3
# Quinn Kelley and Anusha Datar
# Principles of Engineering Lab 2
# Serial-based processing test file.

"""
Listens to arduino over serial port to collect data to generate visualization.
Uses functions from utilities file.
"""
from utilities import *
import serial
import time

# Substitue in port number of the arduino. On most UNIX-based systems, the 
# arduino will be at "/dev/ttyACMO" and on most Windows machines it will be
# at a COM port location.
PORT = "/dev/ttyACM0"
# Set the baudrate. This must match baudrate on the arduino program.
BAUD = 9600

# A list of all the cartesian points generated to plot later.
points = []
serialPort = serial.Serial(PORT, BAUD, timeout=10)
# Whether or not the scan has ended, based on servo angles from arduino code.
scanContinue = True

while scanContinue:
    try:
        data = serialPort.readline().decode().split()
        time.sleep(1);
        if len(data)==4:
            # Use the servo bounds from the arduino program. It could be cool
            # to have the arduino send a calibration message during setup
            # and grab those rather than harcoding them. 
            if (int(cartesian_point[1]) == 120 and int(cartesian_point[2]) == 90):
                scanContinue = False
            cartesian_point = spherical_to_cartesian(cartesian_point)
            # Sometimes, because of timing difficulties, the sensor will send
            # out erroneous values, and these numbers will create huge outliers
            # that make the plots difficult to read. Eliminate these.
            valid_point = True
            for element in cartesian:
                # Threshold empirically determined; object under study was
                # much closer than this.
                if abs(element) > 600:
                    valid_point = False
            if valid_point:
                points.append(cartesian_point)
    except:
        # If something gets cut off on a measurement, move on to the next
        # received message, but wait to minimize residual errors.
        time.sleep(.5)
        continue

# Plot points following data collection.
create_three_dimensional_plot(points)
