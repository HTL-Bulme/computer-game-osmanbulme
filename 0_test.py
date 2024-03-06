#width=7
#length=2
#print(width//length)

#print(r"For space jacks:\n""\nYou did it")

#prefix = "bal"
#print(prefix+"ls")

#word = "23"
#print(range(len(word))) ####

#squares = [1, 4, 9, 16, 25]
# print(2**3*squares)

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# letters[2:5] = ['C', 'D', 'E']
# print(letters)
# letters.append(3)
# print(letters)

# a, b = 0, 1
# while a < 1000:
#     print(a, end=',')
#     a, b = b, a+b

# words = ['cat', 'window', 'defenestrate']
# for i in words:
#     print(i, len(i))

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = car.items()
# print(x)

# fruits = ['apple', 'banana', 'cherry', 'orange']
# x = fruits.copy()
# print(x)


# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
# for user, status in users.copy().items():
#     if status == 'inactive':
#         print(users[user])
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status
#         print(status)

# for i in range(2,5):
#     print(i)

# list(range(5, 10))
# print(list(range(1, 6))) # index 0 bis 5




# for n in range(2, 10): #2,3,4,5,6,7,8,9
#     for x in range(2, n): #2,3
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')

# def http_error(status):
#     match status:
#         case 400:
#             return "Bad request"
#         case 404:
#             return "Not found"
#         case 418:
#             return "I'm a teapot"
#         case _:
#             return "Something's wrong with the internet"

# def multiplication_or_sum(number):

# Zahl1 = 20
# Zahl2 = 30

# Produkt = Zahl1*Zahl2
# Summe = Zahl1+Zahl2

# if Produkt<=1000:
#     print("The result is ",Produkt)
# else:
#     print("The result is ",Summe)

# def Convert(string): 
#     li = list(string.split(" ")) 
#     return li 
  
  
# # Driver code 
# str1 = "Geeks for Geeks"
# print(Convert(str1)) 