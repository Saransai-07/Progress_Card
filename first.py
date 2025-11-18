# fruits = ["apple", "banana", "cherry",1,4,3,5,2]
# print(fruits)

# dist = {"name": "saran", "age" : 30, "city": "hyd"}
# print(dist["name"])
# dist["job"]= "engineer"
# dist["age"] = 31
# print(dist.keys())
# print(dist.values)
# print(dist)/

# mySet = {1, 4, 3, 2, 2, "apple", True}
# print(mySet)
# mySet.add(5)
# mySet.remove(3)
# print(mySet)
# print(2 in mySet)
# coordinates = (10, 30,20, 10)
# print(coordinates)
# numbers = {1, 3, 2, 3, 2, 1}
# print(numbers)  # {1, 2, 3}
# numbers.add(4)
# numbers.remove(2)
# print(numbers)

# a= {1, 2, 3}
# b= {3, 6, 5}
# print(a&b)
# print(a|b)
# student = {"name": "Saran", "age": 21, "skills": ["Python", "HTML"]}

# for i in student.items():
#   print(key ,":", value)

# list1 =[25, 15, 10 , 30, 20]
# sum = 0
# for i in  list1:
#   sum = sum + i  

# print(sum)
# b = max(list1)
# c = min(list1)

# print(c, b)
# list1[2] = 99

# print(list1)

# tuple1 = (1, 3, 2, 4)
# tuple1[2] = 6

# print(tuple1)

# t = (1, 3, 2, 4)

# temp = list(t)
# temp[1] = 99

# t = tuple(temp)

# print(t)

# L = [1, 2, 2, 3, 4, 4, 5]

# S = set(L)
# print(S)


# student = {
#   "name" : "saran",
#   "age" : 22,
#   "course" : "B.Tech",
#   "marks" : {
#     "maths" : 30 ,
#     "science" : 20,
#     "english" : 20,
#     "telugu" : 30
#   }
# }
# sum = 0
# for s,i in student["marks"].items():
#   sum += i
# avg = sum /len(student["marks"])
# print(avg)


# l1 = ["apple", "banana", "apple", "orange", "banana", "apple"]
# for i in l1: 
#   i +=1
# print(len(i))

# l1 = ["apple", "banana", "apple", "orange", "banana", "apple"]
# count ={}
# for word in l1:
#   if word in count:
#     count[word] += 1
#   else : 
#     count[word] = 1
# print(count)

# numbers = [1, 2, 2, 3, 1, 4, 2, 3]
# temp = set(numbers)
# print(list(temp))

# s = "banana"
# count = {}
# for i in s:
#   if i in count:
#     count[i] += 1
#   else : 
#     count[i] = 1
# print(count)

# sentence = "apple banana apple orange banana apple"

# print(list(sentence))

# for i in sentence:
#   print(i)

# numbers = [1, 2, 2, 3, 1, 4, 2, 3]

# unique = []
# seen = set()

# for num in numbers:
#   if num not in seen: 
#     unique.append(num)
#     seen.add(num)
    
# print(unique)

# users = [
#   {"id": 1, "name": "Saran"},
#   {"id": 2, "name": "Ram"},
#   {"id": 3, "name": "Kumar"},
# ]
# sum =1
# for i in users:
#   print(sum, ":", i)
#   sum += 1
  

# d1 = {"a": 10, "b": 20, "c": 30}
# d2 = {"b": 5, "c": 15, "d": 25}

# result ={}

# for key , value in d1.items():
#   result[key] = value

# for key, value in d2.items():
#   if key in result:
#     result[key] += value
#   else :
#     result[key] = value

# print(result)

# users = [
#   {"id": 1, "name": "Saran"},
#   {"id": 2, "name": "Ram"},
#   {"id": 3, "name": "Kumar"},
# ]
# indexed_user = {}
# for user in users:
#   indexed_user[user["id"]] = user
# print(indexed_user)

# marks = {
#   "math": 92,
#   "science": 58,
#   "english": 77,
#   "history": 40
# }

# result = {}

# for key, value in marks.items():
#   if value >=90 and value <=100 :
#     result[key] = "A"
#   elif value >= 75 and value <=89:
#     result[key] = "B"
#   elif value >= 50 and value <= 74:
#     result[key] = "C"
#   else:
#     result[key] = "F"

# print(result)


# arr = [[1,2], [3,4,5], [6]]
# for  i in arr:
#   print(i)

# classA = {"saran", "ram", "kumar"}
# classB = {"ram", "john", "kumar"}

# classC = classB & classA
# print(classC)

# numbers = [3, 6, 1, 2, 6, 3, 8, 6]
# appears = 0
# for i in numbers:
#   if i == 6:
#     appears += 1
# print(appears)
# temp = set(numbers)
# print(list(temp))

# numbers = [3, 6, 1, 2, 6, 3, 8, 6]

# count = 0 
# for n in numbers:
#   if n == 6:
#     count += 1
# print(count)

# new_list = []
# for n in numbers:
#   if n != 6:
#     new_list.append(n)
# print(new_list)

