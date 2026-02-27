##### Hashing

#A has is a fixed-size number that is generated from an object
# python used this number to: Store the objects efficiently and to look them up quickly.

print(hash("Hello"))
print(hash(123))
#each produces an integer that is unique to the object
# That integer is object's has value.
# The hash value is used to determine the location of the object in memory.

## What Does “Hashable” Mean?
# An object is hashable if:\
# 1. it  has a hash value that never changes during its lifetime
# 2. it can be compared to other objects.

####### simply -> if it can be safely used as a dictionary keys then it is hashable ########

###### Why Mutability Matters 

# Mutable objects cannot be hashable (usually)
# because, if the object changes then its hash value will also change. And because of it dictionary will lose track of it.

##example of disaster scenario

key = [1, 2]
my_dict = {key : "value"}

# modifying the key
key.append(3)

# dictionary cannot find the key like before it can't find it because the hash value of the key has changed

# will get error -> TypeError: unhashable type: 'list'


### Why tuples are hashable?
# because they are immutable unline lists, their content cannot be changed. So their hash stays stable.

d = {}
d[(1, 2)] = "hello"


#2
d = {}
key = (1, 2, [3])
d[key] = "value"
# it crashes because tuples are hasble only if their ALL contents are hashable. In this case the list [3] is not hashable, so the tuple is not hashable.