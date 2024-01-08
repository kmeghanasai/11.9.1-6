import matplotlib.pyplot as plt

# Define the function
def x(n):
    return n * (n ** 2 + 5) / 4

# Define the range of n
n_values = list(range(-10, 11))  # from -10 to 10, for example

# Calculate x(n) for each n in the range
x_values = [x(n) for n in n_values]

# Plotting
plt.stem(n_values, x_values)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Plot of x(n) = n(n^2+5)/4')
plt.grid(True)
plt.savefig('plot.pdf')
plt.show()
