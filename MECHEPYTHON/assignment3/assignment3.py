import numpy as np
#initializes the vector and its magnitude
resultant_force = np.array([0, 0])
resultant_force_magnitude=0
#intro to the program
print("Resultants of a force on a truck\n-----------------------------")
print("\n   Insert the following data:\n")
#asks for input of data for vectors
truck_mass = float(input("       Mass of truck (kg): "))
engine_force =float(input("       F_{x, Engine} (N): "))
friction_force =float(input("       F_{x, Friction} (N): "))
drag_force =float(input("       F_{x, Drag} (N): "))
wind_x_force =float(input("       F_{x, Wind} (N): "))
wind_y_force =float(input("       F_{y, Wind} (N): "))
#solves for the vectors and magnitude 
resultant_force = np.array([engine_force+(friction_force*2)+drag_force+wind_x_force, wind_y_force+(-9.81*truck_mass)])
resultant_force_magnitude=round(np.linalg.norm(resultant_force), 2)
wind_magnitude=round(np.linalg.norm([wind_x_force, wind_y_force]), 2)
#print statement of answers
print(f"The resultant of the force is R = {round(resultant_force[0], 3)}i+{round(resultant_force[1], 3)}j N\n")
print(f"The magnitude of the resultant is |R| = {resultant_force_magnitude}N")
print(f"\nThe magnitude of the force exerted by the wind is |FWind| = {wind_magnitude}N")



