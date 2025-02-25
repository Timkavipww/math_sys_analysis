import numpy as np

def function1d(x):
    return (x - 2)**2 + 0.5 * np.sin(2 * x)

def function2d(x):
    return (x[0] - 1)**2 + (x[1] - 2)**2 + np.sin(x[0]) * np.cos(x[1])