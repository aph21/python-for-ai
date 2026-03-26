# Higher Order Function
# We know that in python functions are known as first class objects.
# what does first class object means?
# in python, function are treated like any other values -> like intergers, strngs, or dictionary.
# this means functions can be:
# 1. assigned to any variable
# 2. can be stored into list or dictionary
# 3. can be passed as an argument to another function
# 4. can be returned from another function


# 1. Assigned to a variable


def greet(name):
    return f"Hello {name}"


# assigning a function to a variable
say_hello = greet
print(say_hello("Anjana"))
# say_hello is not calling the function, it is pointing to same function object as greet

# 2. Stored in a list


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


operations = [add, subtract, multiply]

for operation in operations:
    print(operation(10, 5))

# 10, 5, 50


# 3. Passed as an argument to another function


def apply(func, value):
    return func(value)


# here apply is a higher order function because it accepts another function(func) as an argument
# func -> a placeholder for any function we pass in
# value -> the data we want to process


def double(x):
    return x * 2


def square(x):
    return x**2


# double() and square() are regualr function

print(apply(double, 5))  # 10
print(apply(square, 5))  # 25

# Here apply receives a function as an argument and calls it. This is the foundation of Higher Order Functions.


# 4. Returned from another function:
def make_multiplier(n):  # outer function takes 'n' value
    def multiply(x):  # inner function takes 'x' value
        return x * n

    return multiply


double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15


# n is the number we want to multiply by. When we call this ( def make_multiplier(n)) n gets "remembered" inside
# a function is define inside the another function i.e def multiply(x):
# return x * n
# multiply is nested inner function, it uses n fom outer function and this is called closure(the inner function remembers the value of n)
#    return multiply   # ← no parentheses! returning the function itself

# double = make_multiplier(2)   # double is now the multiply function with n=2 locked in
# triple = make_multiplier(3)   # triple is now the multiply function with n=3 locked in


# sorted(), filter(), and map() are all Higher Order Functions built into Python.
# sorted() — takes a function as key argument
# sorted(students, key=lambda s: s["score"])

# filter() — takes a function as first argument
# filter(lambda x: x > 0, numbers)

# map() — takes a function as first argument
# map(lambda x: x * 2, numbers)


# examples
# 1. function that takes another function as an argument
def apply_operation(data: list, operation):
    """
    Apply any operation function to every item in data.

    Args:
        data: List of numbers
        operation: Any function to apply to each item

    Returns:
        New list with operation applied to each item
    """
    result = []
    for item in data:
        result.append(operation(item))
    return result


def double(x):
    return x * 2


def square(x):
    return x**2


def make_negative(x):
    #return -x


numbers = [1, 2, 3, 4, 5]

print(apply_operation(numbers, double))  # [2, 4, 6, 8, 10]
print(apply_operation(numbers, square))  # [1, 4, 9, 16, 25]
print(apply_operation(numbers, make_negative))  # [-1, -2, -3, -4, -5]

# Also works with lambda
print(apply_operation(numbers, lambda x: x + 10))  # [11, 12, 13, 14, 15]


# 2. Function that returns a function
"""
    Returns a greeting function based on language.
    
    Args:
        language: Language code ('en', 'es', 'ar')
    
    Returns:
        A greeting function for that language
    """


def make_greet(language: str):
    def greet(name: str) -> str:
        if language == "en":
            return f"Hello, {name}"
        elif language == "hi":
            return f"Namaste, {name}"
        elif language == "ka":
            return f"Namaskara, {name}"
        else:
            return f"Hi, {name}"

    return greet


# Create specific greeting functions
en_greet = make_greet("en")
hi_greet = make_greet("hi")
ka_greet = make_greet("ka")

print(en_greet("Anjana"))  # Hello, Anjana
print(hi_greet("Anjana"))  # Namaste, Anjana
print(ka_greet("Anjana"))  # Namaskara, Anjana


# strip() -> strip() removes spaces from the START and END of a string It does NOT remove spaces between words
"""
"  My name is Anjana  "
         ↓ strip()
"My name is Anjana"
          ↓ lower()
"my name is anjana"
"""

# The spaces between words stay. Only leading and trailing spaces are removed.


# example to learn the logic
# Step 1: Define the three pipeline functions


def clean(
    message: str,
) -> (
    str
):  # def -> defines the function, clean -> name of the function, (message: str) -> means function takes only one parameter called message. the :str is a type hint that tells us we can only pass string as an argument to this function. -> str -> means the function will return a string
    return message.strip().lower()


# message.strip() -> it will remove spaces from the start and end of the string
# message.lower() -> it will convert the string to lowercase
# return ssends the result back to whover called the function


def validate(
    message: str,
) -> (
    bool
):  # def -> defines the function, validate -> name of the function, (message: str) -> means function takes only one parameter called message. the :str is a type hint that tells us we can only pass string as an argument to this function. -> bool -> means the function will return a boolean value
    return len(message.split()) >= 3


# message.split -> splits the strinto list of words, t splits on whitespace.
# len() -> counts how many items are in that list (i.e words)
# >= checks if that count is greater than or equal to 3
# return -> returns the result of the check (True or False)


def add_prefix(
    message: str,
) -> (
    str
):  # def -> defines the function, add_prefix -> name of the function, (message: str) -> means function takes only one parameter called message. the :str is a type hint that tells us we can only pass string as an argument to this function. -> str -> means the function will return a string
    return f"User said: {message}"


# f"User said: {message}" -> f-string is used to format the string. it is a way to embed expressions inside string literals.

# Step 2: Raw input data
messages = [
    "  My name is Anjana  ",
    "  I want to become Agentic AI developer  ",
    "  Hi  ",
    "  I have started learning python  ",
    "  Ok  ",
]  # messages -> a variable that holds a list of strings


# Step 3: Run the pipeline
cleaned = list(
    map(clean, messages)
)  # map(clean, messages) here map applies clean function to every item in messages one by one, it returns lazy map object so to convert it into list we use list()
valid = list(
    filter(validate, cleaned)
)  # filter(validate, cleaned) here filter applies validate function to every item in cleaned one by one, it returns lazy filter object so to convert it into list we use list()
final = list(
    map(add_prefix, valid)
)  # map(add_prefix, valid) here map applies add_prefix function to every item in valid one by one, it returns lazy map object so to convert it into list we use list()

# Step 4: Print results
for message in final:
    print(message)
# for message in final: here for is a loop that iterates over every item in final one by one, it assigns each item to the variable message and then executes the code inside the loop
# print(message) -> it will print the value of message

