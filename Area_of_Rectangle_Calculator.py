# #This program calculates the Area of a rectangle based on user given dimensions.
# #9/17/2023

# Prompt user for the length and width
# length = input(int("Please enter the length: "))
# width = input(int("Please enter the width" ))
# result = (length * width)
# print(f"The Area of {length} and {width} is {result}. ")

#################################################################
# The above code resulted in a ValueError due to attempting to apply int() to the
# result of the input instead of the input function itself.
#################################################################

# Prompt user for the length and width of rectangle and convert to integers
length = int(input("Please enter the length: "))
width = int(input("Please enter the width: "))
#calculate the Area of the rectangle
result = length * width
#Return the results with the provided dimensions.
print(f"The Area of {length} and {width} is {result}. ")