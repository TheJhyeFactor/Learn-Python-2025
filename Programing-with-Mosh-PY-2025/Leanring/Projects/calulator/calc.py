
def add (x, y):
    return x + y;
def subtract (x, y):
    return x - y
def multiply (x, y): 
    return x * y
def divide (x, y): 
    return x / y if y != 0 else "Error! Division by zero."
def modulus (x, y):
    return x % y
def exponent( x, y):
    return x ** y
def floor_division(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x // y

opration = {
"Add" : add,
"Subtract" : subtract,
"Multiply" : multiply, 
"Divide" : divide,
"Modulus" : modulus,
"Exponent" : exponent,
"Floor_Division" : floor_division
}

print("Welcome to the Calculator!")    
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

op = str(input(f"Please select an operation {list(opration.keys())}: "))

if op in opration.keys():
   print(f"{opration[op](x, y)} here is your result")
else:
   print("Invalid operation selected. Please try again.")
   exit() 