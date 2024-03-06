#for, while, do, intro to list

# Find length of the string without any pre-defined function
# str = input("Enter your name : ")
# counter = 0
# for c in str:
#     print(c, end = " ")
#     counter = counter + 1
# print("\nLength of name is : ", counter) #Outside of for loop

# Reverse the string without any pre-defined function
# str = input("Enter your name : ")
# st = " "
# for c in str:
#     st = c+st
# print(st)

# To print single table
# no = int(input("Enter no. : "))
# t = int(input("Enter table : "))
# for i in range(1, no+1):
#     print(i, "*", t, "=", (i*t))

# Nested for - To print more than one table
# for t in range(int(input("Enter no : "))+1):
#     print("Table of : ", t)
#     for i in range (1,11):
#         print(i,"*",t,"=",(i*t))

# Some pre-defined functions
# help("modules")
# help("topics")
# help("NUMBERS")
# help("INTEGER")

# While loop

# no = int(input("Enter no : "))
# sum = 0
# while(no>0):
#     sum += no # `+=` is an augmented operator
#     no -= 1
#     print("Sum is : ", sum)
# print("Sum is : ", sum)

# Simple Calculator using While Loop
# x = int(input("Enter x : "))
# y = int(input("Enter y : "))
# while True:
#     print("1 - Add")
#     print("2 - Sub")
#     print("3 - Mul")
#     print("4 - Div")
#     print("5 - Exit")
#     choice = int(input("Enter choice : "))
#     if choice == 1:
#         print("Addition : ", (x+y))
#     elif choice == 2:
#         print("Subtraction : ", (x-y))
#     elif choice == 3:
#         print("Multiplication : ", (x*y))
#     elif choice == 4:
#         print("Division : ", (x/y))
#     elif choice == 5:
#         print("Exiting program")
#         break; #come out from the while
#     else:
#         print("Invalid choice, try again")

# import random # predefined/standard module to give random number
# s = random.randint(1,11)
# no = int(input("Guess a number : "))
# while s != no:
#     print("Not Matched")
#     no = int(input("Guess again : "))
# print("Congratulation! You guessed the secret no.")

# List : Similar to array
# Can store more than one datatype
# Ordered - Sorted
# Mutable
# Use [] to create a list
# Index starts with 0
# Provides pre-defined functions

# Odd Even usin while
# no = [1,2,3,4,5,6,7,8]
# odd = 0
# even = 0
# for x in no:
#     if x%2 == 1:
#         odd=odd+1
#     else:
#         even=even+1
# print("Even No : ", even)
# print("Odd No : ", odd)

# List with dynamic element : break, pass, continue 
# print("How many element?")
# no = int(input("Enter no : "))
# Li = []
# for i in range(no):
#     Li.append(int(input("Enter element : ")))
# print("List with element : ", Li)
# b = int(input("Enter value to break/pass/continue : "))
# for n in Li:
#     if n == b:
#         # pass # do nothing when the no is found
#         # break # come out of the loop when the no is found
#         continue # skip to the next element when the no is found
#     else:
#         print(n, end = " ")

# List, tuple, string, dictionary - non-primitive special datatype 
# help(list)
# sort(), reverse(), remove(), len()
# print("How many members?")
# no = int(input("Enter no : "))
# Li = []
# for i in range(no):
#     Li.append(input("Enter names : " + str(i+1) + ":"))
# print(Li)
# Li.sort()
# print(Li)
# Li.reverse()
# print(Li)
# Li.remove(input("Enter name to remove "))
# print("After remove : ", Li, "\n", "Count : ", len(Li))

# To use random name from the list
# import random
# print("How many members?")
# no = int(input("Enter no : "))
# Li = []
# for i in range(no):
#     Li.append(input("Enter names : " + str(i+1) + ":"))
# print(Li)
# print("Selected member : ", Li[random.randint(0, len(Li))])


# print("How many members?")
# no = int(input("Enter no : "))
# Li = []
# for i in range(no):
#     Li.append(input("Enter name " + str(i+1) + ": "))
# print(Li)
# for i in range(0,len(Li)):
#     Li[i] = Li[i] + "-" + input("Enter department : ")
# print("Name with dept : ", Li)


