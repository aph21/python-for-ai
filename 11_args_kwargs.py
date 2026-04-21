food = "pizza"
food.replace("z", "s")
print(food)

#why it still prints 'pizza' instead of "pissa"? -> 
# strings in python are immutable, which means they cannot be changed in place.
# when we call food.replace("z", "s") -> it doesn't modify the original string 'pizza', it returns a new string and we are not saving it , so the fix is:

food = 'pizza'
food = food.replace("z", "s")
print(food)


####### *args and **kwargs ##########
# we know functions accept parameters
def add(a, b):
    return a + b
add(1, 2) # it works and returns 3
add(1, 2, 3) # here Error -> it only takes 2 arguments but here we are passing 3 arguments



## arguments -> when calling a function values we pass are known as arguments
## Positional arguments -> arguments that are passed based on position or order is known as positional arguments
#used in *args
## example: 
def greet(name, age):
    print(name, age)
greet("Anjana", 24)

#python assigns values by order:
# name = "Anjana"
# age = 24
# because 1st arg -> 1st param and 2nd arg -> 2nd param

##Keyword arguments -> are passed using paramter names
greet(age= 30, name ="Prabha")
#here order doesn't matter 
# used in **kwargs



## Parameters -> is the variable written in function definition.
#it is a placeholder that will receive the values when function is called
#in above example, name and age are called paramters


#we know function accept parameters:
def add(a,b):
    return a + b
add(1,2) #works
add(1,2,3) # Error: takes only 2 arguments but here we have passed

#what if we don't know how many arguments user will pass in advance?
# for example:
# 1. a function that adds any number of numbers
# 2. a function that accepts any number of configuration
# 3. An AI tool that accepts flexible number of parameters
## in these type of situation we use *args and **kwargs in python




###### *args and **kwargs

## *args - allows a function to accept any number of positional arguments
def add(*args):
    print(args)
    print(type(args))
add(1,2,3,4,5)
add(2,19)

#args are stored as tuples
#what does "*" tells python?
# to collect all the positional arguments and pack them into a tuple
#using *args practically:
def add(*args):
    total = 0
    for item in args:
        total += item
    return total
print(add(1,2))
print(add(4,5,1,1))
print(add(3,3,3))


##*args with regular paramters
def intro(name, age, *hobbies):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Hobbies: {hobbies}")
intro("Ahmed", 25, "coding", "reading", "AI")


##Rule:
#regular paramter should always come first then *args then **kwargs



### **kwargs -> allows function to accept any number of keyword arguments
#here ** tells python to collect all the keyword arguments and pack them into dictionary
#So no matter how many key=value pairs you pass, they all get collected into one dictionary called kwargs.

def show_info(**kwargs):
    print(kwargs)
    print(type(kwargs))


show_info(name="Ahmed", role="AI Engineer", experience=2)


#Using **kwargs Practically
def build_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:  {value}")
build_profile(name="anjana", role="AI engineer", city="Bengaluru")


## using both *args and **kwargs together
def show_everything(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)


show_everything(1, 2, 3, name="Ahmed", role="AI Engineer")

## * and ** the unpacking operators
##why used as unpacking operators? -> * and ** are not just used in function definition they are also used when calling the function

##unpacking list into a function:

def add(a, b, c):
    return a + b + c
numbers = [1, 2, 3]
# add(numbers) # here we get ERROR (TypeError) saying add() missing 2 required positional arguments: 'b' and 'c' -> means we are only passing one list not 3 numbers, so we need to unpack before adding
add(*numbers) ## unpacks list into: add(1, 2, 3)
print(add(*numbers))


## Unpacking dictionary into function:
def intro(name, role, city):
    print(f"{name} is a {role} from {city}")

info = {"name" : "Anjana", "city" : "Bengaluru", "role" : "Agentic AI Developer" }

intro(**info)
print(intro(**info))


##f string -> formatted string literal
# allows to embed a variable or an expression directly inside a string using {}



##Interview Questions
#1.
def show(*args):
    print(args)
    print(type(args))

show(1, "hello", True, 3.14)

# output is: (1, 'hello', True, 3.14)
# <class 'tuple'>
# why? -> because *args collects all the positional arguments into a tuple
#when calling: show(1, "hello", True, 3.14), python packs them as : args = (1, "hello", True, 3.14)



##2.
def show(**kwargs):
    print(kwargs)
    print(type(kwargs))

show(name="Ahmed", age=25, role="AI Engineer")

#{'name': 'Ahmed', 'age': 25, 'role': 'AI Engineer'}
#<class 'dict'>
#why ? - because **kwargs collects all the keyword arguments into dictionary


##3.
def func(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

func(1, 2, 3, 4, 5, name="Ahmed", role="AI Engineer")

#why?
#-because in this example we have 4 parameters: a, b, 8args, and **kwargs
#* python follows this order: first regular arguments( first and 2nd positional arguments, then extra positional arguments 3,4 ,5 into *args and next are leyword argumenst thos are into **kwargs
# so 1 is passed into a, 2 is passed onto b
# remaining extra positional arguments passed onto *args and in arga they allow function to accept any number of positional arguments and then pack them into tuple so they are packed into tuple -> (3,4,5)
# whereas **kwargs allows function to accept any number of keyword arguments and pack them into dictionary, so name="Ahmed", role="AI Engineer" are packed into dict {'name': 'Ahmed', 'role': 'AI Engineer'}


##4
def add(a,b,c):
    return a + b + c
numbers = [10, 20, 30]

result = add(*numbers)
print(result)

#output is: 60, because 
# *numbers -> is also used for unpacking the list into items
# if we pass whole list [10, 20, 30] without unpacking then python consider it as one list not 3 arguments, so it will result with TypeError telling that 'b' and 'c' are not passed
# so we first unpack the items in numbers using add(*numbers) and then print it


##5
def build_request(model:str, **kwargs):
    request = {"model": model, **kwargs}
    return request
result = build_request("gpt-4", temperature = 0.7, max_token = 500, stream = True)
print(result)

#output is: {'model': 'gpt-4', 'temperature': 0.7, 'max_token': 500, 'stream': True}
#why?
# when we call build_request("gpt-4", temperature=0.7, max_tokens=500, stream=True), so mapping happens:
# model = "gpt-4" and kwargs = {"temperature" :0.7, "max_tokens" :500, "stream" : True }
# **kwargs collects keyword arguments as a dictionary, and ** can be used to unpack a dictionary into another dictionary.

def func(*args, **kwargs):
    print(args)
    print(kwargs)
data = (1,2,3)
config = {"model": "gpt-4", "temperature" : 0.5}

func(*data, **config)