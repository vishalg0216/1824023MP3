
import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
N = len(x)

X = []

for k in range(N):
    s = 0
    for n in range(N):
        s += x[n] * np.exp(-2j * np.pi * k * n / N)
    X.append(s)

print("DFT:")
for k in range(N):
    print(f"X({k}) = {X[k]:.2f}")

plt.stem(range(N), np.abs(X))
plt.xlabel("Frequency Index")
plt.ylabel("Magnitude")
plt.title("Discrete Fourier Transform")
plt.grid()
plt.show()






















