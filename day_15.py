# Higher order function

# in python function is not just a set of instructions, IT is also a VALUE - just like number or string
# a function can be stored in a variable -> this is what "FIRST CLASS OBJECT" means

# a function is called HOF (higher order function) if it does atleast one of these two:
# 1. takes another function as an input (argument)
# 2. returns a function as an output
# when we pass a function to another function then receiving function becomes HOF.


def apply(func, value):
    return func(value)


def double(x):
    return x * 2


result = apply(double, 5)
print(result)

## KEY RULE : when passing a function as an argument, NO PARANTHESES -> double NOT double()

# Why do we need HOF?
# HOF helps us write flexible, reusable and modular code.
# They are the foundation of functional programming.

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

# One HOF (apply), three different behaviors — just by swapping the function you pass in. This is the power of HOFs — flexible, reusable code


# A HOF can also build and return a new function


def make_multiplier(n):
    def multiplier(x):
        return x * n

    return multiplier


double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))
print(triple(5))

# in python -> 3 built in HOF present
# 1. map() -> transforms every item
# 2. filter() -> keeps only item that passes a test
# 3. sort() -> sorts the items using custom rule

# 1. map -> syntax: map(function, iterable)

numbers = [1, 2, 3, 4, 5]


def double(x):
    return x * 2


result = map(double, numbers)
print(list(result))

# map applies the function to every item and returns a map object (iterator)
# we convert it to list to see the result

# 2. filter -> syntax: filter(function, iterable)
# function must return True or False

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_even(x):
    return x % 2 == 0


result = filter(is_even, numbers)
print(list(result))

# filter keeps only items for which the function returns True

# 3. sort -> syntax: sort(iterable, key=function)

numbers = [3, 1, 4, 1, 5, 9, 2, 6]

result = sorted(numbers)
print(result)

# sort can also take a key function

words = ["apple", "banana", "cherry", "date"]

result = sorted(words, key=len)
print(result)
