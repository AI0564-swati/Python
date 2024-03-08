# # Tuple is immutable just like string and opposite to list

# tuple = (45,89,12,90, 56)
# print(type(tuple))
# tup = (1,) # This is how we write a tuple if there is only one value in it. If we don't use `,` it will treat it as an integer.
# print(tup)
# print(type(tup))
# notup = (1)
# print(notup)
# print(type(notup))

# # Tuple method : 
# tup.index(el)
# tup.count(el)

grade = ("C", "D", "A", "A", "B", "B", "A")
print(grade.count("A"))

gradeList = ["C", "D", "A", "A", "B", "B", "A"]
gradeList.sort()
print(gradeList)