# task: create a program that:
# takes the user's input as the diameter
# calculates the circumference and area of the circle
# prints the results

pi = 3.14159265359

def diameter():                            #taking user input of diameter
    global calcDiameter
    calcDiameter = float(input())
    return calcDiameter

def circumference():                      #calculating radius and circumference
    global calcRadius
    calcRadius = calcDiameter / 2
    calcCircumference = 2 * pi * calcRadius
    return calcCircumference

def circleArea():                                         #calculating area of the circle
    calcCircleArea = pi * calcRadius * calcRadius
    return calcCircleArea

print("For a circle with a diameter of", diameter(), ", the circumference is:", circumference(), "and the area is:", circleArea())