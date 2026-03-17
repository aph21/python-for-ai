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
