import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# user input and check if valid input
while True:
    try:
        epsilon_D = float(input("Enter a positive value for ε/D (less than 0.05): "))
        if 0 < epsilon_D < 0.05:
            break
        else:
            print("Value must be positive and smaller than 0.05.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

#plug in to given equations
def colebrook(Re, eD):

    #colebrook white equation

    def equation(f):
        return 1 / np.sqrt(f) + 2 * np.log10(eD / 3.7 + 2.51 / (Re * np.sqrt(f)))

    f_initial_guess = 0.001
    f_solution = fsolve(equation, f_initial_guess)[0]
    return f_solution

# reynolds number for each region
Re_laminar = np.linspace(0.1, 2100, 500)  # avoid zero to prevent division error
Re_transition = np.linspace(2100, 4000, 100)  
Re_turbulent = np.logspace(np.log10(4000), np.log10(8e7), 500)

# friction factors for the regions
f_laminar = 16 / Re_laminar  # Laminar flow
f_transition = 16 / Re_transition  # transition region follows laminar trend as in given graph
f_turbulent = np.array([colebrook(Re, epsilon_D) for Re in Re_turbulent])  # Turbulent flow

# Scurves
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xscale('log')
ax.set_yscale('log')
ax.minorticks_on()
ax.set_xlim(1e3, 1e8)
ax.set_ylim(1e-3, 1)

# laminar region graphed with the log scale
plt.loglog(Re_laminar, f_laminar, label="Laminar Flow", linewidth=2)
# transition region
plt.loglog(Re_transition, f_transition, 'k--', label="Transition Region", linewidth=2)
# turbulent region
plt.loglog(Re_turbulent, f_turbulent, label="Turbulent Flow", linewidth=2)

# define graph elements
ax = plt.gca()
plt.title("Friction Factor vs. Reynolds Number", fontsize=14)
plt.xlabel("Re (Reynolds Number)", fontsize=12)
plt.ylabel("f (Friction Factor)", fontsize=12)
ax.legend()
plt.grid(which="both", linestyle="--", linewidth=0.5)
#displays
plt.show()
