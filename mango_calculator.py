class Calculator():
	#constractor
	def __init__(self):
		while 1:
			try:
				self.n=int(input("Enter the number of mangoes given to harry :"))
				break
			except:
				print("Please enter a valid value !")
				continue
		while 1:
			try:
				self.min=int(input("minimum number of harry's students :"))
				break
			except:
				print("Please enter a valid value !")
				continue
		while 1:
			try:
				self.max=int(input("maximum number of harry's students :"))
				if self.max<=self.min:
					print("maximum number of students can't be less than of equal to minimum number of students !")
					continue
				break
			except:
				print("Please enter a valid value !")
				continue
			#calculator method
	def calculator(self):
					for number in range(self.min, self.max+1):
						if self.n%number!=0:
							print(f"{number} is not a devisor of {self.n}")
						else:
							print(f"{number} a devisor of {self.n}, everyone will got {int(self.n/number)} mangoes")
						
						
calculate = Calculator()
calculate.calculator()
						
				
				
		