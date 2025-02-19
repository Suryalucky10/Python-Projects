import random
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=[1,2,3,4,5,6,7,8,9,0]
symbols=["!","@","#","$","%","^","&","*","~"]
print("Welcome to the Pypassword generator!")
letters=int(input("how many letters would you like in your password?"))
"""password=""
for i in range(1,letters+1):
  char=random.choice(alphabets)
  print(char)
  password+=char
num=int(input("how many numbers would you like in your password?"))
for i in range(1,num+1):
  nm=random.choice(numbers)
  print(nm)
  password+=str(nm)
sym=int(input("how many symbols would you like in your password?"))
for i in range(1,sym+1):
  sm=random.choice(symbols)
  print(sm)
  password+=str(sm)
print(password)"""
#random arranged password
password=[]
for i in range(1,letters+1):
  char=random.choice(alphabets)
  print(char)
  password+=char
num=int(input("how many numbers would you like in your password?"))
for i in range(1,num+1):
  nm=random.choice(numbers)
  print(nm)
  password+=str(nm)
sym=int(input("how many symbols would you like in your password?"))
for i in range(1,sym+1):
  sm=random.choice(symbols)
  print(sm)
  password+=str(sm)
random.shuffle(password)
passw=""
for i in password:
    passw+=i
print(passw)    
    