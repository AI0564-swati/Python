# import sys

# # To read the file
# txt = sys.stdin.read()
# w = txt.split()
# c = len(w)
# print("Word count : ", c)
# command: python day2.py < input.txt

# # Generating id
# i = input("Enter Name : ")
# print(i, "-",id(i), "-", type(i))
 
# i = int(input("Enter no : "))
# print(i, "-",id(i), "-", type(i))

# i = float(input("Enter no : "))
# print(i, "-",id(i), "-", type(i))

# Different colors : confusion

# import sys

# c = sys.stdout.shell
# c.write("Welcome","KEYWORD")
# c.write("\nAggregate","STRING")
# c.write("\nTanu","COMMENT")

# Argument vector
# import sys
# print(sys.argv)
# print(sys.argv[1])
# command: python day2.py a b c

# Run other python script from here

# import sys
# sys.path.append("\home\ai\Desktop\Office Projects\Practise-Projects\Python\Training\test.py")
# import test
# print("This is from main script")

# Format specificator
# %d, %f, %c

# no = int(input("Enter no. : "))
# print("ASCII: %d char: %c" %(no, no))

# name = input("Enter name. : ")
# print("%s is a developer" % name)

# Boolean - True (by default)
# b = input("Enter true or false")
# boolval = b.lower() == "true"
# print("Entered value : ", boolval)
# print("Boolean value is : ", bool(b))

# Long Datatype
# no = 1234567890123456789012345678901234567890
# print(no)
# multiple = no ** 10
# print(multiple)

# To get more digits after the decimal
# import decimal 
# no = float(input("Enter no : "))
# print(no)
# print(100/3)
# decimal.getcontext().prec = 4
# print(decimal.Decimal(100)/decimal.Decimal(3))

# bitwise operator 
# &, |, <<(left shift), >>(right shift), ~(ones complimentary)
# no1 = int(input("Enter no1 : ")) 
# print("Binary no : ", bin(no1)) # 30
# no2 = int(input("Enter no2 : ")) # 45
# print("Binary no : ", bin(no2))

# print(no1 & no2) # 12
# print(no1 | no2) # 63

# print(~no1) # -31

# 2 4 8 16 32 64 126 254 512 1024
# print(16 << 2) # left shift moves right side
# print(16 >> 2) # right shift moves left side
# print(512 >> 4)

# Emoji
# print("\U0001F600")
# print("\U0001F923")

# Logical operator: and or not operator
# print(2 < 4 and 2==4)
# print(2 > 4 or 2 < 4)
# print(not 6.2 <= 6)
# print(3 < 4 < 5)
# print(4 > 3 == 3)
# print(4 < 3 < 5 != 2 < 7)

# input, output, expression, assigning

# Control statement
# 1. Branching / Decision making
#     a. If
#         - if, if else, if elif elif (Ladder If)
#         - Nested if (if within if)
#     b. Switch
#     c. Ternary(?, :) - Python does not support ternary operator directly.
# 2. Looping
#     a. for
#     b. do
#     c. while

# ch = input("Enter a character : ")
# if(ch >= 'a' and ch <= 'z'):
#     print(ch,"is small letter")
# elif(ch >= 'A' and ch <= 'Z'):
#     print(ch, "is capital letter")
# elif(ch >= '0' and ch <= '9'):
#     print(ch, "is numeric letter")
# else:
#     print(ch, "is a symbol")

# Instead of ternary we use branching differently to make it single line condition

# n = int(input("Enter a : "))
# print(n)
# res = n*5 if n>50 else n/5
# print(res)

# a = int(input("Enter a : "))
# b = int(input("Enter b : "))
# c = int(input("Enter c : "))

# print("a is greater" if(a>b) and (a>c) else "b is greater" if(b>a) and (b>c) else "c is greater")

# # For Loop
# no = int(input("Enter no : "))
# for x in range(no): # initial value - 0 end - no
#     print(x)

# no = int(input("Enter no : "))
# for x in range(5, no+1):    # initial value - 5 end - no
#     print(x)

# no = int(input("Enter no : "))
# for x in range(2, no+1, 3):    # initial value - 5 end - no skip by - 3
#     print(x)

# Reverse
# no = int(input("Enter no : "))
# for x in range(no, 0, -3):   
#     print(x)

# Printing ASCII values
# for x in range(0,256):
#     print(chr(x))