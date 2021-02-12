import numpy as np

def compute_pythagorean_distance(a, b):
    horiz_distance = (np.abs(a%10-b%10)+1)*1000
    vert_distance = (np.abs(a//10-b//10)+1)*1000
    h = np.sqrt(horiz_distance**2+vert_distance**2)
    return h