import numpy as np
import matplotlib.pyplot as plt

a = int(input("Enter real part: "))
b = int(input("Enter imaginary part: "))
n = int(input("Enter value of n: "))

z = complex(a, b)

r = abs(z)
theta = np.angle(z)

print("Cartesian Roots:")

for k in range(n):
    angle = (theta + 2*np.pi*k)/n
    root = r**(1/n) * (np.cos(angle) + 1j*np.sin(angle))

    print("Root", k+1, "=", round(root.real, 3),
          "+", round(root.imag, 3), "i")

    plt.scatter(root.real, root.imag)

plt.xlabel("Real Part")
plt.ylabel("Imaginary Part")
plt.title("Nth Roots in Cartesian Form")
plt.grid()
plt.axis("equal")
plt.show()


















