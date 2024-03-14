# Object-Oriented Programming System/Structure

# Procedural --> Functional --> OOPS
# This reduces redundancy and increases reusability.

# Class is a blueprint for creating objects.

# creating class
# class Student:
#   name = "Swati Tanu"

# # creating object (instance)
# s1 = Student()
# print("s1 => ", s1)
# print(s1.name)

# Constructor
# All classes have a function called _init_(), which is always executed when the object is being initiated. Python always execute this function automatically.

# Default constructor
# def __init__(self):
#   pass

# Parameterized constructor
# class Car:
#   ParentCompany = "Mercedes-Benz Group"
#   def __init__(self, color, brand, engine):
#     self.color = color
#     self.brand = brand
#     self.engine = engine
#     print("self => ", self)
#     print("Adding new car in database...")
#   # color = "Black",
#   # brand = "Mercedes"

# print("ParentCompany ==> ", Car.ParentCompany) # We can access class attribute directly via class
# car1 = Car("Black", "Mercedes", "OM904") 
# print(car1.color, car1.brand, car1.engine) # attributes

# i.) Attributes: 1. class.attr 2. obj.attr

# obj attr > class attr (in usage/preferance)

# ii.) Methods : Functions that belong to objects.

# class Student:
#   def __init__(self, name, marks):
#     self.name = name
#     self.marks = marks

#   @staticmethod
#   def hello():
#     print("Using decorator to convert this to a static method, i.e., not using self parameter.")

#   def get_avg(self):
#     sum = 0
#     for val in self.marks:
#       sum += val
#     print("Hi", self.name, ". Your avg score is:" , sum/3)

# s1 = Student("Tony Stark", [87,94,77])
# s1.get_avg()
# s1.hello()

# Static Methods: Methods that don't use self parameter. It works at class level.
# @staticmethod # decorator

# Decorator is a function that takes a function in parameter and returns a function in output too after changing it's behavior.

# 4 pillars of OPPS:

# 1. Abstraction
# Hiding the implementation details of a class & only showing the essential features to the user. 
# class Car:
#   def __init__(self):
#     self.acc = False
#     self.brk = False
#     self.clutch = False

#   def start(self):
#     self.clutch = True
#     self.acc = True
#     print("Car Started...")

# car1 = Car()
# car1.start()

# 2. Encapsulation
# Wrapping data and functions into a single unit (object).

# 3. Inheritance
# When one class(child/derived) derives the properties & methods of another class(parent/base)

# 4. Polymorphism
# When the same operator is allowed to have different meaning according to the context.
# Eg:
# print(1 + 2) # adds in case of numbers
# print("Swati" + "Tanu") # concatenates in case of strings
# print([1,2,3] + [4,5,6]) # merges in case of lists

# class Account:
#   def __init__(self, bal, acc):
#     self.balance = bal
#     self.account = acc

#   def debit(self, amount):
#     self.balance -= amount
#     print("Rs.", amount, "was debited.")
#     print("Total balance = ", self.get_balance())

#   def credit(self, amount):
#     self.balance += amount
#     print("Rs.", amount, "was credited.")
#     print("Total balance = ", self.get_balance())

#   def get_balance(self):
#     return self.balance

# acc1 = Account(10000, 12345)
# print(acc1.balance)
# print(acc1.account)
# acc1.debit(1000)
# acc1.credit(500)

# del keyword: Used to delete object properties or object itself

# del s1.name
# del s1

# class Car:
#   @staticmethod
#   def start():
#     print('Car started...')

#   @staticmethod
#   def stop():
#     print('Car stopped...')

# class ToyotaCar(Car):
#   def __init__(self, name):
#     self.name = name

# car1 = ToyotaCar("Fortuner")
# car2 = ToyotaCar("Prius")

# print(car1.start())

# super() method is used to access methods of the parent class.

