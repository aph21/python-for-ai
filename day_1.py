# print("Hello, World!")
# print("I am learning python for AI and I want to become Agentic AI Developer")

# import requests

# response = requests.get("https://api.github.com")
# print(response.status_code)


# Variables
#What is variable -> it is a named reference to a value that is stored in the memory of a computer. It allows us to store and manipulate data in our programs.
#in python:
# 1) we do not declare types
# 2) Values determine the types.
# 3) Assignment used =(this isnot equality operator, it is assignment operator)

#x = 10 # this means bind the name x to the value 10 and NOT "putting 10 into x"
#y = "Anjana"
#is_student = True

#print(x)
#print(y)   
#print(is_student)


#Indentation in Python
# In python indentation is used to defined the blocks, not {} is used like other languages.
# Also this is not style it is a syntax requirement. If you do not indent properly, you will get an IndentationError.
#Incorrect Indentation = progra, crashes with an error **************

#if True:
#   print("This statement runs")


### Comments in Python
#comments are ignored by python interpreter, they are used to explain the code and make it more readable for humans.
# In python we can use # for single line comments 
# in python we dont have multi line comments but we can use triple quotes for that purpose. which creates multiline string literals


#Questions:
#1) what is the difference between
#x = 10 and  x == 10
# in x = 10 -> this done name binding, it means python craete integer object for 10  and the name x  is bound to that object
# in x == 10 -> this is equality operator, it checks if the value of x is equal to 10 and returns True or False
#evealutes whether object is referenced by the name x is equal to the integer object 10


#2
x = 10
y = x
x = 20

print(y)

#output is 0 because when we assign y = x, y is referencing the same object as x which is 10. When we change x to 20, it creates a new object for 20 and x now references that new object, but y still references the original object which is 10.


#3.
x = [1, 2]
y = x
x.append(3)

print(y)
#output is [1, 2, 3] because in this case x and y are referencing the same list object in memory. When we append 3 to the list using x.append(3), it modifies the list object that both x and y are referencing. Therefore, when we print y, it reflects the change and shows [1, 2, 3].


#4

def add_item(lst):
    lst.append(100)

my_list = [1, 2]
add_item(my_list)

print(my_list)

# output is [1, 2, 100] because when we pass my_list to the add_item function, it is passed by reference. This means that the function receives a reference to the original list object in memory. When we call lst.append(100) inside the function, it modifies the original list object that my_list references. Therefore, when we print my_list after calling the function, it reflects the change and shows [1, 2, 100].


#5
def change(lst):
    lst = [9, 9, 9]

my_list = [1, 2]
change(my_list)

print(my_list)
# output is [1, 2] because in this case, when we assign lst = [9, 9, 9] inside the change function, it creates a new list object and assigns it to the local variable lst. This does not modify the original list object that my_list references. Therefore, when we print my_list after calling the function, it still shows the original list [1, 2].


#6
def change(lst):
    lst.append(10)
    lst = [0, 0]

my_list = [1, 2]
change(my_list)

print(my_list)
#what mutates