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

#the dafualt [] is craeted once when the definition is executed, and it is shared across all calls to the function. so when you append an item to the cart, it modifies the same list, and the next time you call the function, it will return the modified list with all the items that were added previously. to avoid this issue, you can use None as the default value and create a new list inside the function if the cart is None.



## Default Parameter Values
# sometimes we need a parameter to have a default value, - used when caller doesnopt provide one
def greet(name, language = "English"):
    if language == "English":
        print("hello," + name)
    elif language == "Spanish":
        print("Hola," + name)
greet("Anjana")
greet("Anjana", "Spanish")

#paramters with default values must come after paramters without default values, otherwise it will raise a syntax error. because when you call the function, it will not know which value to assign to which parameter, and it will cause confusion. so always put parameters with default values at the end of the parameter list.


### Type Hints — Writing Professional Code
def calc_token(token: int, price : float) -> float :
    return (token/1,00,000) * price

# here :int , :float and -> float are type hints, they are not enforced by the python interpreter, but they are used to indicate the expected types of the parameters and return value of the function. they are used for documentation purposes, and they can also be used by static type checkers like mypy to catch type errors before runtime. they can also be used by IDEs to provide better code completion and error checking.
# They tell you :
#1. what type of input the function expects
#2. what type of output the function returns
# Without type hints — harder to understand
def process(x, y):
    return x + y

# With type hints — immediately clear
def process(x: int, y: int) -> int:
    return x + y



### functions returning multiple values
def get_user_info():
    name = "Anjana"
    age = 24
    role = "Agentic AI Developer"
    return name, age, role


#unpacking the returned values
name, age, role = get_user_info()
print(name)  # Output: Anjana
print(age)   # Output: 24   
print(role)  # Output: Agentic AI Developer
#Under the hood, Python is returning a tuple ("Ahmed", 25, "AI Engineer") and you are unpacking it. This connects directly to what you already know about tuples, and it shows how they can be used to return multiple values from a function. This is a common pattern in Python, and it allows you to return multiple pieces of related information from a function without having to create a custom class or data structure.


#### Variable Scope — Where Variables Live
# Variables created inside the functions only exist inside the function.
def my_fnc():
    message = "I am inside the function"
    print(message)

my_fnc()
#print(message) #NameError: name 'message' is not defined -> why? because message is a local variable, it only exists inside the function, and it is not accessible outside the function. when you try to print message outside the function, it raises a NameError because message is not defined in that scope. this is called variable scope, and it is an important concept to understand when working with functions in Python.


#2
name = "Anjana" # global variable
def greet():
    print("Hello," + name)
greet()
# global exists outside the function, and it can be accessed inside the function. when you call greet(), it will print "Hello, Anjana" because it can access the global variable name. but if you try to modify the global variable inside the function, it will create a new local variable with the same name, and it will not affect the global variable. this is called variable shadowing, and it can lead to confusion if you are not careful. to modify a global variable inside a function, you need to use the global keyword.

#trying to modify the gloabl variable inside a function

count = 0
def inc():
    count += 1
inc()

#we get this error - UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
# to modify the global variable inside a fnc you need global keyword
# but in professional code, especially in AI pipelines -> AVOID GLOBAL VARIABLES  because they make the code unpredictable. INSTEAD you pass the values in And return values out.



########## Exercises ##########

#1. 
def add (a, b):
    print(a + b)
result = add(10, 2)
print(result)
#output is: 12 and None
#because the add function is printing the result isntead of returning it, so wehn we call add(10, 2), it prints 12, but it does not return anything, so the result variable gets assigned the value None. when we print(result), it shows None. to fix this, we need to change the add function to return the sum instead of printing it.


#2.
def multiply(a, b=2):
    return a * b

result1 = multiply(5)
result2 = multiply(5, 3)

print(result1) #10
print(result2) #15
#why? because in first call, we are only passing one argument, so it uses the default value of b, which is 2. so it returns 5 * 2 = 10. In second call it uses the value of b that we passed, which is 3, so it return 5 * 3 = 15. this is how default parameter values work in python, they allow us to call a function with fewer arguments than it defines, and it will use the default values for the missing arguments.

#3
def get_info():
    name = "Ahmed"
    age = 25
    return name, age

result = get_info()
print(result)
print(type(result))
#('Ahmed', 25)
#<class 'tuple'>
#why ? -> because when we return multiple values from a function, python automatically packs them into a tuple. so when we call get_info(), it returns a tuple ("Ahmed", 25), and when we print result, it shows the tuple. when we print type(result), it shows that it is a tuple. this is a convenient way to return multiple values from a function without having to create a custom class or data structure.


#4
def update_list(item, my_list=[]):
    my_list.append(item)
    return my_list

list1 = update_list("apple")
list2 = update_list("banana")
list3 = update_list("cherry")

print(list1)
print(list2)
print(list3)
#['apple', 'banana', 'cherry']
#why? because the default value of my_list is a mutable object (a list), and it is shared across all calls to the function. so when we append an item to my_list, it modifies the same list, and the next time we call the function, it will return the modified list with all the items that were added previously. to avoid this issue, you can use None as the default value and create a new list inside the function if my_list is None.
# corrected version:
def update_list(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list  



#5
def calculate(a: int, b: int) -> int:
    return a + b

result = calculate("10", "20")
print(result)

#output is: 1020
#why? because "10" and "20" are strings, so when you add them together, it concatenates them instead of performing arithmetic addition. the type hints in the function definition are not enforced by the python interpreter, they are just for documentation purposes and for static type checkers. so when you call calculate("10", "20"), it does not raise an error, it just returns the concatenated string "1020". to fix this, you need to either change the input to integers or modify the function to handle string inputs appropriately.


#Type hints are not enforced at runtime, they are just for documentation and human readability.
#this is exactly why in production AI systems, developers use libraries like pydantic to actually enforce the types at runtime.
#fastAPI and Langchain both are built on top of Pydantic.


#6
def outer():
    message = "I am outer"
    
    def inner():
        print(message)
    
    inner()

outer()

#output is: I am outer.
#why? Here `inner` is just a nested function. It accesses `message` from the enclosing scope. But after `outer()` finishes, everything is gone. `inner` does not survive outside.
#his concept is called **LEGB Rule** in Python — the order Python follows to look up variable names.

#LEGB rule : how python finds  variables

#when python sees a variable name, it searches in exact order:
# 1. L -> Local scope : inside current function
# 2. E -> Enclosing scope : inside any outer function
# 3. G -> Global scope : top level of the file
# 4. B -> Built-in scope : built-in names like print, len, etc.