# 1
def change(lst):
    lst.append(9)
    lst = [4, 5]


my_list = [1, 2]
change(my_list)
print(my_list)

# Which line caused mutation?
# the line lst.append(9) caused mutation because it modifies the original list object that my_list references.

# Which line caused rebinding?
#  The line lst = [4,5] caused rebinding because it creates a new list object and assigns it to the local variable lst, which does not affect the original list and does not change the reference of my_list.

# Why does my_list not become [0, 0]?
# my_list does not become [0, 0] because the line lst = [0, 0] creates a new list object and assigns it to the local variable lst, which does not affect the original list that my_list references. The original list remains unchanged as [1, 2].


###Data Types
# int, float, str, bool
# in python everything is an object, including data types. When we create a variable and assign it a value, we are creating an object in memory and the variable name is a reference to that object.
# each has a type, a method, immuatbility rules and Memory behaviour.

x = 10
print(type(x))  # <class 'int'>, this shows that x is an integer object

##### IMPORTANT: Immutability
# int. float, bool, str are immuatable, means they cannot be mutated but Operations can create new Objects.

x = 5
x = x + 1
print(x)
# here this doesn't modify 5 (since it is immutable), instead it creates a new object for 6 and rebinds x to that new object. The original object 5 remains unchanged in memory and x now references the new object 6.)


#####Boolean Trap
bool(0)  # False
bool("")  # False
bool([])  # False
bool(None)  # False
# Everything else → True
# This is important to understand because it can lead to unexpected behavior if you are not aware of how different values are evaluated in a boolean context. For example, if you have a condition that checks if a list is empty, it will evaluate to False if the list is empty and True if it contains any elements.


### EXERCISES

# 1
print(
    True + 1
)  # prints 2 because in Python, the boolean true value is treated as 1 and the boolean false value is treated as 0 when used in arithmetic operations. Therefore, True + 1 is equivalent to 1 + 1, which results in 2.
# IN python bool is a subclass of int, so True and False can be used in arithmetic operations as if they were integers.

print(
    isinstance(True, int)
)  # prints True because in Python, the bool type is a subclass of the int type. This means that True and False are considered instances of both bool and int. Therefore, isinstance(True, int) returns True, indicating that True is indeed an instance of the int class.


print(
    type(True)
)  # prints <class 'bool'> because the type of True is bool, which is a subclass of int. Even though bool is a subclass of int, it is still a distinct type, and the type function will return <class 'bool'> when called with True as an argument.

print(
    bool("False")
)  # prints True because in Python, any non-empty string is considered truthy, meaning it evaluates to True in a boolean context. The string "False" is a non-empty string, so when we call bool("False"), it returns True.

print(bool(" "))
# prints True because in Python, any non-empty string is considered truthy, meaning it evaluates to True in a boolean context. The string " " (a space) is a non-empty string, so when we call bool(" "), it returns True. Also " " has a length of 1, which is greater than 0, so it is not considered as empty stringand thus evaluates to True.

print(
    bool([])
)  # false because in python, an empty list is considered falsy meaning it evaluates to False in a boolean context. When we call bool([]), it returns False because the list is empty and does not contain any elements.
print(
    bool([0])
)  # prints true because in python, a list that contains any elements is considered truthy, meaning it evaluates to True in a boolean context. The list [0] contains one element (the integer 0), so when we call bool([0]), it returns True. Even though the element is 0, which is falsy on its own, the list itself is not empty and therefore evaluates to True.

print(bool(None))
# prints False, because in python, NNone is considered as falsy. when we call bool(None), it returns False because None represents the absence of a value and is treated as False in boolean contexts. None is often used to indicate that a variable has no value or that a function does not return anything.
# what is none conceptually? None is a special constant in Python that represents the absence of a value or a null value. It is often used to indicate that a variable has no value, that a function does not return anything, or to signify the end of a list or other data structure. None is a singleton object, meaning there is only one instance of None in the entire Python runtime, and it is of type NoneType.
# how it is extremely important in backend and AI Systems? None is extremely important in backend and AI systems for several reasons:
# 1. in API responses
# 2. Optional fields (LLM systems)

x = None
print(
    x == False
)  # False because in python, None and False both are distinct objects and they are not equal to each other. so when we compare None and False using equality operator (==), it returns False because they are not the same value. None means absence of value, while False is boolean value repreresenting falsehood. They are different concepts and thus not equal.
print(
    x is False
)  # it gives false  beacuse x points to None and False is boolean object so they are completely differet in memory and thus x is False returns False. The is operator checks for identity, meaning it checks if both operands refer to the same object in memory. Since None and False are different objects, x is False evaluates to False.


a = 256
b = 256
print(a is b) # True
# Because python interns small integers ( from -5 to 256 -> these are cached and resued by python internally)
# so when we write 256 so it doesn't create new object each time and it reuses the same cached object.
#same object -> identity is True

a = 257
b = 257
print(a is b)# Sometimes it prints true and sometimes false based on implementation and context
#because integers outside the range of -5 to 256 are not interned by Python, so when we create two variables a and b with the value 257, they may refer to different objects in memory. Therefore, a is b may return False because they are not the same object, even though they have the same value. However, in some implementations of Python or under certain conditions, it is possible that small integers outside the range are also interned, which could lead to a is b returning True. This behavior can be implementation-dependent and should not be relied upon.# so professional NEVER use is operator for Numeric comparision. So correct way is to use == for value comparison and is for identity comparison.

### Use is only for
#NONE
#True/ False
#checking identity intentionally
####NEVER use is for STRing, int, float, bool comparision because of the interning and caching behavior of Python which can lead to unexpected results when using is for value comparison. Always use == for comparing values of these types to ensure correct behavior.

x = "hello"
y = "hello"

print(x is y) # True, in CPython it will mostly print true.
#why? because python often interns small strings, especially shrt strings, identifiers and string literals inside same code block.
#both x and y are same object in memeory.
x = "hello world"
y = "hello world"

print(x is y)
# it may print True or false based on implementation and context because longer strings are not always interned by Python, so x and y may refer to different objects in memory. Therefore, x is y may return False because they are not the same object, even though they have the same value. However, in some implementations of Python or under certain conditions, it is possible that longer strings are also interned, which could lead to x is y returning True. This behavior can be implementation-dependent and should not be relied upon. Always use == for comparing string values to ensure correct behavior.

###Using is for string comparison is a professional mistake.

#best 3 use case of using is in production Python:
# 1. checking for None
# 2. checking for True/False
# 3. checking for identity intentionally