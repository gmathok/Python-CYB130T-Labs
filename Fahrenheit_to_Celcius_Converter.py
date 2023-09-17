#This program converts user input from Fahrenheit to Celcius using the formula (F-32) * 5/9 = C.
# 2023-09-17

# Prompt user for the Fahrenheit temp & convert it to integer
fahrenheit = int(input("Please enter the Fahrenheit temperature: "))

# Convert Fahrenheit to celcius and bind to variable result
celcius = (fahrenheit - 32) * 5 / 9
# round the result so it's not a repeating decimal
result = round(celcius)

# Return the temp as Fahrenheit and the converted Celcius value.
print(f"The temperature of {fahrenheit} °F in Celcsius is {result} °C. ")