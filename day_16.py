# List & Dictionary Comprehensions

# PROBLEM THAT COMPREHENSION SOLVE:
# before comprehension was invented we had to write like this - 
#old way - verbose and cluttered
numbers = [1, 2, 3, 4, 5]
squares = []

for n in numbers:
    squares.append(n ** 2)

print(squares)
# output: [1, 4, 9, 16, 25]

# this above code works but it takes 4 lines to do a 1 thought operations
# So Comprehension let you express the same logic in a single line with no sacrifice in clarity or readability

#List comprehension - Anatomy
# result = [expression for item in iterable]
# here expression ->  what to produce for each item
# for item ->  the loop variable
# iterable -> the list, tuple, string, or other sequence you are looping over
#result -> new list built from expressions

#re writing the example:

numbers = [1, 2, 3, 4, 5]

squares = [n ** 2 for n in numbers]

print(squares)
# output: [1, 4, 9, 16, 25]

#same result. only one line. No mutation of an external list.  No .append() calls. 


#LIST COMPREHENSION WITH FILTER
# Syntax -> result = [expression for item in iterable if condition]
# condition -> optional filter that determines whether an item is included in the new list

#example:
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = [n for n in number if n % 2 == 0] #Give me n for every n in numbers, but only if n is even.

print(evens)
# output: [2, 4, 6, 8]


#List Comprehension With if-else (Transformation)
# when you want to transform every item 9not filter, put the if-else in expression:
# Syntax: result = [value_if_true if condition else value_if_false for item in iterable]

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

labels = ["Even" if n % 2 == 0 else "Odd" for n in num]

print(labels)

### important ###
# if after the for -> filter
# if before the for -> transform


##Nested List Comprehension
# can loop over multiple iterables

matrix = [[1,2,3], [4,5,6], [7,8,9]]

flat = [num for row in matrix for num in row]
print(flat)
# output: [1, 2, 3, 4, 5, 6, 7, 8, 9]


#Dictionary Comprehension — Same Idea, Different Output
# instead of building list here we build dict
#Sytntax : result = {key_exp: value_exp for item in iterable}

words = ["agent", "token", "model"]

word_lengths = {word : len(word) for word in words}
print(word_lengths)
# output: {'agent': 5, 'token': 5, 'model': 5}


#with filter:
scores = {"Alice": 85, "Bob": 45, "Cherry": 92, "Don": 32}

passed = {name: score for name, score in scores.items() if score >= 60}
print(passed)