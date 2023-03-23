# task: create a program that:
# takes the user's input as the diameter
# calculates the circumference and area of the circle
# prints the results

pi = 3.14159

print("Please enter the diameter:")


diameter = input()

def circumference():                   #calculating radius and circumference
    global calcRadius
    calcRadius = int(diameter) / 2
    calcCircumference = 2 * pi * calcRadius
    return calcCircumference

def circleArea():                                         #calculating area of the circle
    calcCircleArea = pi * calcRadius * calcRadius
    return calcCircleArea

try:
    x = int(diameter)                 #Checks to see if the diameter can become an integer.
except ValueError:
    print("You entered text. Please run the program again and input a valid number.")  #If x cannot be turned into an integer, it means the input was text. So it will raise the "ValueError" which will print the message.
else:
    if int(diameter) < 0:
        print("You entered a negative number. Please run the program again and input a valid number.")
    else:
        print("For a circle with a diameter of", diameter, "\n" "The circumference is:", circumference(), "\n" "The area is:", circleArea())