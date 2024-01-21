import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 11, 1)
y = ((x + 1)**3 + 5 * (x + 1)) / 4

plt.stem(x, y, basefmt='b-', linefmt='r-', markerfmt='ro', bottom=0)

highlight_indices = [0, 1, 2, 3, 4]
for i in highlight_indices:
    plt.stem(i, y[i], linefmt='b-', markerfmt='bo', basefmt='y-', bottom=0)

plt.xlabel('$n$')
plt.ylabel('$x(n)$')

plt.grid(True)

# Save the plot to a file (e.g., PNG)
plt.savefig('plot.png')
plt.show()

