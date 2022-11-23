"""ased on a user's order, work out their final bill.
Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1

create a total bill of customer"""

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0
if size=="S":
    bill +=15
elif size =="M":
    bill +=20
else:
    bill+=25

if add_pepperoni == "Y":
    if size =="S":
        bill += 2
if add_pepperoni=="Y" :
    if size =="M" or size=="L":
        bill +=3

if extra_cheese=="Y":
    bill = bill+1
print(f"Your final bill is: ${bill}.")



"""o/p=>
Welcome to Python Pizza Deliveries!
What size pizza do you want? S, M, or L: M
Do you want pepperoni? Y or N: Y
Do you want extra cheese? Y or N: Y
Your final bill is: $24.
"""
