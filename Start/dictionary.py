# # Dictionary is similar to object.
# # Unordered, mutable, keys are always unique

# # Empty dict:
# collection = {}
# print(collection)
# print(type(collection))

# info = {
#     "name": "Jane",
#     "subject": ["python", "js"],
#     "topics" : ("dict", "set"),
#     "age" : 22,
#     "is_adult" : True,
#     "marks": 88.7,
#     12.99: 89
# }

# print(info)
# print(info["name"])

# # Nested dictionary
# student = {
#   "name": "Tanu",
#   "subjects": {
#     "python" : 90,
#     "js": 79
#   }
# }

# print(student["subjects"])
# print(student["subjects"]["python"])

# # Dict Methods
# print(info.keys())
# print()
# print(info.items())
# print()
# print(info.values())
# print()
# print(info.get("name"))
# print()
# info.update({"city":"Pune"})
# print(info)

# prac = {}
# prac["cat"] = "a small animal"
# prac["table"] = ["a piece of furniture", "list of facts and figures"]

# print(prac)
# print(type(prac))

# marks = {}

# x = int(input("Enter Phy : "))
# marks.update({"Phy" : x})

# x = int(input("Enter Eng : "))
# marks.update({"Eng" : x})

# x = int(input("Enter Maths : "))
# marks.update({"Maths" : x})

# print(marks)