import numpy as np
import matplotlib.pyplot as plt

def fibonacci_search(func, a, b, n=20):
    fib = [0, 1]
    for i in range(2, n+2):
        fib.append(fib[-1] + fib[-2])
    L = b - a
    x1 = a + (fib[n-1] / fib[n+1]) * L
    x2 = a + (fib[n]   / fib[n+1]) * L
    
    f1 = func(x1)
    f2 = func(x2)
    
    for k in range(1, n):
        if f1 > f2:
            a = x1
            x1 = x2
            f1 = f2
            
            x2 = a + (fib[n - k] / fib[n+1 - k]) * (b - a)
            f2 = func(x2)
        else:
            b = x2
            x2 = x1
            f2 = f1
            
            x1 = a + (fib[n - k - 1] / fib[n+1 - k]) * (b - a)
            f1 = func(x1)
    
    x_opt = (a + b) / 2
    f_opt = func(x_opt)
    return x_opt, f_opt