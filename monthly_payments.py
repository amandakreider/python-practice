def calc_car_pymt(amount, doc_fee, down, rate, term):
	total_cost = (amount + doc_fee)*1.0625 + 135
	total_cost = round(total_cost, 2)
	print('The total cost of the car is {}.'.format(total_cost))
	loan_amount = total_cost - down
	mrate = (rate*.01)/12
	payment_amount = (loan_amount*mrate*((1+mrate)**term))/(((1+mrate)**term)-1)
	return payment_amount

user_amount = int(input('What is the price of the car?\n'))
doc_fee_is_449 = input('Is the doc fee 449 (yes or no)?\n')

if doc_fee_is_449 == 'no':
	user_doc_fee = int(input('What is the doc fee?\n'))
else:
	user_doc_fee = 449

user_down = int(input('What is the down payment?\n'))
user_rate = float(input('What is the payment rate? (%)\n'))
user_term = int(input('What is the payment term? (in months)\n'))

car_pmt_amount = calc_car_pymt(user_amount, user_doc_fee, user_down, user_rate, user_term)
car_pmt_amount = round(car_pmt_amount, 2)

interest = (car_pmt_amount*user_term + user_down) - ((user_amount + user_doc_fee)*1.0625 + 135)
interest = round(interest, 2)

interest_per = interest/user_term
interest_per = round(interest_per, 2)

print('The monthly payment for this car will be {}.'.format(car_pmt_amount))
print('The total amount you will pay in interest will be {}.'.format(interest))
print('The total amount you will pay in interest per month will be {}.'.format(interest_per))