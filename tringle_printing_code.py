import copy

while(1):
	while(1):
		try:
			n = int(input("Enter any number: "))
			x = copy.deepcopy(n)
			break
		except Exception as e:
			print("Please enter an valid number")
			continue
		
	while(1):
		try:
			b = int(input("Enter 1 or 0: "))
			if (b==0 or b==1):
				break
			else:
				print("Enter only 0 or 1: ")
				continue
		except Exception as e:
			print("Please enter an valid number")
			continue
			
	i = 1	
		
	if b==0:
		m = bool(False)
	else:
		m = bool(True)
	print("\n")
	if m:
		while(n>=i):
			print(" " * (n - i), end = "")
			print("* " * i)
			i += 1
	else:
		while(n>=i):
			print((x - n) * " ", end = "")
			print("* " * n)
			n -= 1
			
			
	