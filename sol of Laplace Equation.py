
import numpy as np
import matplotlib.pyplot as plt
import math

# Grid size
n = 20

# Create temperature matrix
T = np.zeros((n,n))

# Boundary conditions
T[-1,:] = 100
T[0,:] = 0
T[:,0] = 0
T[:,-1] = 0

# Iteration
for k in range(500):

    for i in range(1,n-1):
        for j in range(1,n-1):

            T[i,j] = 0.25 * (
                T[i+1,j] +
                T[i-1,j] +
                T[i,j+1] +
                T[i,j-1]
            )

# Print result
print("Temperature distribution:")
print(T)

# Plot
plt.imshow(T, cmap='hot', origin='lower')
plt.colorbar(label="Temperature")
plt.xlabel("X position")
plt.ylabel("Y position")
plt.title("Solution of Laplace Equation")
plt.show()
