# def calc_sum(a,b):
#   s = a + b
#   print("sum :", s)
#   return s

# calc_sum(5,3)

# Implicitly a function returns `None`

# Function types
# 1. Built-in fun
# -- sep = " ", end = "\n", print(), len(), type(), range()

# 2. User defined fun

# def default(a,b=1): # default argument should be in beginning
#   s = a + b
#   print("using default arg :", s)
#   return s

# default(3)

# def length(list):
#   l = len(list)
#   print("length :",l)
#   return l

# length([3,839,563,2,79,39,0,378])

# def line(list):
#   for i in list:
#     print("List :", i,end=" | ")

# line([3,839,563,2,79,39,0,378])
# print()

# def fac(n):
#   f = 1
#   for i in range(1,n+1):
#     f *= i
#   print("Factorial :",f)
#   return f

# fac(5)

# def convert(USD):
#   INR = 83
#   print("INR :",USD*INR)
#   return USD*INR

# convert(15)

# def even_odd(n):
#   if(n %2 == 0):
#     print("Even")
#   else:
#     print("Odd")

# user_input = int(input("Enter No: "))
# even_odd(user_input)

def check_odd_even():
    num = int(input("Enter No: "))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

check_odd_even()
