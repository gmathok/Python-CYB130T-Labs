# #This program calculate and prints the sum of two numbers entered by the user.
# #Green Mathok
# #9/17/2023
# num_1 = input("Enter a number ")
# num_2 = input("Enter secondary number ")
# print(sum(f"The sum of {num_1}and{num_2} is ")) 

###########################################################################
#Revised code after realizing the above code leads to a TypeError and wrong use of sum function.
###########################################################################
#Prompt user for two numbers
# num_1 = input("Enter a number ")
# num_2 = input("Enter a secondary number ")

# #Convert input strings into integers
# num_1 = int(num_1)
# num_2 = int(num_2)

# #Calculate the sum of the two numbers and store in the results variable
# result = num_1 + num_2

# # Here we use the f-string to format and print out the sum
# print(f"The sum of {num_1} and {num_2} is {result}")

#############################################################################
#Optimizing the above code after realizing input and int can be performed in
# the same line
#############################################################################
num_1 = int(input("Enter a number "))
num_2 = int(input("Enter a secondary number "))
result = num_1 + num_2
print(f" The sum of {num_1} and {num_2} is {result} ")
