import numpy as np
import matplotlib.pyplot as plt
#written by james w morton 

#essentially this is just a related rates problem in python hooray!

def spherical_volume_derivative(h, R):
    # Derivative of volume with respect to height
    return np.pi * h * (2 * R - h)

def simulate_tank_drainage(R, h0, d, k, g=32.2, dt=0.1):
    # Outlet cross-sectional area
    A = np.pi * (d / 2) ** 2  # ft^2

    # Time and height initialization
    t = 0
    h = h0

    # Results storage
    times = [t]
    heights = [h]

    while h > 0:
        dVdh = spherical_volume_derivative(h, R)
        Q = k * A * np.sqrt(2 * g * h)
        dhdt = -Q / dVdh
        h += dhdt * dt  # Update height
        t += dt  # Update time

        # Store results
        times.append(t)
        heights.append(max(h, 0))
    #returns the respective arrays
    return np.array(times), np.array(heights)
#saves to file
def save_results_to_file(times, heights, filename="tank_drainage.txt"):
    data = np.column_stack((times, heights))
    np.savetxt(filename, data, header="Time (s)\tHeight (ft)", fmt="%.4f")

def plot_results(times, heights):
    plt.figure(figsize=(10, 6))
    plt.plot(times, heights, label="Liquid Height", color="b")
    #abscissa is a real wacky word to say x coordinates
    plt.xlabel("Time (s)")
    plt.ylabel("Height (ft)")
    plt.title("Height of Liquid in Tank Over Time")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Ask for user input
    R = float(input("Enter the tank radius (ft): "))
    h0 = float(input("Enter the initial liquid height (ft): "))
    d = float(input("Enter the outlet diameter (ft): "))
    k = float(input("Enter the constant k: "))

    # Simulate
    times, heights = simulate_tank_drainage(R, h0, d, k)

    # Save results
    save_results_to_file(times, heights)

    # Plot results
    plot_results(times, heights)

