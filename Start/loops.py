# # While loop

# count = 1
# while count <= 5:
#   print("hello")
#   count += 1

# print("Loop ended")

# i = 5
# while i >= 1:
#   print("reverse")
#   i -= 1

# print("Reverse Loop ended")

# n = int(input("Enter no : "))
# i = 1
# while i <= 10:
#   print(n, "*", i, "=", n*i)
#   i += 1

# list = [2,4,78,27,99,5,3,68]
# i = 0
# while i < len(list):
#   print(list[i])
#   i += 1

# x = int(input("Enter no : "))
# tuple = (2,4,78,27,99,5,3,68)
# i = 0
# while i < len(tuple):
#   if tuple[i] == x:
#     print("The element", x, "is found")
#     break
#   else:
#     print("The element", x, "is not found")
#   i += 1

# print("End of loop")

# For loop

# nums = [1,72,93,4,56]
# for val in nums:
#   print(val)
# else:
#   print("End")

# # range(): Range function returns a sequence, starting from 0 by default, and increments by (step size) 1 (by default), and stops before a specified number(complesory to mention).

# # range can be written in 3 ways:
# print(range(5)) # range(stop)
# print(range(2,10)) #range(start, stop)
# print(range(2,10,2)) #range(start, stop, step)

# seq = range(5)
# for i in seq:
#   print(i)

# # pass: It is a null statement that does nothing, it is a placeholder for future code.
# for i in range(5):
#   pass
# print("Using pass statement")

# n = int(input("Enter no : "))
# sum = 0

# for i in range(n+1):
#   sum += i
# print("sum : ", sum)


# n = int(input("Enter no : "))
# fac = 1

# for i in range(1, n+1):
#   fac *= i
# print("factorial : ", fac)