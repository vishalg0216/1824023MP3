
import numpy as np
import matplotlib.pyplot as plt
import math

# Potential well parameters
V0 = 20
a = 1

z0 = a * math.sqrt(V0)

# Bisection method
def bisect(f, low, high):
    for i in range(100):
        mid = (low + high)/2

        if f(low)*f(mid) < 0:
            high = mid
        else:
            low = mid

    return (low + high)/2

# Store energy values
energies = []
states = []

# Find even and odd energy states
for n in range(int(z0/math.pi)+2):

    # Even state
    low = n*math.pi + 0.00001
    high = min(n*math.pi + math.pi/2 - 0.00001,
               z0 - 0.00001)

    if low < high:
        def f(z):
            return z*math.tan(z) - math.sqrt(z0**2-z**2)

        if f(low)*f(high) < 0:
            z = bisect(f, low, high)
            energies.append(-V0 + (z/a)**2)
            states.append((z, "even"))

    # Odd state
    low = n*math.pi + math.pi/2 + 0.00001
    high = min((n+1)*math.pi - 0.00001,
               z0 - 0.00001)

    if low < high:
        def f(z):
            return -z/math.tan(z) - math.sqrt(z0**2-z**2)

        if f(low)*f(high) < 0:
            z = bisect(f, low, high)
            energies.append(-V0 + (z/a)**2)
            states.append((z, "odd"))

# Position
x = np.linspace(-5, 5, 1000)

# Plot wavefunctions
for E, state in zip(energies, states):

    z, parity = state

    k = z/a
    alpha = math.sqrt(V0-k**2)

    psi = np.zeros(len(x))

    for i in range(len(x)):

        if abs(x[i]) <= a:

            if parity == "even":
                psi[i] = math.cos(k*x[i])
            else:
                psi[i] = math.sin(k*x[i])

        else:

            if parity == "even":
                psi[i] = math.cos(k*a)*math.exp(
                    -alpha*(abs(x[i])-a))

            else:
                psi[i] = np.sign(x[i])*math.sin(k*a)*math.exp(
                    -alpha*(abs(x[i])-a))

    # Normalize wavefunction
    norm = math.sqrt(np.trapz(psi**2, x))
    psi = psi/norm

    plt.plot(x, psi, label="E = "+str(round(E,3)))

    print("Energy eigenvalue =", round(E,3))

plt.xlabel("Position (x)")
plt.ylabel("Wavefunction")
plt.title("Finite Potential Well")
plt.legend()
plt.grid()
plt.show()
