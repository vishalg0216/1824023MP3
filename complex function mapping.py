import numpy as np
import matplotlib.pyplot as plt

n = int(input("Enter number of points: "))
a = float(input("Enter range: "))

x = np.linspace(-a, a, n)
y = np.linspace(-a, a, n)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)

for i in x:
    z = i + 1j*y
    plt.plot(z.real, z.imag)

for i in y:
    z = x + 1j*i
    plt.plot(z.real, z.imag)

plt.title("Z Plane")
plt.xlabel("Real Part")
plt.ylabel("Imaginary Part")
plt.grid()

plt.subplot(1, 2, 2)

for i in x:
    z = i + 1j*y
    w = z**2
    plt.plot(w.real, w.imag)

for i in y:
    z = x + 1j*i
    w = z**2
    plt.plot(w.real, w.imag)

plt.title("W Plane (w = z²)")
plt.xlabel("Real Part")
plt.ylabel("Imaginary Part")
plt.grid()

plt.tight_layout()
plt.show()








