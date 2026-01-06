# Import NumPy for numerical operations
import numpy as np

# Import the 'quad' function from SciPy for numerical integration
from scipy.integrate import quad

# Print a simple greeting to verify Python is running correctly
print("Hello, EAE 130!")

# Personal introduction 
print("My name is <Kuval Bora> and I am using <Windows>.")

# ---------------------------------------------------------------------
# NUMPY TEST
# ---------------------------------------------------------------------
# Create two vectors using NumPy arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Compute the dot product of vectors a and b
dot_product = np.dot(a, b)

# Print the result of the NumPy operation (expected output: 32)
print("NumPy dot product test:", dot_product)

# ---------------------------------------------------------------------
# SCIPY TEST
# ---------------------------------------------------------------------
# Define a function for SciPy to integrate.
# Here, we integrate sin(x) over the interval [0, pi].
def integrand(x):
    return np.sin(x)

# Perform the numerical integration using quad().
# 'result' is the integral value, 'error' is an estimate of numerical error.
result, error = quad(integrand, 0, np.pi)

# Print the numerical integration result (expected ≈ 2.0)
print("SciPy integration test (integral of sin(x) from 0 to pi):", result)