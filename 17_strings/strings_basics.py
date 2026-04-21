# String - is sequence of characters stored in memory
# In Python string is immutative
# Type -> str

##EVERY SINGLE THING LLM RECEIVES AND RETURNS IS A TEXT - A STRING

########1. Creating strings
#single quotes
s1 : str = 'hello' # string is defined using single quotes and : str means type hint

#double quotes
s2 : str = "hello"

# triple quotes - for multi line srings (imp for prompts)
prompt : str = """
you are an AI assistant.
Your job is to answer questions clearly.
"""
#this is how you write system prompts in LLM applications.

# Raw string — backslashes are literal (used in file paths, regex)
path: str = r"C:\Users\aph\documents"


########2. String Immutability -The core rule
# once a string is created, it cannot be changed.
# if you try to change it -> it will create new string in memory
text:str= "Hello"
text[0] = "h" #TypeError: 'str' object does not support item assignment
#so you cannot modify a character in place. you alwasy create new string.
text: str = "hello"
new_text: str = "H" + text[1:] #what is text[:1]? -> it is a slice of the string 'text' from index 1 to the end
print(new_text) #output: Hello

# memory mode -> text still points to "hello" and new_text points to brand new object "Hello". The original is untouched.


########3. Indexing and Slicing
#strings are zero indexed sequences.
s: str = "python"
print(s[0]) #output: p
print(s[1]) #output: y
print(s[2]) #output: t
print(s[3]) #output: h
print(s[4]) #output: o
print(s[5]) #output: n
print(s[-1]) #output: n
print(s[-2]) #output: o
print(s[-3]) #output: h
print(s[-4]) #output: t
print(s[-5]) #output: y
print(s[-6]) #output: p

print(s[0])    # P
print(s[-1])   # n  (last character)
print(s[2:5])  # tho  (start inclusive, end exclusive)
print(s[:3])   # Pyt
print(s[3:])   # hon
print(s[::-1]) # nohtyP  (reverse — a common trick)

#Slice syntax: s[start:stop:step]
# start -> inclusive
# stop -> exclusive
# step -> increment (default is 1)


############ 4. Essential string methods

text : str = " Hello, World! "

#case
print(text.upper()) #" HELLO, WORLD! " -> returns the uppercase version of the string
print(text.lower()) #" hello, world! " -> returns the lower case version of the string
print(text.title()) #" Hello, World! " -> returns the title case version of the string

# Whitespace - CRITICAL for cleaning LLM outputs
print(text.strip()) #"Hello, World!" -> removes leading and trailing whitespace
print(text.lstrip()) #"Hello, World! " -> removes leading whitespace
print(text.rstrip()) #" Hello, World!" -> removes trailing whitespace

#search
print(text.find("World")) # -> returns the index of the first occurrence of the substring "World"
print(text.find("Python")) # -> returns -1 because "Python" is not in the string
print(text.count("l")) # -> returns the number of occurrences of the substring "l"
print(text.replace("World", "Python")) # -> replaces the substring "World" with "Python"

#Check
print(text.strip().startswith("Hello")) # -> returns True if the string starts with "Hello"
print(text.strip().endswith("!")) # -> returns True if the string ends with "World"
print(text.strip().isnumeric()) # -> returns True if the string is numeric
print(text.strip().isalpha()) # -> returns True if the string is alphabetic
print(text.strip().isalnum()) # -> returns True if the string is alphanumeric


########## 5. Split and Join - IMPORTANT

