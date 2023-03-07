#!/usr/bin/python3
amount, interest = input("Enter amount and interest: ").split()
amount = float(amount)
interest = float(interest)
total = amount
for i in range(1, 11):
	total = total + (total * interest/100)
print('Earnings after ten years = {:.2f}'.format(total))
