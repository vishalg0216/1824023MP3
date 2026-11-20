
import numpy as np
import matplotlib.pyplot as plt
import math

# Length of bar
L = 10
n = 10
h = L/n

# Boundary temperatures
T1 = 100
T2 = 50

# Matrix and RHS
A = np.zeros((n-1, n-1))
B = np.zeros(n-1)

for i in range(n-1):
    A[i,i] = -2

    if i > 0:
        A[i,i-1] = 1

    if i < n-2:
        A[i,i+1] = 1

# Boundary conditions
B[0] = -T1
B[n-2] = -T2

# Solve equations
T = np.linalg.solve(A, B)

# Add boundary temperatures
T = np.insert(T, 0, T1)
T = np.append(T, T2)

x = np.linspace(0, L, n+1)

print("Temperature:", T)

# Plot
plt.plot(x, T, 'o-')
plt.xlabel("Length of bar")
plt.ylabel("Temperature")
plt.title("Equilibrium Temperature of Bar")
plt.grid()
plt.show()
