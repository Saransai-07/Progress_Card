#  string and string manipulations
# text = ["backend"," frontend"]

# print(text[0:4])
# print(text[2:])
# print(text[:3])
# print(text[::-1])

# s = 'h.e.llo'
# print(s.split("l"))

# name = "Saran"
# age = 22
# # print(f'my name is {name} and I am {age}')

# "Hello {}".format(name)

# text = "hello"
# text = 'H' + text[1:]
# print(text)

# text = "Count vowels in a string."
# count = 0
# for i in text:
#   if i == 'a':
#     count += 1
#   elif i == 'e':
#     count += 1
#   elif i == 'i':
#     count += 1
#   elif i == 'o':
#     count += 1
#   elif i == 'u':
#     count += 1
    
# print(f'the no of vowels in text is {count}')

# text2 = "Reverse a string" 
# print(text2[::-1])

# text3 = "string is palindrome"
# for i in text3:
#   if i == [::-i]:
#     print("palinodrome ")
#   else : 
#     print('not palinodrome')


# def count_vowels(s: str):
#   vowels = set("aeiou")
#   count = 0
#   for ch in s.lower():
#     if ch in vowels:
#       count += 1
#   return count

# print(count_vowels("Hello"))

# def is_palinodrome(s):
#   s = "".join(char.lower())
#   for char in s:
#     if char.isalnum():
#       return s == s[::-1]

# print(is_palinodrome("racecar"))
# print(is_palinodrome("A man ,a plan ,,,a canal Panama"))

# def remove_spaces_simple(s:str) -> str:\
#   return s.replace(" ","")

# def remove_all_whitespaces(s:str) -> str:
#   return " ".join(ch for ch in s if not ch.isspace())

# print(remove_spaces_simple("a b   c"))
# print(remove_all_whitespaces("a \t b  \t  \nc"))
  
# def extract_digits(s):
#   return "".join(ch for ch in s if ch.isdigit())

# print(extract_digits("a1bc34d53"))


import re 
# from collections import Counter
# from typing import Dict

# def word_frequency(text):
#   text = text.lower()
#   words = re.findall(r'\b\w+\b', text)
#   return dict(Counter(words))

# print(word_frequency("Hello hello  world!1"))
# print(word_frequency("Logs : ERROR 500, error 404, error"))

# def removal_special_chars(s):
#   return re.sub(r'[^A-Za-z0-9_-]+','',s)

# def remove_special_chars_manual(s):
#   return "".join(ch for ch in s if ch.isalnum() or ch in "_-")

# print(removal_special_chars("user@domain.com!"))   # "userdomaincom"
# print(removal_special_chars("file_name-01#v2"))    # "file_name-01v2"
# print(remove_special_chars_manual("a$b%c^--")) 

# def remove_special_chars(s, keep_space=True):
#   allowed = set(['_' , '-'])
#   if keep_space:
#     allowed.add(' ')
#   return "".join(ch for ch in s if ch.isalnum or ch in allowed)

# print(remove_special_chars("hello@world.com"))       # "helloworldcom"  (dot removed)
# print(remove_special_chars("user_name-123!#$"))      # "user_name-123"   (keeps underscore & hyphen)
# print(remove_special_chars("keep spaces  yes!"))     # "keep spaces  yes" (spaces preserved)
# print(remove_special_chars("keep spaces  yes!", keep_space=False))  # "keepspacesyes"

# name = input()
# print(name)
# print(type(name))

# try:
#   num = int(input("Enter the number"))
#   print(10/num)
# except ValueError:
#   print('That was not a number')
# except ZeroDivisionError:
#   print('Cannot divide by zero ')
  
  
# with open("data.txt", "r") as file:
#   content = file.read
#   print(content)

# class Car:
#   def __init__(self, brand, spped):
#     self.brand = brand
#     self.spped = spped
    
#   def accelerate(self):
#     return f'{self.brand} accelerate to {self.spped} km/h'
  
# c1 = Car("BMW", 250)
# c2 = Car("AUDI", 250)

# print(c1.accelerate())
# print(c2.accelerate())


# num1 = int(input("Enter the first number"))
# num2 = int(input("enter the secopnd number"))

# add = num1 + num2
# sub = num1 - num2
# mul = num1 * num2
# div = num1 / num2

# print(f"sum is {add}, sub is {sub}, mul is {mul}, div is {div} ")

# name = input("Enter the name")
# age = int(input("enter the age "))

# age2 = age+5
# str(age2)

# print(f" Hello {name} you wii be {age2} years old after 5 years")

# sentence = input("Enter the sentence ")

# print(len(sentence))
# print(sentence[:3])
# print(sentence[-3:])
# print(sentence.upper())

# num = int(input("Enter the how many numbers"))
# list1 = []
# for i in range(num):
#   num2 = int(input(" Enter the number"))
#   list1.append(num2)

# print(list1)

# str1 = input("Enter the string 1") 
# str2 = input('Enter the second string')

# list1 =[str1, str2]
# list1.reverse()

# print(str(list1))

# num1 = int(input("Enter the number 1"))
# num2 = int(input("Enter the number 2"))

# try:
#   div = num1 / num2
#   print(f'the safe Division {div}')
# except ValueError:
#   print(f"Please enter the valid number")
# except ZeroDivisionError:
#   print("Cannot divide by zero ")
  
# list1 = [10, 20, 'abc', 40]

