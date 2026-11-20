
import numpy as np
import matplotlib.pyplot as plt
import math

# Define interval
L = 1
n = 10
h = L/n

# Create matrix
A = np.zeros((n,n))
B = np.zeros(n)

for i in range(n):
    A[i,i] = -(2+h**2)

    if i > 0:
        A[i,i-1] = 1

    if i < n-1:
        A[i,i+1] = 1

# Boundary condition y(0)=1
B[0] = -1

# Neumann boundary condition y'(1)=0
A[n-1,n-2] = 2

# Solve
y = np.linalg.solve(A,B)

# Add first boundary value
y = np.insert(y,0,1)

x = np.linspace(0,1,n+1)

print("Concentration profile:")
print(y)

# Plot
plt.plot(x,y,'o-')
plt.xlabel("Position (x)")
plt.ylabel("Concentration y(x)")
plt.title("Reaction-Diffusion Equation")
plt.grid()
plt.show()
