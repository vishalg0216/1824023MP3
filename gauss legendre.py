import numpy as np
import matplotlib.pyplot as plt
import math

L = float(input("Enter displacement (m): "))
n = int(input("Enter number of Gauss points: "))

x, w = np.polynomial.legendre.leggauss(n)

a = 0
b = L

X = (b-a)*x/2 + (a+b)/2

F = 3*X**2 + 2*X + 5

W = 0

for i in range(n):
    W += w[i]*F[i]

W = W*(b-a)/2

print("Work Done =", W, "J")

xx = np.linspace(0, L, 100)
ff = 3*xx**2 + 2*xx + 5

plt.plot(xx, ff)
plt.fill_between(xx, ff, alpha=0.3)
plt.xlabel("Displacement (m)")
plt.ylabel("Force (N)")
plt.title("Work Done by Variable Force")
plt.grid()
plt.show()


