import numpy as np
import matplotlib.pyplot as plt

N = 256
L = 8

x = np.linspace(-L, L, N, endpoint=False)
f = np.exp(-x**2)

dx = x[1] - x[0]

F = np.fft.fft(f)
F = np.fft.fftshift(F)

freq = np.fft.fftshift(np.fft.fftfreq(N, d=dx))

F = F * dx

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(x, f)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Original Function")
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(freq, np.abs(F))
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.title("Fast Fourier Transform")
plt.grid()

plt.tight_layout()
plt.show()

print("FFT calculated successfully.")