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
