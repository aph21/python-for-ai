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