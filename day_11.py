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