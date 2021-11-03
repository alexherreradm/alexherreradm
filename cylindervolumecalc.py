import math

while (True):
    try:
        radius = float(input("Enter the radius of cylinder: "))
        if (radius < 0):
            print("Negative initial positions are not allowed.")
            continue
    except ValueError:
        print("The value you entered is invalid. Only positive numerical value are valid.")
    else:
        break


while (True):
    try:
        height = float(input("Enter the height of cylinder: "))
        if (height < 0):
            print("Negative initial positions are not allowed.")
            continue
    except ValueError:
        print("The value you entered is invalid. Only positive numerical value are valid.")
    else:
        break

pi = float(math.pi)
volume_of_cylinder = pi*pow(radius,2)*height
print("The volume of a cylinder that has a radius of",radius,"meters and a height of",height,"meters is",volume_of_cylinder,"meters^3.")

