# # Sets is the collection of the unordered items.
# # Each element in the set must be unique and immutable(values). But set itself is mutable.
# # We cannot store list and dic inside sets.
# # We can store boolean, int, float, str and tuple

# set1 = {1,2,2,"A","B","A","B","X","Z",3,5,6,6,7,8,1}

# print(set1)
# print(type(set1))
# print(len(set1))

# # create empty set
# collection = set()
# print(collection)
# print(type(collection))

# # Set methods
# collection.add(1)
# collection.add("B")
# collection.add((True,6.9,7))
# collection.add(2)
# collection.remove(2)

# print(collection)
# # collection.pop() # removes any random value
# # collection.clear()

# set2 = {"A", "B", "C", "D", "E"}
# u = set1.union(set2)  # returns collection of both sets
# i = set1.intersection(set2) # returns common elements from both sets

# print(u)
# print(i)

# prac = {"python", "js", "c++", "java", "python", "js", "c++", "java", "c"}

# print(prac)
# print(type(prac))
# print(len(prac))

# How to print 9 and 9.0 as different values in set?
values = {9, 9.0}
print(values) # won't work

values = {9, "9.0"}
print(values) # Possible solution 1: change the data type

values = {
  ("float", 9.0),
  ("int", 9)}
print(values) # Possible solution 2: use built-in data type