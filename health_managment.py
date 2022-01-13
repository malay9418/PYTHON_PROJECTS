def getdate():
	import datetime
	return datetime.datetime.now()

print("Available names harry, hamad, malay")
while(1):
	n = input("Please enter your name: ")
	if (n=="malay" or n=="harry" or n=="hamad"):
		print("\nHello", n, "Welcome to your helath managment data center\n")
		break
	else:
		print("Please enter a valid name !")
		continue






def fun(name):
	print("What do you want to do?")
	print("""
Enter
1 for lock data
2 for retreive data""")
	f1 = (name + "exe.txt")
	f2 = (name + "die.txt")
	while(1):
		s = input("Select: ")
		if (s == str(1) or s == str(2)):
			break
		else:
			print("Please enter only 1 or 2 !")
			continue
	if (int(s)==1):
		print(
"""You selected to lock data
what type of data do you want to lock?\n""")
		print("Enter")
		print("1 for exercise")
		print("2 for diet")
		while(True):
			s2 = input("Select: ")
			if (s2 == str(1) or s2 == str(2)):
				break
			else:
				print("Please enter only 1 or 2")
				continue
		if (int(s)==1):
			print("""
You selected for exercise
What type of exercise have you done?""")
			e = input("Enter: ")
			f = open(f1, "a")
			dt1 = (str(getdate()) + ":" + e)
			print(dt1)
			f.write(dt1)
			f.close()
				
		else:
			print("""
You selected for diet
What type of food have you eaten?""")
			e = input("Enter: ")
			f = open(f2, "a")
			dt2 = (str(getdate()) + ":" + e)
			print(dt2)
			f.write(dt2)
			f.close()
	else:
		print("""
You selected to retreive data
what type of data do you want to lock?\n""")
		print("Enter")
		print("1 for exercise")
		print("2 for diet")
		while(1):
			s2 = input("Select: ")
			if (s2 == str(1) or s2 == str(2)):
				break
			else:
				print("Please enter only 1 or 2")
				continue
		if (int(s2)==1):
			try:
				f = open(f1)
				print(f.read())
			except:
				print("Sorry you haven't locked any data yet please lock a data first !")
				fun(n)
		else:
			try:
				f = open(f2)
				print(f.read())
			except:
				print("Sorry you haven't locked any data yet please lock a data first !\n")
				fun(n)
fun(n)
		
	
		
	
	