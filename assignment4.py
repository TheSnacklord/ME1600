import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

#function to plot points on graphs, the interpolation on the graphs, and another graph of the residuals of the data vs the interpolations
def plot_points(x_array, y_array, x_label, y_label, title):
    #defines the graphs and figure
    fig, (ax1, ax2)=plt.subplots(2, 1, figsize=(8, 12))
    
    # this is just the scatter plot of the original data
    ax1.scatter(x_array, y_array, color="k", label="Data", marker="*", s=50)
    
    #numpy array to 30 (essentially the x_array)
    x_interpolate = np.linspace(0,30, 30)
    
    #lists for the colors, markers, names, degrees, and linestyle
    degrees = [1, 2, 3, 4]
    colors = ["red", "blue", "green", "purple"]
    names = ["Linear", "Quadratic", "Cubic", "Fourth-order"]
    symbols=["x", "", "|", "o"]
    linestyle=["-", "--", "-", "-"]

    #loop for the first graph
    for degree, color, name, symbol, line in zip(degrees, colors, names, symbols, linestyle):
        #polynomial.fit to fit the x_array to the y_array with a certain degree
        fit = Polynomial.fit(x_array, y_array, degree)  
        #calculates y values fit from x_interpolation
        y_fit = fit(x_interpolate)
        #plots the polynomials and the points
        ax1.plot(x_interpolate, y_fit, label=name, color=color, linestyle=line, marker=symbol)
    #sets up the graph for graph 1
    ax1.set(xlabel=x_label, ylabel=y_label)
    ax1.set_title(title)
    ax1.grid(True)
    ax1.legend()

    #loop for the second graph, it iterates through each of the lists defined at the top
    for degree, color, name, symbol, line in zip(degrees, colors, names, symbols, linestyle):
        #redefines everything for the new loop
        fit = Polynomial.fit(x_array, y_array, degree)
        y_fit = fit(x_interpolate)
        #solves for the residuals
        residuals=(-y_array[1:]+y_fit)
        #graphs the residuals and x values
        ax2.plot(x_array[1:], residuals, label=name, color=color,  linestyle=line, marker=symbol)
    #sets up graph 2 and shows the plot
    ax2.set(xlabel=x_label, ylabel='Residual (ppm)')
    ax2.set_title("Residual of bacteria growth fit")
    ax2.grid(True)
    ax2.legend()
    plt.tight_layout()
    plt.show()

#inputs from file (if necessary) there was a file included so i included an input from file, although it wasnt explicitly stated in the project description
time_data=[]
bact_ppm_data=[]
filename = input("Type file name to open, for default values type 'default': ")
#takes data from file and reads it and submits the arrays to plot_points
if(filename!="default"):
    with open(filename, mode='r') as f:
        lines=f.readlines()
        headers=lines[0].strip().split(',')
        x_name, y_name = headers[0], headers[1]
        for line in lines[1:]:
            value=line.strip().split(',')
            time_data.append(float(value[0]))
            bact_ppm_data.append(float(value[1]))
            time_plot=np.array(time_data)
            bact_plot=np.array(bact_ppm_data)
    f.close
    plot_points(time_plot, bact_plot,x_name, y_name, "Bacteria growth fit")
else:
    #uses the default values given in the file
    time = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])
    bacteria_ppm = np.array([8, 13, 21, 34, 53, 79, 113, 157, 211, 277, 356, 448, 556, 680, 821, 980, 1160, 1360, 1581, 1826, 2095, 2389, 2710, 3058, 3435, 3841, 4279, 4749, 5252, 5789, 6362])
    plot_points(time, bacteria_ppm, "Time(min)", "Bacteria(ppm)", "Bacteria growth fit")