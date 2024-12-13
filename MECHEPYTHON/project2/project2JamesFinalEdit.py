import numpy as np
import matplotlib.pyplot as plt

# Initialize empty lists for storing input parameters
variable_list = []
name_list = ["L", "k", "cp", "rho", "T0", "T1", "FT", "ht", "hx"]
unit_list = ["m", "W/(m·K)", "J/(kg·K)", "kg/m^3", "K", "K", "s", "s", "m"]
T_exp=np.zeros
T_imp=np.zeros

def input_positive_units(name: str, unit: str) -> float:
#asks for positive input given the conditions passed in returns a float
    while True:
        try:
            value = float(input(f"Enter the {name} in {unit} (positive value): "))
            if value > 0:
                return value
            else:
                print("Error: The value must be positive. Please try again.")
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")

def save_results_to_file(
    filename: str,
    method: str,
    params: list,
    Temp: np.ndarray,
    ht: float,
    hx: float,
    unit_list: list = None
):
#does as named it save the numpy array and the variables inputted to a file

    # opens file for writing
    with open(filename, 'w') as file:
        #title
        file.write(f"Wire temperature - {method} solution\n\n")

        # write the parameters
        param_names = ["L", "k", "cp", "rho", "T0", "T1", "Final Time", "Delta t", "Delta x"]
        for name, value, unit in zip(param_names, params, unit_list):
            file.write(f"{name} = {value} {unit}\n")
        
        file.write("\nTemperature Distribution:\n")

        # write the temperature distribution
        Nt, Nx = Temp.shape
        for n in range(Nt):
            time = n * ht
            file.write(f"t = {time:.2f} s:\n")
            for i in range(Nx):
                position = i * hx
                file.write(f"  x = {position:.2f} m, T = {Temp[n, i]:.2f} K\n")
            file.write("\n")


def explicit_solve(
    L: float,
    k: float,
    cp: float,
    rho: float,
    InitialWireT: float,
    LiquidT: float,
    FinalTime: float,
    ht: float,
    hx: float
) -> tuple[int, int, np.ndarray]:
    #explicit method takes input of the conditions above and returns the tuple given
    lambda_ = (ht / (hx**2)) * (k / (rho * cp))
    if lambda_ >= 0.5:
        raise ValueError("Stability condition not met: λ must be less than 0.5")

    #makes the time and space(length) steps
    Nx = int(L / hx) + 1  # lenght points
    Nt = int(FinalTime / ht) + 1  # time steps

    # initialize temperature array
    T = np.zeros((Nt, Nx))
    T[0, :] = InitialWireT  # Set initial condition
    T[:, 0] = LiquidT  # Boundary condition at x=0
    T[:, -1] = LiquidT  # Boundary condition at x=L

    # iterates through the time at each point to determine the values of temp
    for n in range(0, Nt - 1):
        T[n, 0] = LiquidT #  left boundary
        T[n + 1, -1] = max(T[n, :])  # right boundary
        #iterates through the length points (for loops kind of act as arrays multiplication)
        for i in range(1, Nx - 1):
            T[n + 1, i] = (
                lambda_ * T[n, i - 1] +
                (1 - 2 * lambda_) * T[n, i] +
                lambda_ * T[n, i + 1]
            )

    # plots with all the colors using viridis
    t = np.linspace(0, FinalTime, Nt)
    x = np.linspace(0, L, Nx)
    plt.figure(figsize=(8, 6))
    plt.imshow(T, extent=[x.min(), x.max(), t.min(), t.max()],
               origin='lower', aspect='auto', cmap='viridis', vmin=LiquidT, vmax=np.max(T))
    plt.colorbar(label='T (K)')
    plt.title('Temperature Distribution (Explicit Method)')
    plt.xlabel('x (m)')
    plt.ylabel('t (s)')
    plt.show()
    T_exp=T
    #sets an equal to temp and saves to file
    save_results_to_file(
    "explicit_solution.txt",
    "Explicit",
    variable_list,
    T_exp,
    variable_list[7],  # ht (Delta t)
    variable_list[8],  # hx (Delta x)
    unit_list
)
    return Nt, Nx, T


def implicit_solve(
    L: float,
    k: float,
    cp: float,
    rho: float,
    InitialWireT: float,
    LiquidT: float,
    FinalTime: float,
    ht: float,
    hx: float
):
    #essentially a similar calculation to explicit except approximate the boundary conditions were removed because they werent working :(
    #i couldnt get the function to replicate the graph in the problem description
    alpha = k / (rho * cp) 
    lambda_ = alpha * ht / (hx**2)

   
    Nx = int(L / hx) + 1
    Nt = int(FinalTime / ht) + 1

    # temperature array
    T = np.full((Nt, Nx), InitialWireT)

    # matrix definitions
    A = np.diag((2 * (1 + lambda_)) * np.ones(Nx - 2)) + \
        np.diag(-lambda_ * np.ones(Nx - 3), 1) + \
        np.diag(-lambda_ * np.ones(Nx - 3), -1)

    B = np.diag((2 * (1 - lambda_)) * np.ones(Nx - 2)) + \
        np.diag(lambda_ * np.ones(Nx - 3), 1) + \
        np.diag(lambda_ * np.ones(Nx - 3), -1)
    #iterates through the matrices and multplies them, had to do some weird stuff to get it to the right size of array
    for n in range(1, Nt):
        rhs = B @ T[n - 1, 1:-1]
        T[n, 1:-1] = np.linalg.solve(A, rhs)

    # graphs
    t = np.linspace(0, FinalTime, Nt)
    x = np.linspace(0, L, Nx)
    plt.figure(figsize=(8, 6))
    plt.contourf(x, t, T, levels=100, cmap="viridis")
    cbar = plt.colorbar()
    cbar.set_label("T (K)", rotation=270, labelpad=15)
    plt.title("Temperature Distribution (Implicit Method)", fontsize=14)
    plt.xlabel("x (m)", fontsize=12)
    plt.ylabel("t (s)", fontsize=12)
    plt.tight_layout()
    plt.show()

    T_imp=T

    # Save results
    save_results_to_file(
        "implicit_solution.txt",
        "Implicit",
        variable_list,
        T_imp,
        variable_list[7],  # ht (Delta t)
        variable_list[8],  # hx (Delta x)
        unit_list
    )
    return Nt, Nx, T


for name, unit in zip(name_list, unit_list):
    variable_list.append(input_positive_units(name, unit))

# Solve and visualize using both methods
explicit_solve(*variable_list)
implicit_solve(*variable_list)

print("Solutions saved to 'explicit_solution.txt' and 'implicit_solution.txt'.")

