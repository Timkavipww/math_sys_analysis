import numpy as np
import matplotlib.pyplot as plt

def dichotomy_search(func, a, b, tol=1e-5, delta=1e-6):
    while (b - a) > tol:
        mid = (a + b) / 2.0
        x1 = mid - delta
        x2 = mid + delta
        
        if func(x1) < func(x2):
            b = x2
        else:
            a = x1
            
    x_opt = (a + b) / 2.0
    return x_opt, func(x_opt)
