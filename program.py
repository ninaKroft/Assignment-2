# task: create a program that:
# takes the user's input as the diameter
# calculates the circumference and area of the circle
# prints the results

pi = 3.14159

print("Please enter the diameter:")


diameter = input()

def circumference():                   #Function that calculates the circumference
    global calcRadius
    calcRadius = float(diameter) / 2
    calcCircumference = 2 * pi * calcRadius
    return calcCircumference

def circleArea():                                         #Function that calculates the area of the circle
    calcCircleArea = pi * calcRadius * calcRadius
    return calcCircleArea

try:
    x = float(diameter)                 #Checks to see if the diameter can become an integer.
except ValueError:
    print("You entered text. Please run the program again and input a valid number.")  #If the diameter cannot be turned into an integer, it means the input was text. A ValueError will be raised when it is not able to be turned into an integer. The program will recognize this error and know to print the message.
else:
    if float(diameter) < 0:        #If the diameter is able to become an integer, the code will continue down to here, where the program checks if the diameter is a negative number. If it is, it will print the message.
        print("You entered a negative number. Please run the program again and input a valid number.")
    else:
        print("For a circle with a diameter of", diameter, "\n" "The circumference is:", circumference(), "\n" "The area is:", circleArea())  #If the diameter is a valid number, the program will run the functions to calculate the circumference and area of the circle then print them.