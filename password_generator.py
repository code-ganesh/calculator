digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']

symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

password_list=[]
import random
no_char=int(input("enter number of characters required\n"))
no_digits=int(input("enter number of digits required\n"))
no_symbols=int(input("enter number of symbols required\n"))

for i in range(no_char):
    password_list+=random.choice(char)
for i in range(no_digits):
    password_list+= random.choice(digits)
for i in range(no_symbols):
    password_list+= random.choice(symbols)
random.shuffle(password_list)

password=""
for char in password_list:
    password+=char
print(password)

