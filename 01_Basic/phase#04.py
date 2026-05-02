
# #Utility function library

# Tool 1: Add
def add(a, b):
    return a + b

# Tool 2: Subtract
def subtract(a, b):
    return a - b

# Tool 3: Even or Odd
def is_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Tool 4: Capital letters
def make_upper(text):
    return text.upper()

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
text = input("Enter a word: ")

print("Add =", add(a, b))
print("Subtract =", subtract(a, b))
print("Even/Odd =", is_even(a))
print("Upper =", make_upper(text))


#Password strength checker

password = input("Enter password: ")

length = len(password)

if length >= 12:
    print("Strong Password!")
elif length >= 8:
    print("Medium Password!")
else:
    print("Weak Password!")