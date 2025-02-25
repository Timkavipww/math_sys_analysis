from scipy.optimize import minimize

def optimize_with_gradient(func, x0):
    res = minimize(func, x0, method='BFGS')
    return res.x[0], res.fun