# # bubble sort
# for i in range(len(new_list)):
#   for j in range(len(new_list)-1):
#     if new_list[j] > new_list[j + 1]:
#       new_list[j], new_list[j + 1] = new_list[j + 1] , new_list[j]
# print(new_list)

# numbers = (10, 20, 30, 40, 20, 10, 50)
# count = 0 
# for i in numbers:
#   if i == 20 :
#     count += 1
# print(count)

# temp = list(numbers)
# print(temp)

# new_list = []
# for i in temp:
#   if i != 30:
#     new_list.append(i)
#   else :
#     new_list.append(99)
# temp2 = tuple(new_list)
# print(temp2)

# index = 0
# for i in numbers:
#   if i != 40:
#     index += 1
#   else :
#     index
#     break
# print(index)

# list1 =[]
# for i in numbers:
#   if i in list1:
#     list1
#   else :
#     list1.append(i)

# print(tuple(list1))

# student = {
#   "name": "Saran",
#   "age": 22,
#   "marks": {
#     "math": 78,
#     "science": 88,
#     "english": 90,
#     "history": 55
#   }
# }
# total = 0 
# for keys, values in student["marks"].items():
#   total += values
# print(total)

# new_dist = {}
# for key, values in student["marks"].items():
#   if values >= 90 and values<=100:
#     new_dist[key] = "A"
#   elif values >= 75 and values<=89:
#     new_dist[key] = "B"
#   elif values >= 50 and values<=74:
#     new_dist[key] = "C"
#   else :
#     new_dist[key] = "F"
# print(new_dist)

# avg = total / len(student["marks"])
# print(avg)
# if avg >= 80 :
#   student["grade"] = "Excellent" 
# elif avg >= 60:
#   student["grade"] = "Good"
# elif  avg >= 40 :
#   student["grade"] = "Avreage"
# else :
#   student["grade"] = "poor"
# print(student)   

# list1 = [1, 2, 3, 4, 5, 6]
# list2 = [4, 5, 6, 7, 8, 9]
# set1 = set(list1)
# set2 = set(list2)
# print(set1 | set2)
# print(set1 & set2)
# print(set1 - set2)
# # print(set1   | set2 & set1 )
# # print(set1 | set2 - set1 | set2)
# print(set1 ^ set2)

# products = [
#   ("Laptop", 55000),
#   ("Mouse", 500),
#   ("Keyboard", 1500),
#   ("Monitor", 12000),
#   ("CPU", 30000)
# ]

# new_product = {}
# for key, value in products:
#   new_product[key] = value
# print(new_product)

# highest_product = None
# highest_price = -1 

# for name , price in products :
#   if price > highest_price:
#     highest_price = price 
#     highest_product = name 
# print(highest_product, highest_price)

# total = 0 
# for name , price in products:
#   total += price  
# avg_price = total / len(products)
# print(avg_price)

# category = {
#   "expensive" : [],
#   "medium" : [],
#   "cheap" : [],
# }

# for name, price in products:
#   if price >= 20000:
#     category["expensive"].append(name)
#   elif 5000 <= price < 20000 :
#     category["medium"].append(name)
#   else : 
#     category["cheap"].append(name)
    
# print(category)

# students = [
#   {"name": "Saran", "skills": ["Python", "HTML", "CSS"]},
#   {"name": "Kumar", "skills": ["Python", "Java", "SQL"]},
#   {"name": "Ravi", "skills": ["HTML", "CSS", "JavaScript"]},
#   {"name": "Mohan", "skills": ["Python", "JavaScript", "SQL"]}
# ]

# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Something before the function call")
#         result = func(*args, **kwargs)
#         print("Something after the function call")
#         return result
#     return wrapper

# def say_hello(name):
#     print(f"Hello, {name}!")

# say_hello = my_decorator(say_hello) # Manual application
# say_hello("Alice")




# def smart_divide(func):
#   def wrapper(a, b):
#     if b == 0:
#       print("whoops! Cannot divide by zero")
#       return
#     return func(a, b)
#   return wrapper

# @smart_divide
# def divide(a,b):
#   return a/b

# print(divide(10,2))
# print(divide(10,0))


# def repeat(num_times):
#   def decorator_repeat(func):
#     def wrapper(*args,**kwargs):
#       for i in range(num_times):
#         result = func(*args,**kwargs)
#       return result
#     return wrapper
#   return decorator_repeat

# @repeat(num_times=3)
# def greet(name):
#   print(f"Hello {name}")

# greet("Saran")


# def logger(func):
#   def wrapper(*args, **kwargs):
#     print(f"Calling { func.__name__} with args : {args}, kwargs: {kwargs}")
#     result = func(*args, **kwargs)
#     print(f"{func.__name__} returned: {result}")
#     return result
#   return wrapper

# @logger
# def add(a, b):
#   return a+b

# add(5, 3)

# Calling add with args : (5, 3), kwargs: {}
# add returned: 8
def requires_auth(func):
    def wrapper(*args, **kwargs):
        # Check if user is authenticated
        is_authenticated = check_authentication()
        if not is_authenticated:
            raise PermissionError("Authentication required")
        return func(*args, **kwargs)
    return wrapper

@requires_auth
def sensitive_operation():
    return "Sensitive data"

def check_authenticatiodn():
    return True  # Simulated authentication check