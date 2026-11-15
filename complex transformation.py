import numpy as np
import matplotlib.pyplot as plt

a = int(input("Enter real part: "))
b = int(input("Enter imaginary part: "))

z = complex(a, b)

tx = int(input("Enter translation in real direction: "))
ty = int(input("Enter translation in imaginary direction: "))

s = int(input("Enter scaling factor: "))

angle = float(input("Enter rotation angle in degrees: "))

translation = z + complex(tx, ty)
scaling = z * s

rotation = z * np.exp(1j * np.radians(angle))

reflection = np.conjugate(z)

print("Original:", z)
print("Translation:", translation)
print("Scaling:", scaling)
print("Rotation:", rotation)
print("Reflection:", reflection)

points = [z, translation, scaling, rotation, reflection]
labels = ["Original", "Translation", "Scaling",
          "Rotation", "Reflection"]

for p, label in zip(points, labels):
    plt.scatter(p.real, p.imag, label=label)

plt.xlabel("Real Part")
plt.ylabel("Imaginary Part")
plt.title("2-D Vector Transformations")
plt.legend()
plt.grid()
plt.axis("equal")
plt.show()



