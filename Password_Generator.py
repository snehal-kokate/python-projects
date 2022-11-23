import random
let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# #Eazy Level
# password = ""
#
# for char in range(1, nr_letters + 1):
#   password += random.choice(let)
#
# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)
#
# for char in range(1, nr_numbers + 1):
#   password += random.choice(num)

# print(password)
"""o/p=>(every time generate new password)
Welcome to the PyPassword Generator!
How many letters would you like in your password?
3
How many symbols would you like?
2
How many numbers would you like?
2
ocs&+81 
"""
"""using above method of generating password anyone can try with length
 of password and guess the correct one so try below method,
 so that generated password also random generating like change in order"""

password_list = []
for char in range(1, nr_letters + 1):#start from 1 so end should be +1
    password_list.append(random.choice(let))
    # password_list = password_list + random.choice(let) #error:can only concatenate list (not "str") to list
#    here we not concatenate list with list we concatenate char with list,so that can be done by using 'append' only
for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(num)

print(password_list)#['i', 'n', 'i', 'c', 't', 'm', 'y', '#', '(', '4', '1', '6']

random.shuffle(password_list)#change the order of list
print(password_list)#['n', 't', 'i', 'c', '6', 'i', '4', 'm', '1', '#', '(', 'y']

password = "" #here we left the list and all charracter come up in one string
for char in password_list:
    password += char
print(f"Your password is: {password}") #Your password is: ntic6i4m1#(y


"""o/p=>
Welcome to the PyPassword Generator!
How many letters would you like in your password?
How many symbols would you like?
How many numbers would you like?
['i', 'n', 'i', 'c', 't', 'm', 'y', '#', '(', '4', '1', '6']
['n', 't', 'i', 'c', '6', 'i', '4', 'm', '1', '#', '(', 'y']
Your password is: ntic6i4m1#(y
"""
