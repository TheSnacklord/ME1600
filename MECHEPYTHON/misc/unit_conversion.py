#Introduction statement listed in assignment doc
print("\nUnit conversion utility\n-----------------------\n\nChoose what conversion you want to perform\n")
print("1. Meters to miles\n2. Miles to meters\n3. Watts to horsepower\n4. horsepower to watts\n5. kilogram to pound-mass\n6. poundmass to kilograms\n")
#gets input from person and turns it to int
def conversion():   
    return int(input("Insert a choice [1-6]:"))
#function to print what the conversion will be
def format_input(s1, s2):
    return float(input(f"Enter {s1} to convert to {s2}:"))
#conversion functions
def meters_miles():
    x = format_input("meters", "miles")
    print(f"{x} meters is {x/1609.34} miles")
def miles_meters():
    x = format_input("miles", "meters")
    print(f"{x} miles is {x*1609.34} meters")
def watts_horses():
    x = format_input("watts", "horsepower")
    print(f"{x} watts is {x/745.7} horsepower")
def horses_watts():
    x = format_input("horsepower", "watts")
    print(f"{x} horsepower is {x*745.7} watts")
def kilo_pound():
    x = format_input("kilogram", "pounds")
    print(f"{x} kilogram is {x*2.20462} pounds")
def pound_kilo():
    x = format_input("pounds", "kilograms")
    print(f"{x} pounds is {x/2.20462} kilograms")
#essentially a switch checking what int it is, or if it is in bounds
if(conversion()==1):
    meters_miles()
elif(conversion()==2):
    miles_meters()
elif(conversion()==3):
    watts_horses()
elif(conversion()==4):
    horses_watts()
elif(conversion()==5):
    kilo_pound()
elif(conversion()==6):
    pound_kilo()
else:
    print("retry, please try again")



