while(1):
	try:
		n = int(input("Enter your number: "))
		break
	except:
		print("Please enter a valid number !")
		continue
def factorial(fac):
		if fac==1:
			return 1
		else:
			return (fac * factorial(fac - 1))
print("Factorial of your number is", factorial(n))
		
		
	