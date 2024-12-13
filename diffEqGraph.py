import numpy as np
import matplotlib.pyplot as plt

# Define the function y(x) for a given initial condition C
def y(x, C):
    return C * np.exp(-3 * x**3)

# Generate a wider range of x values
x = np.linspace(-.7, .7, 400)

# Different initial conditions
initial_conditions = [0, 1, 2, 4, 6, -1, -2, -4, -6, 10, -10]

# Plot solutions for different initial conditions
plt.figure(figsize=(10, 6))
for C in initial_conditions:
    y_values = y(x, C)
    plt.plot(x, y_values, label=f'C = {C}')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Solutions of the Differential Equation for Various Initial Conditions')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)  # Add x-axis
plt.axvline(0, color='black', linewidth=0.5)  # Add y-axis
plt.legend()
plt.show()
