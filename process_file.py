#!/usr/bin/env python3
# Quinn Kelley and Anusha Datar
# Principles of Engineering Lab 2

import math
import matplotlib.pyplot as plt
from  mpl_toolkits.mplot3d import Axes3D
import serial
import time

points = []

def spherical_to_cartesian(point):
    """
    Converts spherical points from pan/tilt mechanism
    """
    distance = int(point[0])
    theta = int(point[1])
    phi = int(point[2])
    x = distance*math.sin(math.radians(phi))*math.cos(math.radians(theta))
    y = distance*math.sin(math.radians(phi))*math.sin(math.radians(theta))
    z = -distance*math.cos(phi)
    cartesian_point = [x, y, z]
    return cartesian_point

def create_three_dimensional_plot(points):
    """
    Creates three dimensional visualization of data collected from scan.
    points : List of lists where each sub-list is a 
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x_values = []
    y_values = []
    z_values = []
    for element in points:
        x_values.append(element[0])
        y_values.append(element[1])
        z_values.append(element[2])
    ax.scatter(xs=x_values, ys=y_values, zs=z_values)
    plt.show()

cartesian_points_list = []
spherical_points_list = []

points = open("test_dataset.txt", "r")
point_list = points.readlines()
for point in point_list:
    point.strip('\n')
    point_list = point.split()
    for index in point_list:
	    index.strip()
    cartesian = spherical_to_cartesian(point_list)
    cartesian_points_list.append(cartesian)
 
create_three_dimensional_plot(cartesian_points_list)
