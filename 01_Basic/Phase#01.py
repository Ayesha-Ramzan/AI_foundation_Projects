
# Task 1: Personal Info Program
# Ask the user:
# name?
# age?
# city?
# print
#Hello <name>!
#You are cage> years old and live in <city>.
name = input("Name? ")
age = int(input("Age? "))
city = input("City? ")
# Print results:
print(f"Hello {name}!")
print(f"You are {age} years old and live in {city}.")



#Task 2: Simple Calculator
#Ask the user for:
#Two numbers
# Print:
# Addition
#Subtraction
# Multiplication
# Division
num1=int(input("enter number_1:"))
num2=int(input("enter number_2:"))
#print(f"additon: (num1+num2)\nSubtraction: (num1-num2}\nMultiplication: (num1*num2)\nDivision:{num1/num2}
num1=float(input("enter number_1:"))
num2=float(input("enter number_2:"))
print(f"Additon: {num1+num2}\nSubtraction:{num1-num2}\nMultiplication: {num1*num2}\nDivision: {num1/num2}")
#\n:next line


#Task 3: Temperature Converter
#Input temperature in Celsius
# Convert it to Fahrenheit
#Formula: (C 9/5) + 32
C=float(input("Temp in celsius="))
F=(C*9/5) + 32
print(F)



# Task 4: Type Check
# Create variables of:
# int, float, string, boolean
#print their type using type()
int = 5
float = 2.5
string = "ash"
boolean = True

print(f"{type(int)}\n{type(float)}\n{type(str)}\n{type(bool)}")
print(type(int))
print(type(float))
print(type(string))
print(type(boolean))