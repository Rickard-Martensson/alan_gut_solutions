import numpy as np
from scipy.integrate import quad


# Define the function to integrate
def integrand(t):
    if t == 0:
        return np.sqrt(1)  # limit of sin(t)/t as t -> 0 is 1
    else:
        return np.sqrt(np.sin(t) / t)


# Compute the integral from 0.001 to pi
result, error = quad(integrand, 0.001, np.pi)

print("Integral result:", result)
print("Estimated error:", error)
