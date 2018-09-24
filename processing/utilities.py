# Utilities file.
"""
Because of shared functions with File IO and serial-based communication, this
file proved to be a valuable resource to maintain a consistent architecture 
throughout test phases.
"""
import math                                                                     
import matplotlib.pyplot as plt                                                 
from  mpl_toolkits.mplot3d import Axes3D                                        
import serial                                                                   
import time                                                                     
                                                                                
                                                                                
def spherical_to_cartesian(point):                                              
    """                                                                         
    Converts spherical point from pan/tilt mechanism into cartesian points.        
    Note that it assumes a 0 to 120 servo-angle based cone for scanning and 
    employs an empiricially determined calibration curve to find the radial
    distance measured by the sensor.

    point : A list as follows:
            [DISTANCE_MEASUREMENT, LATITUDE_ANGLE, LONGITUDINAL_ANGLE]
    returns : A list with the cartesian point equivalent of the input:
              [X, Y, Z]
    """                                                                         
    distance = 8.6*int(point[0]) + 80
    # Our current angles are from 60 degrees to 120 degrees. Shift those 
    # to be between -60 and 60 degrees.
    theta = int(point[1]) - 120
    # Subtract 120 + 90 from this one to account for reversal of azimuthal 
    # direction because of existing sensor orientation.
    phi = int(point[2]) - 120
    # Spherical coordinate formula. 
    x = distance*math.sin(math.radians(phi + 180))*math.cos(math.radians(theta))      
    y = -distance*math.sin(math.radians(phi + 180))*math.sin(math.radians(theta))
    z = distance*math.cos(phi)                                                 
    cartesian_point = [x, y, z]                                                 
    return cartesian_point                                                      
                                                                                
def create_three_dimensional_plot(points):                                      
    """                                                                         
    Creates three dimensional visualization of data collected from scan.        
    
    points : List of lists where each sub-list is a cartesian point 
             [X, Y, Z]                     
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
    # Use the matplotlib 3D plot feature.
    ax.scatter(xs=x_values, ys=y_values, zs=z_values)                  
    ax.set_title("3D Scan Surface Plot.")                                       
    ax.set_xlabel("X (mm)")                                                     
    ax.set_ylabel("Y (mm)")                                                     
    ax.set_zlabel("Z (mm)")     
    plt.show()

def create_three_dimensional_surface(points):
    """                                                                         
    Creates three dimensional visualization of data collected from scan.        
                                                                                
    points : List of lists where each sub-list is a cartesian point             
             [X, Y, Z]                                       
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
    # Use the matplotlib 3D plot feature.
    ax.plot_trisurf(x_values, y_values, z_values)
    ax.set_title("3D Scan Surface Plot.")
    ax.set_xlabel("X (mm)")
    ax.set_ylabel("Y (mm)")
    ax.set_zlabel("Z (mm)")
    plt.show()
