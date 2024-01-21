
diameter = 54 #global variable

def get_perimeter():
    pi = 3.1416 # local variable
    radius = diameter/2 # radius is a local variable
    perimeter = 2*pi*radius #local variable
    return perimeter

print(f"The perimeter of a circle with radius {radius} is {get_perimeter()}.")