# for i in list1:
#   try:
#     i.isdigit()
#     print(i)
#   except :
#     print(f'invalid number : {i}')

# numbers = [10, 20, 30, 40]
# index = int(input("Enter the index number"))

# try:
#   indexed_number = numbers[index]
#   print(indexed_number)
# except ValueError:
#   print(f"non- numeric number")    
# except IndexError:
#   print(f" index out of range")
  

# num1 = int(input("Enter the first number"))
# opreator = input("Enter the operator")
# num2 = int(input("Enter the second number"))


# try:
#   print(f'the operation is ({num1}{opreator}{num2})')
# except ValueError:
#   print(f'Please enter the correct number')
# except ZeroDivisionError:
#   print(f'Cannot divisible byu zero')
# except:
#   print(f'Unsupported operator')
  
# values = input('Enter the comma seperate values ').split(',')

# for v in values:
#   v = v.strip()
#   try: 
#     num = int(v)
#     print(num)
#   except ValueError:
#     print(f"invalid number: {v}")


# num1 = int(input("Enter the first number"))
# opreator = input("Enter the operator")
# num2 = int(input("Enter the second number"))

# try :
#   if opreator == "+":
#     print(num1 + num2)
#   elif opreator == "-":
#       print(num1 - num2)
#   elif opreator == "*":
#       print(num1 * num2)
#   elif opreator == "/":
#       print(num1 / num2)
#   else:
#     print("Unsupported operator")
# except ValueError:
#   print("invalid number enterd")
# except ZeroDivisionError:
#   print("Cannot dividble by zero")

# with open("data.txt","r") as f:
#   content = f.read()
#   print(content)
  
# with open("data.txt", "r") as  f:
#   print(f.read())
  
# with open("info.txt", "w") as f:
#   f.write('Hello Saran')

# with open("info.txt" , 'r') as f:
#   content = f.read()
#   print(content)

# items = ['apple', 'banana', 'cherry'] 
# with open('info.txt', 'a') as f:
#   for i in items:
#     f.write(f"\n {i}")

# with open('info.txt') as f:
#   for line in f:
#     print(line.strip())


# file_name = input("enter the file name ")
# destination_file = input('enter the file name')

# with open(f"{file_name}", "r") as f:
#   count = 0 
#   for i in f:
#     count += 1
#   print(f'File has {count} lines.')

# with open(f'{file_name}','r') as f:
#   for i in f:
#     with open(f"{destination_file}","a") as f1:
#       f1.write(f"\n {i}")
      
      
# class Car:
#   def __init__(self, brand, price):
#     self.brand = brand
#     self.price = price

# c1 = Car('BMW', 500000)
# c2 = Car('Audi', 450000)
# print(c2.price, c2.brand)

# class Car:
#   def __init__(self, brand, price, color):
#     self.brand = brand
#     self.price = price
#     self.color = color
    
#   def start(self):
#     print(f'{self.brand} is stating')
#   def stop(self):
#     print(f'{self.price} price car is stopped')
#   def damaged(self):
#     print(f'{self.color} and {self.brand} is damaged')


# c1 = Car("BMW", 2000000, 'red')
# c2 = Car("AUDI" , 1500000, "black")

# # print(c1.damaged())
# c1.damaged()

# class BankAccount:
#   def __init__(self, owner, balance):
#     self.owner = owner
#     self.balance = balance
    
#   def deposit(self, amount):
#     self.balance += amount
  
#   def withdraw(self, amount):
#     if amount <= self.balance:
#       self.balance -= amount
#     else:
#       print('Insuffient balance')

# acc = BankAccount("saran", 1000)
# acc.deposit(500)
# acc.withdraw(1501)
# print(acc.balance)

# class Student:
#   def __init__(self, name, age, grade):
#     self.name = name
#     self.age = age 
#     self.grade = grade
  
#   def details(self):
#     print(f'My name is {self.name} and age is {self.age} and my grade is {self.grade}')
    
#   def is_passed(self):
#     if self.grade >= 40:
#       return "passed"
#     else : 
#       return "Failed"
# student1 = Student("Saran", 23, 77)
# student1.details()
# print(student1.is_passed())


# class Calculator:
#   def __init__(self, num1, num2):
#     self.num1 = num1
#     self.num2 = num2
  
#   def add(self):
#     return self.num1 + self.num2
#   def sub(self):
#     return self.num1 - self.num2
#   def mul(self):
#     return self.num1 * self.num2
#   def div(self):
#     if self.num2 == 0:
#       return "Error: Cannot divide by zero"
#     return self.num1 / self.num2

# a1 = Calculator(20,10)
# a2 = Calculator(20,10)
# a3 = Calculator(20,10)
# a4 = Calculator(20,0)

# print(a1.add())
# print(a1.sub())
# print(a1.mul())
# print(a4.div())  


# class Vehicle:
#   def __init__(self, brand, model, year):
#     self.brand = brand
#     self.model = model
#     self.year = year
    
#   def show_info(self):
#     print(f'Brand :{self.brand} , model :{self.model}, year: {self.year}')
  
# class Car(Vehicle):
#   def __init__(self, fuel):
#     self.fuel = fuel
  
#   def fuel_type(self):
#     self.fuel
  
#   def car_Details(self):
#     print(f'Brand :{self.brand} , model :{self.model}, year: {self.year} and fuel type : {self.fuel}' )
    
    
# c1 = Car("Audi", "City", 2024)

# c1.car_Details()
