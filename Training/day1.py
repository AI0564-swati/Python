# # Comment
# '''
# Multi line Comments
# '''

# notes= '''This
#                is
#                 sample
#                   notes'''
# print(notes)

# pattern ='''
#                  *

#         *               *

#                 *
#                 '''
# print(pattern)

# # Dynamic Programming Language
# x = 5 # Assigning statement - int
# print(x)
# print(type(x))
# x = "Aggregate" # String
# print(x)
# print(type(x))

# # Syntax is clean and straightforward 
# # -  no blocks needed
# # - indentation is important --> tab/4spaces 

# # Python libraries:
# # 1. Internal / Standard libraries
# import random

# r = random.randint(1,100)
# print(r)

# # Note: In C we get same random num but not in Python

# # 2. External libraries

# # An interpreted language: converts each program statement into machine code

# # keywords - 35
# # IDLE - Integrated Development Learning Environment.
# print("Sample")
# print("Test")

# # Can use multiple statement in same line
# print("Sample"); print("Test")

# # To print in same line
# print("Sample", end=" ")
# print("Test", end=" ")
# print("Welcome")

# # Input statement - to get input from the user dynamically
# name = input("Name : ") # Input by default is string
# print("Name is : ", name)
# salary = int(input("Enter Salary : "))

# print("Name is : ", input("Name : "), "Salary is : ", salary) # nested function
 
# print(salary + 5000)

# # System info
# import sys
# print("Python Version : ", sys.version)
# print("Python Version Info : ", sys.version_info)

# # Chaining Assignments
# oldadhaar = "1001"
# newadhaar = oldadhaar = oldadhaar + "- A"
# print("oldadhaar : ", oldadhaar)
# print("newadhaar : ", newadhaar)

# # Multiple variable in same line
# pno,pname,price = 101,"Asus Laptop",95000
# print(pno,"\n",pname,"\n",price)

# # Escape Operator - \n \t
# print("\"Aggregate\"")
# print("Kolkata","\n","West bangal""\n\t\t","India")

# # length of string
# print(name, "length is : ", len(name))

# # swap
# a = input("Enter a : ")
# b = input("Enter b : ")
# c = input("Enter c : ")

# # Only Python supports this
# a,b = b,a 
# print("a is : ", a) 
# print("b is : ", b) 
# print("c is : ", c) 

# # Augmented assignments (Arithmetic operators)
# m = 12
# m %= 7 
# print("Remainder : ", m)

# n = 3
# n *= 2
# print("Multiple : ", n)

# o = 3
# o **= 2
# print("Power : ", o)

# # Print Calender
# import calendar
# y = int(input("Enter year : "))
# m = int(input("Enter month : "))

# print(calendar.month(y,m))

# # Print random value of list
# import random
# print(random.choice(["Ram", "Shyam", "Sita", "Lakshman", "Urmila"]))


