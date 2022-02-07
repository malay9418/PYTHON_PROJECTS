
import time
while True:
	try:
		age = input("Please enter your age or year of bearth: ")
		if 1<= len(age) <= 4:
			break
		else:
			raise Exception()
	except:
		print("Please enter a valid input ! ")
		continue
		
		
if 1<=len(age)<=3:
	age = int(age)
	print(f"Your age is: {age}")
else:
	print(f"You entered your birth year {age}")
	age = 2022 - int(age)
	print(f"Your age is: {age}")
	
def quest(age):
	while True:
		try:
			age_query_on = int(input("Enter the year you want to know your age: "))
			if age_query_on<2022:
				raise Exception()
			else:
				print(f"Your age will be {age + (age_query_on - 2022)} on {age_query_on}")
				break
		except:
			print("Please enter a valid year !")
			continue
	
	
if age>110:
		print("WTF! You seems the oldest person alive here ! ")
		exit()
elif age<1:
	print("You haven't borned yet !\nCome after bearth : )")
	exit()
else:
	quest(age)

	
