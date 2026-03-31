#Higher order function

#in python function is not just a set of instructions, IT is also a VALUE - just like number or string
#a function can be stored in a variable -> this is what "FIRST CLASS OBJECT" means

# a function is called HOF (higher order function) if it does atleast one of these two:
    #1. takes another function as an input (argument)
    #2. returns a function as an output
#when we pass a function to another function then receiving function becomes HOF.
 
def apply(func, value):
    return func(value)

def double(x):
    return x * 2

result = apply(double, 5)
print(result)

## KEY RULE : when passing a function as an argument, NO PARANTHESES -> double NOT double()

#Why do we need HOF?
#HOF helps us write flexible, reusable and modular code.
#They are the foundation of functional programming.

# pass different function to the same HOF

def double(x):
    return x * 2

def square(x):
    return x * x

def make_negative(x):
    return -x

def apply(func, value):
    return func(value)

print(apply(double, 5))
print(apply(square, 5))
print(apply(make_negative, 5))

#One HOF (apply), three different behaviors — just by swapping the function you pass in. This is the power of HOFs — flexible, reusable code


#A HOF can also build and return a new function

