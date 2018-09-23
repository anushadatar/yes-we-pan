#!/usr/bin/env python3
# Quinn Kelley and Anusha Datar
# Principles of Engineering Lab 2
# File-Based Processing Test File

"""
Test file to work on algorithm validation for generating visualizations of 
scanner data collected over serial. Because of issues with serial connection
resets, this file, along with test_dataset.txt, proved to be a useful resource
for prototyping. This program employs the same utilities as the serial-based
program but with file IO.
"""
from utilities import *
cartesian_points_list = []

# Import test dataset and read through it as if it were serial data.
points = open("test_dataset.txt", "r")
point_list = points.readlines()
for point in point_list:
    point.strip('\n')
    point_list = point.split()
    for index in point_list:
	    index.strip()
    # Generate cartesian list to provide to shared plotting function.
    cartesian = spherical_to_cartesian(point_list)
    cartesian_points_list.append(cartesian)

create_three_dimensional_plot(cartesian_points_list)
