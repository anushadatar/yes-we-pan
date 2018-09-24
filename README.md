# yes-we-scan
3D Scanner Project for Olin College Principles of Engineering Project 2
## How To Run This Code
This project has two major components: the physical component consisting of an Arduino Uno attached to a time-of-flight sensor and two (2) servo motors and a python-based data processing system. To run them simultaneously, include the assembly and wiring in the attached report and then upload the code in the collection directory to the arduino. 

Then, find the port of the arduino - on most unix-based systems, this will be "/dev/ttyACM0" and on Windows systems it will be COM#. In general, a quick way to check from the terminal is to pipe the results of ls to a file, unplug the device, pipe the results of ls to another file, and then compare the two files. Specify this port in the top of the process_data.py file.
Then, execute the python file on a machine connected to the arduino. This should collect the data and plot the points following a scan.
