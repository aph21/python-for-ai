####### CLOSURES #########

## A clusure happens when a :
# 1. nested function references a variable from the enclosing scope
# 2. nested function is returned and survives the enclosing function
# 3. The variable from enclosing scope is remebered even after  the outer function has finished its execution


def outer():
    msg = "I am outer"

    def inner():
        print(msg)

    return inner


my_fnc = outer()
my_fnc()
