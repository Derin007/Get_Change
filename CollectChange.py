def get_change(i, n):
	# i is the value of the product
	# n is the amount customer presented

	convert1 = float(i) * 100
	convert2 = float(n) * 100

	quarter = 25
	dime = 10
	nickel = 5
	penny = 1
	"""countquart = 0
	countdime = 0
	countnickel = 0
	countpenny = 0"""
	countquart = countdime = countnickel = countpenny = 0
	initial_change = convert2 - convert1
	final_change = 0

	while initial_change > 0:
		if initial_change >= quarter:
			initial_change -= quarter
			countquart += 1

		elif initial_change >= dime and initial_change < quarter:
			initial_change -= dime
			countdime += 1

		elif initial_change >= nickel and initial_change < dime:
			initial_change -= nickel
			countnickel += 1

		elif initial_change >= penny and initial_change < nickel:
			initial_change -= penny
			countpenny += 1

		else:
			print("An Error occured somehow!")
			initial_change -= 1

	final_change = (countquart * 25) + (countdime * 10) + (countpenny * 1) + (countnickel * 5)
	if final_change >= 1:
		final_change = float(final_change) / 100
	print("Final change is:", final_change)
	#print(final_change)
	print("Quarter count is: ", countquart)
	print("Dime count is: ", countdime)
	print("Nickel count is: ", countnickel)
	print("Penny count is: ", countpenny)

print("Enter the value of product")
price = input()
print("Present amount greater than price")
amount_tendered = input()
get_change(price, amount_tendered)
#get_change(5, 7.46)

