from scipy.optimize import golden

def optimize_with_golden(func, brack):
    xmin=golden(func, brack=brack)
    return xmin, func(xmin)
