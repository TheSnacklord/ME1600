import numpy as np
import math
import matplotlib.pyplot as plt

n = 0
#User chooses option 1 in the given statement
def max_stable_load():
    #While true loops to require a positive number, continue and break: to break out of the loop when a positive number is given, everything is named accurate to what it is
    while True:
        forklift_weight = float(input("Insert the weight of the forklift: "))
        if (forklift_weight < 0):
            print("Please, enter a positive number.")
            continue
        break
    while True:
        operator_weight = float(input("Insert the weight of the operator: "))
        if (operator_weight < 0):
            print("Please, enter a positive number.")
            continue
        break
    while True:
        load_weight = float(input("Insert the weight of the load: "))
        if (load_weight < 0):
            print("Please, enter a positive number.")
            continue
        break
    while True:
        L1_distance  = float(input("Insert the distance L1: "))
        if (L1_distance < 0):
            print("Please, enter a positive number.")
            continue
        break
    while True:
        L2_distance  = float(input("Insert the distance L2: "))
        if (L2_distance < 0):
            print("Please, enter a positive number.")
            continue
        break
    while True:
        L3_distance  = float(input("Insert the distance L3: "))
        if (L3_distance < 0):
            print("Please, enter a positive number.")
            continue
        break
    #solves for R, or the rear wheel reaction force
    rear_wheel_moment=((L2_distance*(forklift_weight+operator_weight))-(load_weight*L1_distance))/(2*(L2_distance+L3_distance))
    #solves for F, or the front wheel reaction force
    front_wheel_moment=((forklift_weight+operator_weight)+load_weight-(2*rear_wheel_moment))/2
    #solves for the max load that the forklift can take
    max_load=(L2_distance*(forklift_weight+operator_weight))/(L1_distance)
    #prints the statements required by the assignemnt description
    print(f"The reaction force R is {round(rear_wheel_moment, 4)}\n")
    print(f"The reaction force F is {round(front_wheel_moment, 4)}\n")
    print(f"The maximum load weight is {round(max_load, 4)}\n")
#One function for both part 2 and 3, we just pass different arguements in to change the f strings and the graphed data
def graph_mxstble_general(distance_str, max_str):
    while True:
    #Makes sure it is positive as seen in fucntion above, in theory could be made shorter by using individual functions for each input, everything is named accurately
        forklift_weight = float(input("Insert the weight of the forklift: "))
        if (forklift_weight < 0):
            print("Please, enter a positive number.")
            continue
        break
    while True:
        operator_weight = float(input("Insert the weight of the operator: "))
        if (operator_weight < 0):
            print("Please, enter a positive number.")
            continue
        break
    while True:
        entered_distance = float(input(f"Insert the distance {distance_str}: "))
        if (entered_distance < 0):
            print("Please, enter a positive number.")
            continue
        break
    while True:
        max = int(input(f"Insert the maximum desired {max_str}: "))
        if max<0:
            print("Please, enter a positive number.")
            continue
        break            
    #We dont check if number of points is positive as it isn't a real world value
    num_points = int(input("Insert the number of points to plot: "))
    distance = np.linspace(0, max, num_points)
    #The conditional which switches the calculations for option 2 and 3
    if(distance_str == ("L2")):
        weight=(entered_distance*(operator_weight+forklift_weight))/distance
    else:
        weight=(distance*(operator_weight+forklift_weight))/entered_distance
    plt.figure(figsize=(10, 6))
    plt.plot(distance, weight, linestyle='-', color='g', label=f'Weight vs {max_str}')
    plt.xlabel(f"{max_str}")
    plt.ylabel("Max Load")
    plt.legend()
    plt.grid(True)
    plt.show()
def max_stble_fweight():
    #checks if positive for real values, everything is named afor what it is
    while True:
        max_fweight = np.abs(int(input(f"Insert the maximum desired weight of the forklift: ")))
        operator_weight = float(input("Insert the weight of the operator: "))
        if (operator_weight < 0):
            print("Please, enter a positive number.")
            continue
        break
    while True:
        L1_distance = float(input("Insert the distance L1: "))
        if (L1_distance < 0):
            print("Please, enter a positive number.")
            continue
        break
    while True:
        L2_distance = float(input(f"Insert the distance L2: "))
        if (L2_distance < 0):
            print("Please, enter a positive number.")
            continue
        break
    #No positive check as it is only used for graphing
    num_points = int(input("Insert the number of points to plot: "))
    # Generate wf values in the range [0, wf_max](an array)
    wf_values = np.linspace(0, max_fweight, num_points)


    # Calculate the maximum weight of the load before tipping

    wl_max_values = ((wf_values+operator_weight)*L2_distance)/ L1_distance
    # Plots the graph of the max stable load
    plt.plot(wf_values, wl_max_values, label='Max Load Weight', color='b')
    plt.xlabel('Wf')
    plt.ylabel('Maximum stable load')

    plt.show()
#Loop which runs the command line program and will check for 1-5 ints to determine what the user wants, also checks if it has selected and option, it then executes the function listed in the assignment description that is related to the integer
while n!=5:
    print("Stability of a forklift\n-----------------------\n1. Find maximum stable load\n2. Graph maximum stable load as a function of L1")
    print("3. Graph maximum stable load as a fucntion L2\n4. Graph maximum stable load as a function of the forklift weight\n5. Quit\n")
    #Try makes sure it is an int, i decided not to use it in the other functions as it would lenghten the code significantly and it is assumed they are enetering a float or int, it also very dificult to include all edge cases
    try:
        n = int(input("Please, make a choice [1-5]: "))
    except ValueError as e:
        print("Please enter an integer\n")
    #the if/elif statement that checks the input
    if n==1:
        max_stable_load()
    elif n==2:
        graph_mxstble_general("L2", "L1")
    elif n==3:
        graph_mxstble_general("L1", "L2")
    elif n==4:
        max_stble_fweight()
    elif n==5:
        print("Exiting...")
    else:
        print("Invalid choice. Please try again")




