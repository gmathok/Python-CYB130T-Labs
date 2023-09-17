# #This program takes the user's name as input and greets them with a personalized message.
# #Green Mathok
# #9/17/2023

# Prompt user for their name and convert input to a string
user_name = str(input("Please enter your name: "))
result = user_name
print(f"Hi {result}!, I hope you are having a great day ")

##############################################################
#Optimized code after realizing input function returns a string by defult and the 
#result variable is uncessary.
#######################################################################
# Prompt the user for their name and store it under the created variable
user_name = input("Please enter your name: ")
#Greet the user with the personalized message.
print(f"Hi {user_name}!, I hope you are having a great day. ")
