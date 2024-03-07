# To get emoji dynamically
# c = int(input("Enter No : "),16)
# u = chr(c)
# print("Unicode character : ", u)

# # ASCII - Unicode 
# for i in range(1536,1792):
#   print(chr(i), end=" ")

# for i in range(2304,2431):
#   print(chr(i), end=" ")

# Create List
# no = int(input("Enter No : "))
# Li=[]
# for x in range(1,(no+1)):
#   Li.append(input("Enter Name : "))
# print("List1 : ", Li)

# Slice List
# s = int(input("Enter Starting No : "))
# e = int(input("Enter Ending No : "))
# print(Li[s:e])

# na = input("Enter a name to search : ")
# if na in Li:
#   print("%s is present"%na)
# else:
#   print("%s is absent"%na)

# Indexing using enumerate :  New list with serial number
# newli = ["{}{}{}".format(y+1,".",x) for y,x in enumerate(Li)]
# enumerate can give an index as well as data from a List
# print(newli)

# Combining two lists
# no = int(input("Enter No : "))
# newLi=[]
# for x in range(1,(no+1)):
#   newLi.append(input("Enter Name : "))
# print("List2 : ",newLi)

# Li3 = []
# Li3 = Li + newLi
# print("Concated list : ", Li3)

# Segregating list using enumerate
# newli1 = [x for y, x in enumerate(Li3) if y%2 == 0]
# newli2 = [x for y, x in enumerate(Li3) if y%2 != 0]
# print("Segregated lists : \n",newli1,"\n",newli2)

# Shuffling list
# from random import shuffle
# shuffle(Li)
# print("Shuffled List : ", Li)

# Compare two list elements
# from collections import Counter
# print(list(Counter(Li) - Counter(newLi)))

# To get maximum, minimum and count of lists
# no = int(input("Enter no : "))
# newLi=[] # Empty list

# for x in range(no):
#   newLi.append([])
#   dept = input("Enter dept : ")
#   count = int(input("Enter Salary Count : "))
#   for i in range(count):
#     newLi[x].append(int(input("Enter Salary : ")))
# print("Final List : ", newLi)
# print("Maximum Salary : ", max(newLi, key=sum))
# print("Minimum Salary : ", min(newLi, key=sum))
# print("Max Count Salary : ", max(newLi, key=len))

# Add incentive to only paricular department
# no = int(input("Enter No : "))
# newLi = [] # Empty list - one dimension 
 
# for x in range(no):
#   Li = [input("Enter name : "), input("Enter dept : "), int(input("Enter Salary : "))]
#   newLi.append(Li) # two dimension
# print("Original list", newLi)

# incentive = int(input("Enter Incentive Amount : "))
# dept = input("Enter Department Name : ")

# for i, (name, dept, salary) in enumerate(newLi):
#   if dept == dept:
#     newLi[i][2] = newLi[i][2] + incentive
# print(newLi)

# Add incentive to all department
# no = int(input("Enter No : "))
# newLi = [] 
 
# for x in range(no):
#   Li = [input("Enter name : "), input("Enter dept : "), int(input("Enter Salary : "))]
#   newLi.append(Li) 
# print("Original list", newLi)

# incentive = int(input("Enter Incentive Amount : "))

# for i, (name, dept, salary) in enumerate(newLi):
#   newLi[i][2] = newLi[i][2] + incentive
# print(newLi)

# Get name list, compare prev month and curr month salary
# from collections import Counter
# no = int(input("Enter no : "))
# nameLi = []
# for i in range(no):
#   Li = input("Enter Name "+ str(i+1) + ":")
#   nameLi.append(Li)
# print("Name List : ", nameLi)
# PreList = []
# CurList = []
# for i in range(len(nameLi)):
#   name = nameLi[i]
#   newvar = input("Enter Prev Salary to " + name + ": ")
#   x = [name,newvar]
#   PreList.append(x)

#   newvar = input("Enter Cur Salary to " + name + ": ")
#   x = [name,newvar]
#   CurList.append(x)

# print("Previou List : ", PreList)
# print("Current List : ", CurList)

# for i in range(no):
#   print(Counter(PreList[i]) == Counter(CurList[i]))

