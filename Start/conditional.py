light = input("light : ")

if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("look")
elif(light == "green"):
    print("go")
else:
    print("light is broken")

# Ternary operator

food = input("food : ")
eat = "Yes" if food == "cake" or food == "jalebi" else "no"
print(eat)

# Clever If/Ternary Operator
age = int(input("age : "))
vote = ("Yes", "No") [age < 18]
print(vote)

num1 = int(input("num1 : "))
num2 = int(input("num2 : "))

print(num1 >= num2)