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


#3
students = [
    {"name": "Ahmed", "score": 85},
    {"name": "Sara", "score": 92},
    {"name": "Ali", "score": 78},
    {"name": "Zara", "score": 95},
]

sorted_students = sorted(students, key=lambda s: s["score"], reverse=True)

for student in sorted_students:
    print(f"{student['name']}: {student['score']}")

#output is:
#Zara: 95
#Sara: 92
#Ahmed: 85
#Ali: 78
#Why?
# here sorted() sorts by the score value (95,92,85,78) in descending order (reverse=True)
# lambda s: s["score"] tells sorted() to look at the "score" value inside each student dictionary for sorting.
# the for loop just prints the sorted list in a readable format.


#4
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)

#output is: [2,4,6,8,10]
#why
#1. filter() goes through every item in list and keeps only item that pass the test and returns True.
# if true -> keep it if False -. throw it.
# lambda x: x % 2 == 0 -> here x % 2 gives the remainder when dividing  x by 2. == will check if the remainder is really eaqual to zero or not, if its equal to zero then that number is even.
# Why wrap it with list()? -> wrapping filter object with list() will forces it to run and collect all the results into a proper list instead of filter object

#5
prices = [100, 250, 80, 400, 150, 320]

discounted = list(map(lambda price: price * 0.9, prices))

print(discounted)
#output is: [90.0, 225.0, 72.0, 360.0, 135.0, 288.0]
#why
#map() applies a function to every item in a list and returns a new list with the results.
#lambda price: price * 0.9 -> takes a price and returns 90% of it (10% discount).
#list() converts the map object into a list.

#6.
data = [
    {"name": "GPT-4", "cost": 30, "quality": 95},
    {"name": "GPT-3.5", "cost": 2, "quality": 75},
    {"name": "Claude-3", "cost": 15, "quality": 90},
    {"name": "Gemini-Pro", "cost": 1, "quality": 80},
]

budget = 20

affordable = list(filter(lambda m: m["cost"] <= budget, data))
best = sorted(affordable, key=lambda m: m["quality"], reverse=True)[0]

print(f"Best model within ${budget} budget: {best['name']} (Quality: {best['quality']})")

#ouput : Best model within $20 budget: Claude-3 (Quality: 90)
#why?
#1. filter() -> keeps only affordable models so here it throws out {"name": "GPT-4", "cost": 30, "quality": 95}
# 2. sorted() -> rank the afoordable list  items by their quality, so there we get [Claude-3 (90), Gemini-Pro (80), GPT-3.5 (75)]
# 3. [0] -> means it picks the first item i.e the best
# i.e {"name": "Claude-3", "cost": 15, "quality": 90}
#then prints it using print statement and f string