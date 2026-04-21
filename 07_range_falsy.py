# Example: filtering falsy values. - this is sometimes used intentionally to remove falsy values from a list.
values = [0, 1, "", "AI", None]
for v in values:
    if v:
        print(v)
# because python removes 0, "" and None from the list, only 1 and "AI" are printed.

### range() function - generates a sequence of numbers. It can take one, two, or three arguments: start, stop, and step.
# range(stop) - generates numbers from 0 to stop-1
print(list(range(5)))  # Output: [0, 1, 2, 3, 4]
# range(start, stop) - generates numbers from start to stop-1   
print(list(range(2, 5)))  # Output: [2, 3, 4]
# range(start, stop, step) - generates numbers from start to stop-1, incrementing by step
print(list(range(0, 10, 2)))  # Output: [0, 2, 4, 6, 8] 
# range() is often used in for loops to iterate a specific number of times.
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4   
    