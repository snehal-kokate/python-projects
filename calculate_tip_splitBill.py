print("welcome to tip calculator..")

bill = float(input("enter your bill :"))
tip = int(input("how much tip would you like to give? 10,12 or 15 ?:"))
people  = int(input("how maney are split the bill: "))

#calculation
cal_tip = tip/100 * bill
tot_bill_with_tip = cal_tip+bill
bill_per_person = tot_bill_with_tip/people

#total amount
# split_amount =round(bill_per_person,2)
# Each person have to pay : 33.6

"or"
#(:.2f) this will return two place o/p '33.60' instead '33.6'
split_amount = "{:.2f}".format(bill_per_person)
#Each person have to pay : 33.60
print("Each person have to pay : "+str(split_amount))

print(f"the total bill with tip: {tot_bill_with_tip}")

"""o/p=>
welcome to tip calculator..
enter your bill :150
how much tip would you like to give? 10,12 or 15 ?:12
how maney are split the bill: 5
Each person have to pay : 33.60
the total bill with tip: 168.0
"""
