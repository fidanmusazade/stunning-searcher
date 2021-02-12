import numpy as np

def generate_coordinates():
    coordinates = {0: np.array([500, 9500])}
    for i in range(1, 100):
        if coordinates[i-1][0]==9500:
            coordinates[i] = np.array([500, coordinates[i-1][1]-1000])
        else:
            coordinates[i] = np.array([coordinates[i-1][0]+1000, coordinates[i-1][1]])
    return coordinates

def compute_pythagorean_distance(a, b):
    horiz_distance = (np.abs(a%10-b%10)+1)*1000
    vert_distance = (np.abs(a//10-b//10)+1)*1000
    h = np.sqrt(horiz_distance**2+vert_distance**2)
    return h