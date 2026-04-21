a = [1, 2, 3]
b = a
a = [4, 5, 6]
print(b)
#prints [1,2, 3] because b is still referencing the original list that a was referencing before it was reassigned to a new list.

a = [1, 2, 3]
b = a
a.append(4)
print(b)
# prints [1,2,3,4], because a and b are referencing the same list object in memory. so when we append (i.e mutation) the list that a is referecing, it also affects the b list because it is referencing the same list object.

########## LIST v/s TUPLE ############
# List -> mutable sequence
lst = [1,2,3]
lst.append(4)
print(lst) # prints [1,2,3,4], because we can change list objects by adding or removing elements. this means Mutation is possible with lists.

#Tuple -> immutable sequence
tup = (1,2)
tup.append(3) #AttributeError: 'tuple' object has no attribute 'append'
#why? because tuples are immutable, once the tuple is created we cannot change its content. we cannot add or remove elements from a tuple, which is why we get an AttributeError when we try to call the append method on a tuple.

#######Tuple has no mutation methods.###########


# Lists -> Designed for dynamic resizing. Store extra space to accomodate the future growth. have overhead for mutation operations like append, insert, remove etc. because they need to manage the extra space and maintain the order of elements.
# Tuples -> Designed for immutability. do not store extra space for future growth.
# tuples have fixed size and more efficient memory usage. # tuples are less more and more faster

#Why Tuples Are Useful in Backend / AI Systems

# 1. Immutable configuration. -> in AI systems, immutability = safety. 
#2. Dictionary keys - tuples are hashable and  lists are not. So we can use tuples as keys in dictionaries, which is useful for storing and retrieving data based on multiple attributes.You cannot use a list as a dictionary key.
# 3. Structured data return - function often return multiple values as tuples, which is a convenient way to group related data together. For example, a function that processes an image might return a tuple containing the processed image and some metadata about the processing.
# 4. Performance - tuples can be more memory efficient and faster than lists, especially when dealing with large datasets. In AI systems, where performance is critical, using tuples can help optimize memory usage and speed up data processing.


#########Exercises:
t = (1, 2, [3, 4])
t[2].append(5)

print(t)
#print (1, 2, [3, 4, 5])
# because the tuple is immutable, since it contains a mutable list as on of its elements, so we can modify the list inside the tuple, but we cannot change the structure of the tuple itself. Therefore, we can append 5 to the list [3, 4] which is an element of the tuple, resulting in (1, 2, [3, 4, 5]).
#this called Shallow immutability, because the immutability applies to the tuple itself, but not to the mutable objects inside it. If we try to change the structure of the tuple, such as adding or removing elements, we will get an error. But we can modify the mutable objects inside the tuple without any issues.


#####Tuple immutability applies to the tuple structure, not to the objects inside it.####


# what happens if 
t = (1, 2, [3, 4])
t[2] = [5, 6]
print(t)
# TypeError: 'tuple' object does not support item assignment
#because it cause the modify of the tuple structure which is not allowed since tuples are immutable



a = (1, 2, 3)
b = (1, 2, 3)

print(a is b)
#false because is operator checks for identity, not equality. In this case a and b are two dfferent tuple objects in memory, even though they have the same content. Therefore, a is b evaluates to False because they are not the same object in memory. If we want to check for equality of content, we should use the == operator instead, which would return True in this case since a and b have the same values.
# but in CPython it may print TRUE
#because python may intern small immutable objects
#Tuple literals inside the same code block can be optimized
#The interpreter may reuse the same tuple object

#####It may print True in CPython due to constant interning optimizations, but identity comparison for tuples is not guaranteed and should not be relied upon. Always use == for value comparison.###