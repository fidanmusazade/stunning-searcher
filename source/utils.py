import numpy as np

def generate_coordinates():
    coordinates = {0: np.array([500, 9500])}
    for i in range(1, 100):
        if coordinates[i-1][0]==9500:
            coordinates[i] = np.array([500, coordinates[i-1][1]-1000])
        else:
            coordinates[i] = np.array([coordinates[i-1][0]+1000, coordinates[i-1][1]])
    return coordinates