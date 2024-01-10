import matplotlib.pyplot as plt

def sequence(n):
    return ((n + 1) * ((n + 1)**2 + 5)) / 4

n_values = list(range(0, 21))  # Define the range of n values (0 to 20 in this case)
x_values = [sequence(n) for n in n_values]  # Calculate x[n] values

plt.stem(n_values, x_values)  # Plotting the stem plot
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Plot of x[n] = ((n+1)((n+1)^2+5))/4')
plt.grid(True)

# Save the plot as a PNG file
plt.savefig('x_n_plot.png')

plt.show()

