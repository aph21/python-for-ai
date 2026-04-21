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


############# LOOPS - For, while , break and continue ###############

#loops allow the programs to repeat the actions until a certain condition is met.
# In AI systems, loops power the: agenet reasing steps, retries, processing datasets, and  tool execution pipelines.

# loops reapeatedly executes a block of code untill certain condition met:
#instead of writing
print("Hello")
print("Hello")
print("Hello")  
print("Hello")  

#we can use loop
for i in range(4):
    print("Hello")


#Types of loops:
#1. For loop
#2. While loop

###for loop is used when we know the number of iterations in advance. Used when we want toiterate over a collection of items, such as a list, tuple, or dictionary. It is also used when we want to execute a block of code a specific number of times.

for item in [1, 2, 3, 4, 5]:
    print(item)

###While loops are used when we do not know the exact number of iterations we are doing. It is used when we want to repeat a block of code until a certain condition is met.
#used when repetition is depends on a condition rather than a specific number of iterations.

x = 0
while x < 5:
    print(x)
    x += 1

#The loop runs until the condition becomes False.

### Break and continue statements:
#1. Break statement is used to exit the loop prematurely when a certain condition is met.
for i in range(10):
    if i == 5:
        break
    print(i)
#2. Continue statement is used to skip the current iteration and move to the next iteration of the loop when a certain condition is met.
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)


###########

while True:
    print("running")
#True is always True, so the condition never becomes False.
#So the loop never stops unless we explicitly stop it using: break, program exit, error or an external interrupt.
#This is an infinite loop because the condition True is always true, so the loop will continue to execute indefinitely until it is manually stopped or interrupted.
# But this pattern is often used in Backend systems and agents intentionally to keep them running and responsive to incoming requests or events. In such cases, there is usually a mechanism in place to break out of the loop when needed, such as a shutdown signal or an exit condition.
#example:
while True:
    user_input = input('type "quit" to exit: ')

    if user_input == "quit":
        print("Exiting the loop.")
        break

#### Why backend systems use infinite loops?
# backend systems must always stay awake to handle requests.
# example tasks: 
# -listening for HTTP requests
# -processing messages from a queue
# -monitoring system health
# - running background workers
# - AI agents waiting for tasks

while True:
    request = wait_for_request()
    process(request)
# In this example, the backend system is continuously waiting for incoming requests. When a request is received, it processes the request and then goes back to waiting for the next one. This allows the backend system to be responsive and handle multiple requests over time without needing to restart or shut down.
#The server keeps waiting for new requests forever. 

#This is exactly how: AI agents work. They keep running and waiting for new tasks or inputs, and they process those tasks as they come in. This allows them to be responsive and available whenever they are needed. AI auto agents, for example, can keep running in the background, waiting for new tasks to be assigned to them, and they can process those tasks as they arrive without needing to be restarted or shut down.
#autonomous agents are designed to operate continuously, making them ideal for tasks that require ongoing monitoring, real-time decision-making, or handling multiple requests over time. By using an infinite loop, these agents can stay active and responsive, ensuring they can perform their functions effectively without interruption.


############ interview question:
#1
for i in [0, 1, 2]:
    if i:
        print(i)
#prints 1 and 2 because in python, the integer value 0 is considered to be falsy, while the integer values 1 and 2 are considered to be truthy. In the for loop, when i is 0, the condition if i evaluates to false, so it does not print anything. When i is 1 or 2, the condition if i evaluates to true, so it prints the value of i, resulting in the output of 1 and 2.





