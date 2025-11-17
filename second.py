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