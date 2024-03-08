# marks = [94.3, 87.5, 72.6, 45.9, 63.4]
# print(marks)
# print(type(marks))
# print(len(marks))

# # slicing
# slice = marks[1:4]
# print("slice : ", slice)
# slice2 = marks[-3:-1]
# print("slice2 : ", slice2)

# Additional methods for list:
# list.append(element)
# list.sort() # ascending
# list.sort(reverse = True) # descending
# list.reverse()
# list.insert(idx,el)
# list.remove(element)
# list.pop(idx)

# movies = []

# a = input("Enter movie1 : ")
# b = input("Enter movie2 : ")
# c = input("Enter movie3 : ")

# movies.append(a)
# movies.append(b)
# movies.append(c)

# print(movies)

# Check palindrome
list = [1, "abc", "abc", 1]
pallist = list.copy()
pallist.reverse()

if(list == pallist):
    print("List is palindrome")
else:
    print("List is not palindrome")