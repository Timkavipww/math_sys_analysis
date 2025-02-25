import numpy as np
import matplotlib.pyplot as plt
from dichotomy_search import dichotomy_search
from golden_method import *
from functions import *
from optimize_with_gradient import *
from scipy.optimize import minimize
from fibbonaaci import fibonacci_search
from variables import *

def main():
    
    #FOR GOLDEN
    
    xmin= optimize_with_golden(function1d, brack=bracket)[0]
    ymin = optimize_with_golden(function1d, brack=bracket)[1]
    
    print(f"xmin = {xmin:.6f}")
    print(f"g(x) = {ymin:.6f}")

    x_vals = np.linspace(0, 4, 400)
    y_vals = function1d(x_vals)
    
    
    plt.plot(x_vals, y_vals, label=r'$g(x) = (x-2)^2 + 0.5\sin(2x)$')
    plt.scatter(xmin, ymin, color='red', zorder=3,
                label=f"Минимум: x={xmin:.4f}, g(x)={ymin:.4f}")
    plt.legend()
    plt.grid()
    plt.show()
    
    
     #FOR GRADIENT
    xmin = optimize_with_gradient(function1d, x0gradient)[0]
    fmin = optimize_with_gradient(function1d, x0gradient)[1]
    
    print(f"Метод градиента: Минимум найден: x = {xmin:.6f}, f(x) = {fmin:.6f}")
    
    x_vals = np.linspace(0, 4, 400)
    y_vals = function1d(x_vals)

    plt.plot(x_vals, y_vals, label=r'$f(x)=(x-2)^2+0.5\sin(2x)$')
    plt.scatter(xmin, fmin, color='red', zorder=3,
                label=f"xmin ={xmin:.4f}, f(x)={fmin:.4f}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Оптимизация методом градиента (BFGS)")
    plt.legend()
    plt.grid()
    plt.show()
    
    

    # Оптимизация методом градиента (BFGS)
    res = minimize(function2d, x0gradient2d, method='BFGS')
    xmin = res.x
    fmin = res.fun

    print("Минимум найден: x = {:.6f}, y = {:.6f}, f(x,y) = {:.6f}".format(xmin[0], xmin[1], fmin))

    x = np.linspace(-2, 4, 400)
    y = np.linspace(-2, 6, 400)
    X, Y = np.meshgrid(x, y)
    Z = function2d([X, Y])

    plt.figure(figsize=(8, 6))
    CS = plt.contour(X, Y, Z, levels=30, cmap='viridis')
    plt.clabel(CS, inline=True, fontsize=8)
    
    plt.scatter(xmin[0], xmin[1], color='red', marker='x', s=100,
                label=f"Минимум: ({xmin[0]:.2f}, {xmin[1]:.2f})")
    plt.title("Оптимизация двумерной функции методом градиента (BFGS)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid()
    plt.show()
    
    
    x_opt = dichotomy_search(function1d, a, b, tol=1e-5, delta=1e-6)[0]
    f_opt = dichotomy_search(function1d, a, b, tol=1e-5, delta=1e-6)[1]
    
    print("Метод дихотомии: минимум найден: x = {:.6f}, f(x) = {:.6f}".format(x_opt, f_opt))
    
    x_vals = np.linspace(a, b, 400)
    y_vals = function1d(x_vals)
    
    plt.plot(x_vals, y_vals, label=r'$f(x)=(x-2)^2+0.5\sin(2x)$')
    plt.scatter(x_opt, f_opt, color='red', zorder=3,
                label=f"Минимум: x={x_opt:.4f}, f(x)={f_opt:.4f}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Оптимизация методом дихотомии")
    plt.legend()
    plt.grid()
    plt.show()

    

    x_opt, f_opt = fibonacci_search(function1d, a, b, n=20)
    print(f"Метод Фибоначчи: минимум найден: x = {x_opt:.6f}, f(x) = {f_opt:.6f}")
    
    x_vals = np.linspace(a, b, 400)
    y_vals = [function1d(x) for x in x_vals]

    plt.plot(x_vals, y_vals, label=r'$f(x)=(x-2)^2+0.5\sin(2x)$')
    plt.scatter(x_opt, f_opt, color='red', zorder=3,
                label=f"Минимум: x={x_opt:.4f}, f(x)={f_opt:.4f}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Оптимизация методом Фибоначчи")
    plt.legend()
    plt.grid()
    plt.show()
if __name__ == "__main__":
    main()
