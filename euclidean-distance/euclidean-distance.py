import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    X = np.array(x)
    Y = np.array(y)
    n = len(x)
    if X.shape != Y.shape:
        raise ValueError("Vectors must have the same shape")
    Z = 0
    for i in range(n):
        Z += ((X[i] - Y[i])**2)
        euclidean_distance = (Z)**(1/2)
    
    return (euclidean_distance)
