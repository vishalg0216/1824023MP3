import numpy as np
import matplotlib.pyplot as plt
import math

def f(t):
    if t >= 1:
        return 0
    return math.exp(-t/(1-t))/(1-t)**2

def simpson(n):
    h = 1/n
    s = f(0) + f(1)

    for i in range(1, n):
        if i % 2 == 0:
            s = s + 2*f(i*h)
        else:
            s = s + 4*f(i*h)

    return s*h/3

def gauss(n):
    x, w = np.polynomial.legendre.leggauss(n)

    result = 0

    for i in range(n):
        t = (x[i] + 1)/2
        result = result + w[i]*f(t)

    return result/2

n_values = [10, 20, 40, 80, 160]

exact = 1

simpson_error = []
gauss_error = []

for n in n_values:

    s = simpson(n)
    g = gauss(n)

    simpson_error.append(abs(s-exact))
    gauss_error.append(abs(g-exact))

    print("N =", n)
    print("Simpson Result =", s)
    print("Gauss Result =", g)
    print()

plt.plot(n_values, simpson_error, 'o-', label="Simpson Rule")
plt.plot(n_values, gauss_error, 's-', label="Gauss Quadrature")

plt.xlabel("Number of Points")
plt.ylabel("Absolute Error")
plt.title("Comparison of Convergence")
plt.yscale("log")
plt.legend()
plt.grid()
plt.show()