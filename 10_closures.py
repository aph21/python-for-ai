####### CLOSURES #########

## A clusure happens when a :
# 1. nested function references a variable from the enclosing scope
# 2. nested function is returned and survives the enclosing function
# 3. The variable from enclosing scope is remebered even after  the outer function has finished its execution


def outer():
    msg = "I am outer"

    def inner():
        print(msg)

    return inner  # returning function but not calling it


my_fnc = outer() #outer finishes execution here but inner is still alive and has access to msg variable
my_fnc() # but inner still has access to msg variable and can print it


#This is the key moment. outer() has finished. message should be gone. But inner closed over message and kept it alive in memory. That is why it is called a closure.



##The Famous Loop Bug

function = []

for i in range(3):
    def f():
        print(i)
    function.append(f)

function[0]() # 2
function[1]() # 2   
function[2]() # 2

# expectation : o, 1, 2 but it prints 2, 2, 2# WHYYYY?
# because python stores references to the variables not the value.
# All pront 2 because all functions references to same i variable, which ends at 2 after the loop


## Fix in Python 
functions = []

for i in range(3):
    def f(x = i): #captures the current value of i as default argument
        print(x)
    functions.append(f)


functions[0]()
functions[1]()
functions[2]()
# default arguments are evaluated at the function creation time
# not at function call time

# so when i = 0
# python does this internally -> x = i --> x = 0
# then f -> default x = 0
# so memory now : f1 :- defalut x = 0
# append functions -> [f1]
# KEY POINT : f1 does NOT depend on i anymore
#it has its own x = 0

#second iteration when i = 1
# so now def f (x = i):
# so python evaluates default : x = 1
# so craetes new function f2:- default x = 1
# so append functions -> [f1, f2]
# again f2 has its own x so not shared

# same happens for third iteration when i = 2

# so when functions[0]() called -> f1 runs
# when functions[1]() called -> f2 runs
# when functions[2]() -> f3 runs
# i.e
#0
#1
#2




#the nonlocal keyword
# if we want to modify the variable from enclosing scope inside nested function we need nonlocal
# In closure inner function can read a variable from enclosing scope. But if we try to reassign it, python treats it as new local variable instead:
def counter():
    count = 0

    def inc():
        count = count + 1 # this makes python think that count is local variable inside inc(), but it is not defined inside there yet, so the fix is using nonlocal
        print(count)

    return inc

#so nonlocal tells python "this variable is from enclosing function, not a new local one"

def counter():
    count = 0

    def inc():
        nonlocal count
        count = count + 1
        print(count)
    return inc

cnt = counter()
cnt()
cnt()
cnt()

##key rules:
#1. nonlocal works only with enclosing functions, for global scope use global instead
#2. The variable must already exist in the enclosing function. You cant create new variable with nonlocal
#3. Without nonlocal reading works fine - only reassignment causes problem