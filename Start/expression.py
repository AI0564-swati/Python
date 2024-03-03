''' operator precedence : 
not > and > or
(), **, *, /, //(Integer Division, i.e., floor - closest lesser integer value), %, (+, - are operated left to right) '''

a = 3
b = 2
sum = a + b
print(sum)

diff = a - b
print(diff)

# String and Numeric values can operate together with * (Repetation)
A,B = 2,3
Txt = "@"
print(A*Txt) 
print(A*Txt*B) 

# String and Numeric values can operate together with + (Concatenation)
A,B = "2",3
Txt = "@"
print((A+Txt)) 
print((A+Txt)*B) 

# Arthematic expression with integer and float will result in float
print(3+5.0) # 8.0
print(1/2) # 0.5
print(1//2) # 0.0
print(6/2) # 3.0

# modulo (%) will give -ve remainder only in case numerator is +ve and denominatior is -ve, in other case it will always be +ve.
