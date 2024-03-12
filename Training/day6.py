# Tuple:

# Similar to dict and list to store more than one element in a single variable.
# Can store different data type
# Create tuple ()
# Access element by index
# Immutable

# x = 1,20,33,43,5,6,7,8,5
# print("Tuuple : ", x)
# print(type(x))

# Creating empty tuple
# t = ()

# help(tuple)
# there is only two pre-defined function/method for tuple i.e., count() and index()

# print(max(x))
# print(min(x))
# print(len(x))
# print(x[2])
# print(x[int(input("Enter Index : "))])
# print(x.count(int(input("Enter num to search : "))))

# name = "sd","ew","ret","fd","wq"
# print(name)
# new_name = name
# print(new_name)

# name = name + ("oi", "yo")
# print(name)
# print(id(name))

# li = ["sd","ew","ret","fd","wq"]
# name = name + tuple(li)
# print(name)
# print(id(name))

# Insert new value at a particular value
# name = name[:int(input("Enter index : "))] + (input("Enter name to insert : "),) + name[:int(input("Enter index : "))]
# print(name)
# print(id(name))

# Converting tuple as list
# print("List : ", list(name))
# print("Reversed List : ", tuple(reversed(name)))

# li = ["sd","ew","ret","fd","wq"]
# name = ["sd","ew","ret","fd","wq"]

# res = [(li,name) for na, te in zip(li,name)]
# print("Paired list : ", res)
# new_res = tuple(res)
# print("List of Tuple : ", new_res)

# Set
# special data type like list, dict, tuple, etc.
# can store more than one element
# contains only unique value
# To create set{} or set()
# Can perform union of set, intersection of set, difference of two sets
# No index
# The values are shuffled every time

# help(set)
# colorset = set()
# li = ["red", "green", "yellow", "blue", "red", "yellow"]
# print("List : ", li)
# print("Set : ", set(li))
# colorset = set(li)
# colorset.update(["Orange", "White"])
# print(colorset)
# colorset.discard(input("Enter the color to remove : "))
# print(colorset)

# search = input("Enter color of search : ")
# print("Available" if search in colorset else "Not Available")

# Regular Expression (regex)
'''
Used to find specific pattern/sequence in strings
'''

# escape method adds a \ before each special character and space
# import re # re - module
# print(re.escape(input("Enter a qualified website : ")))
# sentence = re.escape(input("Enter a sentence : "))
# pattern = input("Enter pattern to search : ")
# match = re.search(pattern, sentence)

# if match:
#   print("Found at :", match.start(), " index")
# else:
#   print("Not Found")

# To find only capital and small letters
# pattern = '[A-Za-z]+'
# match = re.findall(pattern, sentence)

# To find any particular symbol 
# pattern = r'[.?\-]+'
# match = re.findall(pattern, sentence)

# To find any particular digit 
# pattern = r'\d{3}'
# match = re.findall(pattern, sentence)

# To find any alpha numeric character 
# pattern = r'b[pP]\w'
# match = re.findall(pattern, sentence)



