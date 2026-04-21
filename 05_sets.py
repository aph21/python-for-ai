#1
s = set()
s.add((1, 2))
print(s)

# what is set() ?
# A set is a collection of unique elements. It is unordered and mutable. sets uses hashing internally to store its elements. only allows hashable objects as its elements. because it uses hashing to store its elements, it can perform operations like membership testing and adding/removing elements in constant time on average.

s = {1,2,3}
print(s)

#OR
s = set([1, 2, 3])
print(s)

#############Core Properties of Sets

# 1. No duplicates allowed

s = {1,1,2,4,6,6,6,6}
print(s)
#prints {1, 2, 4, 6} because sets automatically remove duplicates.

#2. Unordered
s= {3,2,4,1,8,5}
print(s)
#prints {1, 2, 3, 4, 5, 8} because sets do not maintain any order. The elements are stored in a way that allows for efficient membership testing and adding/removing elements.

#3. Only Hashable Objects are Allowed
s = {1, "hello", (1, 2)}
print(s)
#prints {1, 'hello', (1, 2)} because all the elements are hashable. If we try to add a non-hashable object like a list, it will raise a TypeError.

#how come {1, 2} is hashable and {1,2} is not?

########SET METHODS (Important ones)
#1. add() -> adds an element to the set
s = set()
s.add(1)
s.add(2)
print(s)

#2. remove() -> removes an element from the set. If the element is not present, it raises a KeyError.
s.remove(1)
print(s)

# check memebership
print(2 in s) # True

#now goes back to first question
s = set()
s.add((1, 2))
print(s)

#first s = set() craetes an empty set.
#(1,2) are tuple
# tuple is hashable
# so it gets added successpully to the set. If we try to add a list instead of a tuple, it will raise a TypeError because lists are not hashable.

#2. 
s = set()
s.add((1, 2, [3]))
#here tuple containes a list which is not hashable, so ot raises a TypeError: unhashable type: 'list' because the tuple is not hashable due to the presence of the list.

#3
s = {1, 2, 3}
s.add(3)
print(s)

# what it prints ? {1,2,3} because set do not allow duplicates, so adding 3 again does not change the set.
#Why? because sets are designed to store unique elements, so when you try to add an element that is already present in the set, it simply ignores the addition and keeps the set unchanged.

#4
s = set()

s.add((1,2))
s.add((1,2))

print(len(s))
#what does it print?
# it prints 1 because sets do not allow duplicates, so adding the same tuple (1, 2) twice does not change the set. The length of the set remains 1 because it only contains one unique element, which is the tuple (1, 2).
#in terms of hashing and uniqueness, when you add the tuple (1, 2) to the set for the first time, it is hashed and stored in the set. When you try to add the same tuple again, it is hashed again and compared to the existing hash value in the set. Since they are the same, the set recognizes that it is a duplicate and does not add it again, keeping the length of the set at 1.
# so python set uses hashing comparision and equality check to determine if an element is already present in the set. If the hash values match and the elements are equal, it considers them duplicates and does not add them again.


#5
s = {1,2,3}

print(2 in s)
print(5 in s)
#why memebership check in sets is so fast?
# prints true for first one and false for second one
# because sets uses hashing

#6
s = {1,2,3}
s.add(True)

print(s)
#prints {1, 2, 3} because in python boolean value true is considered equal to 1. so adding true to the set does not change the set because it is already present as 1. The set doesn't allow duplicates, so it ignores the addition of true since it is considered equal to 1. Therefore, the set remains unchanged and only contains the unique elements {1, 2, 3}.