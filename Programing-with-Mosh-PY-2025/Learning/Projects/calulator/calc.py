
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
#defining the functions for each operation


opration = { #dictionary of operations making it easy to access
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

op = str(input(f"Please select an operation {list(opration.keys())}: ")) #shows the user the available operations

if op in opration.keys(): #got stuck on this part, it was not working as expected was using == until i Spoke my logic out loud and i need to check if the input was IN not == to 
   print(f"{opration[op](x, y)} here is your result")
else:
   print("Invalid operation selected. Please try again.")
   exit() 