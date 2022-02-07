import  random as ran
import os
mac_chs = ran.choice(range(3))
f1 = "computer"
f2 = "you"
if os.path.exists(f"{f1}.txt"):
	os.remove(f"{f1}.txt")
if os.path.exists(f"{f2}.txt"):
	os.remove(f"{f2}.txt")
i = 0
list = ["stone", "paper", "scissor"]

def fun(you_chs):
		print()
		print(f"You selected {list[you_chs]}")
		global use
		use = mac_chs
		if you_chs == mac_chs:
			print(f"\nComputer also selected {list[you_chs]} \n\nTry again !!\n")
			print()
			global i
			i -= 1
			return None
		elif mac_chs == 0:
			if you_chs == 1:
				return f2
			else:
				return f1
		elif mac_chs == 1:
			if you_chs == 0:
				return  f1
			else:
				return f2
		else:
			if you_chs == 0:
				return f2
			else:
				return f1
					
	
	
		

while i < 5:
	print("Enter:\n 1 to choose stone \n 2 to choose paper \n 3 to choose scissor")
	try:
		you_chs = (int(input("Select: ")) - 1)
		i += 1
		need = fun(you_chs)
		
		def prn():
			global fl1
			global fl2
			print()
			print(f"Computer selected {list[use]}")
			print()
			print(need.capitalize(), "own !")
			print()
			fl1 = open(f"{f1}.txt", "a")
			fl2 = open(f"{f2}.txt", "a")
		if need == None:
			continue
		
		
		elif need == f1:
			prn()
			fl1.write("1\n")
			fl2.write("0\n")
		else:
			prn()
			fl1.write("0\n")
			fl2.write("1\n")
		fl1.close()
		fl2.close()
	except:
		print("\nPlease enter a valid input !\n")
		continue
fl1 = open(f"{f1}.txt")
fl2 = open(f"{f2}.txt")
print("""
*********************~SCORE~***************************************""")
print("\t    Computer\t       You")
for x in range(10):
		print("\t\t" + fl1.readline().replace("\n", " ") + "\t\t" + fl2.readline().replace("\n", " "))
		
		
	
    	
	
