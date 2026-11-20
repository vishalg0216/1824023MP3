
import numpy as np
import matplotlib.pyplot as plt
import math

# Quantum numbers
l = 1
m = 0

# Angles
theta = np.linspace(0, math.pi, 100)
phi = np.linspace(0, 2*math.pi, 100)

TH, PH = np.meshgrid(theta, phi)

# Associated Legendre polynomial for l=1, m=0
P = np.cos(TH)

# Normalization constant
N = math.sqrt((2*l+1)/(4*math.pi))

# Spherical harmonic
Y = N * P

# Probability density
R = np.abs(Y)**2

# Convert into Cartesian coordinates
X = R * np.sin(TH) * np.cos(PH)
Y1 = R * np.sin(TH) * np.sin(PH)
Z = R * np.cos(TH)

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y1, Z, cmap='viridis')

ax.set_title("Spherical Harmonics Probability Density")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()
