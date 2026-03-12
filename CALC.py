# Incorporate functions into the Python program (Hint: is any part of your code reusable?)Please submit your repository link here. 
# Basic Calculator using Functions

# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    return a / b

# Function for modulus
def modulus(a, b):
    return a % b


# Main program
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation:")
print("+  Addition")
print("-  Subtraction")
print("*  Multiplication")
print("/  Division")
print("%  Modulus")

operation = input("Enter operation: ")

if operation == "+":
    print("Result:", add(num1, num2))

elif operation == "-":
    print("Result:", subtract(num1, num2))

elif operation == "*":
    print("Result:", multiply(num1, num2))

elif operation == "/":
    print("Result:", divide(num1, num2))

elif operation == "%":
    print("Result:", modulus(num1, num2))

else:
    print("Invalid operation")

print("End of Program")