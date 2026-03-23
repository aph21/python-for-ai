######Lambda Function
#sometimes we need a small, simple, throwaway function that we will be using one or twice
#Lambda functions are small, anonymous function that has no name ( not def), has one expression only(no mutliple statements), returns automatically and can be used in inline.
#SYNTAX:
## lambda arguments: expression
#lambda here indicates the keyword, arguments means inputs (parameters), pression means what it computes and returns automatically

#regular function
def add(a,b):
    return a+b

#same function using LAMBDA
lambda a,b : a+b
#expression after : is automatically returned. we never write return in lambda function


###How to use Lambda

##OPT 1: Assign it to a variable
add = lambda a,b : a+b
result = add(3,5)
print(result)

##OPT 2: use it directly inline

result = (lambda a,b : a+b)(3,5)
print(result)


### Lambda with different cases
# with no arguments
greet = lambda : "Hello I'm Anjana Hegde"
print(greet())

# with one argument
square = lambda x: x ** 2
print(square(5))

# Multiple arguments:
multiply = lambda a, b: a * b
print(multiply(4, 5))   # 20

# With condition (ternary):
check = lambda x: "positive" if x > 0  else "negative"
print(check(-11))
print(check(0))
print(check(2))



## Important Limitation
# Lambda functions can have only one expression
# they cannot contain: 
    # Multiple lines of code
    # Loops
    # if/else block -> they can only contain ternary
    # return statement
    # variable assignments


## where Lambda is actually used? -> with Higher order functions


########### Interview Exercises

#1.
square = lambda x: x ** 2
print(square(4))
print(square(7))
#16
#49
#why ?
#here lambda means keyword, x: means input and x ** 2 is an expression or it tells what it computes.
#lambda x: x ** 2 is just a compact way of saying "give me a number, I'll return its square." Same logic as a regular function, just shorter.


#2.
numbers = [5, 2, 8, 1, 9, 3]

sorted_numbers = sorted(numbers, key=lambda x: x)

print(sorted_numbers)
#output is: [1,2,3,5,8,9]
#Why?

#How sorted() works? -> it is a built in python function. It takes any collection (like a list) and returns a brand new sorted version of it.
# What does key paramter do? -> it tells sorted() how to decide the order. It expects a function sorted() will call this function on every item in the list and use the return values to sort.
# In this case, lambda x: x is a function that takes an item x and returns x itself. So sorted() sorts the list in ascending order.
# If we had written lambda x: -x, it would sort the list in descending order.