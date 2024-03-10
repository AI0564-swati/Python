# Dictionary, Set and Tuple

# pre-defined functions
# - max, min, len, sorted
# module functions
# - shuffle
# special datatype functions
# - Li.sort(), Li.reverse()
# user defined functions

# Dictionary is collection of stored data in key-value pairs 
# Similar to object
# Immutable
# Key should be unique

# help(dict)

# __eq__ - method :within a class
# update() - function : out of class

# Creating empty dict
# d1 = dict()
# di = { }

# di.update({'Name' : 'Swati'}) # adding key and value in dic
# di.update({'Designation' : 'Developer'}) # adding another element in dic
# print(di)

# dynamically
# di = { }
# no = int(input("Enter No : "))
# for i in range(no):
#   di.update({input("Enter Key" + str(i+1) + ":"):input("Enter Value" + str(i+1) + ":")})
# print(di)

# generate automatic key and value
# generate OTP in 4 digits and store as a value
# di = { }
# no = int(input("Enter No : "))
# for i in range(no):
#   di.update({(i+1):(i+1)*(i+1)})
# print(di)

# import random

# di = {}
# no = int(input("Enter the number: "))

# for i in range(no):
#     otp = random.randint(1, 10)
#     di[i+1] = otp

# print("Generated OTPs:", di)

# List keys and value seperaately: 
# print(di.keys())
# print(di.values())

# delete a particular key
# del di[int(input("Enter the key you want to delete : "))]
# print("After deleting : ", di)

# To clear all and get empty dictionary
# di.clear()
# print("After clearing the dict", di)

# di = {x: x**x for x in range(1, int(input("Enter No : ")) + 1)}
# print(di)

# from collections import OrderedDict
# di = {}
# no = int(input("Enter no : "))
# for i in range(no):
#   di.update({random.randint(1,no+1) : random.randint(1000,10000)})
# # print(di.items())
# print("Original dict : ", di)

# for k in sorted(di):
#   print("Sorted dict : ", k, di[k],end=" ")

# print()

# for k in reversed(di):
#   print("Reversed dict : ", k, di[k],end=" ")

# newdi = OrderedDict(di.items())
# for k in newdi:
#   print(k, newdi[k])

# Appending list in a dict
# Li = []
# di = {}
# no = int(input("Enter No : "))
# for i in range(no):
#   Li.append(input("Enter Name : "))
# di.update({"Emp Name List" : Li})
# print(di)
    
# give dept names as keys and add more than one names based on department as a value

# depts = {}
# no = int(input("Enter no: "))

# for k in range(no):
#     department = input(f"Enter department: ")
#     num_employees = int(input(f"Enter no of employees: "))
#     Li = []
#     for i in range(num_employees):
#         employee_name = input(f"Enter employee name: ")
#         Li.append(employee_name)
#     depts[department] = Li

# print(depts)

# Nested dictionary
# no = int(input("Enter no : "))
# d1 = {}
# for i in range(1, no+1):
#   print()
#   k = input("Enter product name : " + str(i) + ":")
#   Qty = int(input("Enter Qty : "))
#   Price = int(input("Enter price : ")) 
#   d1.update({k:{'Qty' : Qty, 'Price' : Price}})
# print(d1)
# print()
# GT = 0
# Q = 0
# P = 0
# for key1, val1 in d1.items():
#   print("\n", key1)
#   if type(val1) is dict:
#     for key2, val2 in val1.items():
#       print(key2,":",val2)
#       if key2 == 'Qty':
#         Q = val2
#       else:
#         P = val2
#     print("Total : ", Q*P)
#     GT = GT + (Q*P)
# print("Grand Total : ", GT)