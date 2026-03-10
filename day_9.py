######### Functions #########
# definition -> A function is a named, reusable block of code that takes input, do something and return optionally.
# but this is SHALLOW definition
# actuallly what function do? - 
# Function is a first class object in python, which means its not just a block of code, it is a value, it can be stored in list, assigned to a variable, passesd as an argument to another function, returned from another function, and can be created dynamically at runtime.
# function is a way to organize and reuse code, it allows us to break down a complex problem into smaller, manageable pieces, and it also allows us to abstract away the details of how something is done, so we can focus on what we want to achieve.

def greet(name: str) -> str:
    """This function takes a name as input and returns a greeting message."""
    return f"Hello, {name}"


#### function with input paramters
# what if you want to greet other people? you can pass the name as an argument to the function, and it will return the greeting message for that name.

def greet(name):
    print("Hello," + name)
greet("Anjana")
#here name is a paremeter, it is a variable that only exists inside the function. when you call the greet("Anjana"), the value "Anjana", gets assigned to name automatically, and the function body is executed, which prints "Hello, Anjana".


####Functions with Multiple Inputs
def  add(a, b):
    return a + b
print(add(2,3))
print(add(-34, -11))

#order matters
def intro(name, age):
    print(f"My name is {name} and I am {age} years old.")
intro("Anjana", 25)  # Output: My name is Anjana and I am 25 years old.
intro(25, "Anjana")  # Output: My name is 25 and I am Anjana years old.


######## return statement
# printing is not same as returning, when you print something, it is displayed on the console, but it is not returned to the caller, when you return something, it is sent back to the caller, and it can be stored in a variable, or used in an expression.\
#example
def add_with_print(a, b):
    print(a + b)

def add_with_return(a, b):
    return a + b

#They look similar. But they are completely different.
# add_with_print(2, 3)  # Output: 5 and None
# add_with_return(2, 3)  # Output: 5
# Print -> shows something on screen. the value disappears after that you cannot use it again.
#return -> sends the value back to whoever called that function. we can store it, use itand pass it to another function, and do whatever we want with it. it is a way to get the result of a function and use it in our code.


##In AI systems, you almost always use return. Because you need the output of one function to feed into the next function, and you need to store the output of a function in a variable, so you can use it later in your code. if you use print, you will not be able to do that, because print does not return anything, it just shows something on the screen.



#def -> keyword used to define a function
#greet -> name bound to the function object in the current namespace
# (name : str) -> str -> function signature, it specifies the parameters and return type of the function
# """This function takes a name as input and returns a greeting message.""" -> docstring, it is a string literal that appears right after the function definition, it is used to document the function, it can be accessed using the __doc__ attribute of the function object.
# # : -> tells function body is starting from the next line, and it is indented to indicate that it is part of the function body.  

# in functions -> we write  the logic once and reuse it everywhere in the ocde.
#example:
def greet():
    print("Hello")
greet()  # Output: Hello

# Mistake 1: Mutable default arguments
def add_item(item, cart=[]):
    cart.append(item)
    return cart
print(add_item('apple'))  # Output: ['apple']
print(add_item('banana'))  # Output: ['apple', 'banana']

#the dafualt [] is craeted once when the definitio