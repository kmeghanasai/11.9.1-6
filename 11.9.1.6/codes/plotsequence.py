import numpy as np
import matplotlib.pyplot as plt

def x_n(n):
    return ((n + 1)**3 + 5*(n + 1))/4 * np.heaviside(n, 1)

# Define the range of n values
n_values = np.arange(0, 10, 1)

# Calculate x(n) for each n
x_values = [x_n(n) for n in n_values]

# Plot the signal
plt.stem(n_values, x_values, basefmt='b-', linefmt='r-', markerfmt='ro')
plt.xlabel('$n$')
plt.ylabel('$x(n)$')
plt.grid(True)

# Save the plot to a file (e.g., PNG)
plt.savefig('plot')
plt.show()

