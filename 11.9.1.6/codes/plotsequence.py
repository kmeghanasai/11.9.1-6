import numpy as np
import matplotlib.pyplot as plt

def x_n(n):
    return ((n + 1)**3 + 5*(n + 1))/4 * np.heaviside(n, 1)

# Define the range of n values
n_values = np.arange(0, 10, 1)

# Calculate x(n) for each n
x_values = [x_n(n) for n in n_values]

# Plot all stems
plt.stem(n_values, x_values, basefmt='b-', linefmt='r-', markerfmt='ro',  bottom=0)

# Highlight stems for n=1,2,3,4,5 with yellow color
highlight_indices = [0,1, 2, 3, 4]
for i in highlight_indices:
    plt.stem(i, x_n(i), linefmt='b-', markerfmt='bo', basefmt='y-',  bottom=0)

plt.xlabel('$n$')
plt.ylabel('$x(n)$')
plt.grid(True)

# Save the plot to a file (e.g., PNG)
plt.savefig('plot.png')
plt.show()

