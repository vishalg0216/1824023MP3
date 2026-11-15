import numpy as np
import matplotlib.pyplot as plt

a = int(input("Enter real part: "))
b = int(input("Enter imaginary part: "))
n = int(input("Enter value of n: "))

z = complex(a, b)

r = abs(z)
theta = np.angle(z)

print("Polar Roots:")

for k in range(n):
    angle = (theta + 2*np.pi*k)/n
    root = r**(1/n)

    degree = np.degrees(angle)

    print("Root", k+1, "=", round(root, 3),
          "angle", round(degree, 2), "degrees")

    plt.polar(angle, root, 'o')

plt.title("Nth Roots in Polar Form")
plt.show()