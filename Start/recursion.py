# Recursion: When a function calls itself repeatedly.
# Works very similar to loops.

# def show(n):
#   if(n == 0): # base code (condition)
#     return
#   print(n)
#   show(n-1)
#   print("End")

# show(5)

# def fac(n):
#   if( n==0 or n==1):
#     return 1
#   else:
#     return n * fac(n-1)
  
# print(fac(5))

# def cal_sum(n):
#   if(n == 0):
#     return 0
#   else:
#     return n + cal_sum(n-1)
  
# print(cal_sum(2))

def print_list(list, i=0):
  if(i == len(list)):
    return 
  else:
    print(list[i])
  print_list(list, i+1)

print_list([2,4,6,8])