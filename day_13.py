#Higher Order Function
# We know that in python functions are known as first class objects.
# what does first class object means?
#in python, function are treated like any other values -> like intergers, strngs, or dictionary.
# this means functions can be:
# 1. assigned to any variable
# 2. can be stored into list or dictionary
# 3. can be passed as an argument to another function
# 4. can be returned from another function


# 1. Assigned to a variable

def greet(name):
    return f"Hello {name}"
#assigning a function to a variable
say_hello = greet
print(say_hello("Anjana"))
# say_hello is not calling the function, it is pointing to same function object as greet

# 2. Stored in a list

def add(a,b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

operations = [add, subtract, multiply]

for operation in operations:
    print(operation(10, 5))

#10, 5, 50