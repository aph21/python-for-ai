#what is dictionary in python?
# it is datastructure that stores key-value pairs. It is also known as associative array or hash map in other programming languages. In a dictionary, each key is unique and maps to a specific value. The keys can be of any immutable data type, such as strings, numbers, or tuples, while the values can be of any data type.
#Dictionaries are mutable, meaning you can change their contents after they have been created. They are commonly used for storing and retrieving data based on keys, making them a powerful and flexible data structure in Python.
#key → value

user = {
    "name": "Anjana",
    "age": 24,
    "role": "AI Engineer"
}
print(user["name"])

###### Properties:
#1. Key value storage
#2. Keys must be hashable
#3. Values can be anything
#4. Unique keys
#5. Mutable
#6. fast lookups


#example:
#1.
d = {}

d[1] = "integer"
d[True] = "boolean"

print(d)
#prints {1: 'boolean'} because in python, the boolean value True is considered equal to 1. So when you assign a value to the key 1 and then assign another value to the key True, it overwrites the previous value associated with the key 1. As a result, the dictionary ends up with only one key-value pair, which is {1: 'boolean'}.

#2
d = {}

d[False] = "A"
d[0] = "B"

print(d)
# prints {False : 'B}, because in python, the boolean false is considered to be equal to 0. So when d[False] = "A" dictionary become {False : 'A'} internally python calculates the hash value of False and stores the value "A" at that hash location. Then when d[0] = "B" is executed, it calculates the hash value of 0, which is the same as the hash value of false, so python compares the keys and finds that they are equal. As a result, it updates the value at that hash location to "B", effectively overwriting the previous value "A". Therefore, the final dictionary contains only one key-value pair, which is {False: 'B'}.

#3
d = {}

d[(1,2)] = "tuple"
d[[1,2]] = "list"

print(d)
#here we get error as TypeError: unhashable type: 'list'. because in python, lista are mutable and cannot be used as keys in a dictionary. When you try to use a list as a key, it raises a TypeError indicating that the type is unhashable. On the other hand, tuples are immutable and can be used as keys without any issues. Therefore, the first assignment d[(1,2)] = "tuple" works fine, while the second assignment d[[1,2]] = "list" raises an error.
'''
| Type  | Hashable                  | Can be dict key   |
| ----- | --------------------------| ------------------|
| int   | ✅                        | ✅               |
| float | ✅                        | ✅               |
| str   | ✅                        | ✅               |
| bool  | ✅                        | ✅               |
| tuple | ✅ (if contents hashable) | ✅               |
| list  | ❌                        | ❌               |
| set   | ❌                        | ❌               |
| dict  | ❌                        | ❌               |
'''


########### CONTROL FLOW STATEMENTS

x = 0

if x:
    print("A")
else:
    print("B")

#prints B because in python, the integer value 0 is considered to be falsy. In an if statement, a falsy value is treated as false, so the else block is executed, resulting in the output "B".

x = []

if x:
    print("A")
elif x == []:
    print("B")
else:
    print("C")
#prints B because in python, an empty list is considered to be falsy. In the if statement, the condition x evaluates to false, so it moves to the elif statement. The condition x == [] evaluates to true since x is indeed an empty list, so the code block under the elif statement is executed, resulting in the output "B".

x = None
if x:
    print("A")
elif x == None:
    print("B")
elif x is None:
    print("C")
else:
    print("D")
#it prints B because in python, the value None is considered to be a falsy value. In the if statement, bool(x) becames bool(None) which is False, so it moves to first elif statement. that condition x == None evalutes to be true, since x is None, so code block under first elif statement is executed, resulting in the output "B". The second elif statement is not evaluated because the first elif condition is already satisfied.