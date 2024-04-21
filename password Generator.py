import random
alpha_g=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alpha_s=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
sym=['!','@','#','$','%','^','&','(',')','-','_','+','*','/','{','}','[',']',':',';','?',]
num=['1','2','3','4','5','6','7','8','9','0']
upper=int(input("How many Uppercase letter you need?"))
lower=int(input("How many Lowercase letter you need?"))
symb=int(input("How many Symbols you need?"))
numb=int(input("How many Number you need?"))
password=[]
for i in range(upper):
    password+=random.choice(alpha_g)
for i in range(lower):
    password+=random.choice(alpha_s)
for i in range(symb):
    password+=random.choice(sym)
for i in range(numb):
    password+=random.choice(num)
random.shuffle(password)
password_new=""
for i in password:
    password_new+=i
print(f"Your Password is {password_new}")
