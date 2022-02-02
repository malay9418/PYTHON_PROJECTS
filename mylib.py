class Library:
	#constructor
	def __init__(self, library_name, inp_book_list):
		self.name = library_name
		print(f"Welcome to {self.name}")
		self.all_book_list = inp_book_list
		self.availabe_book_list = self.all_book_list.copy()
		self.lended_dict = {}
		print("Availabe books are: ")
		for book in self.all_book_list:
			print(book)
		
	#disply method
	def display_menue(self):
		print()
		print("""Enter:
1 to lend book
2 to return book
3 to publish book
4 to check availablity""")
		while(1):
			user_choose = input("Select: ")
			if user_choose == "1":
				self.lend_book()
			elif user_choose == "2":
				self.return_book()
			elif user_choose == "3":
				self.upload_book()
			elif user_choose == "4":
				self.available_books()
			else:
				print("Please enter a valid input !")
				continue
				
	#availablity
	def available_books(self):
		print("Availabe books are: ")
		for book in self.all_book_list:
			print(book)
		print()
		self.display_menue()
			
	#lend method
	def lend_book(self):
		while(1):
			book_name = input("Enter the name of book you want to lend\n(or enter q to go back to the main menue): ")
			if book_name == "q":
				self.display_menue()
			elif book_name not in self.all_book_list:
				print("Sorry book is not availabe here ! ")
				continue
			elif book_name not in self.availabe_book_list:
				print(f"Currently {self.lended_dict[book_name]} have that book. It's not available !")
				continue
			else:
				lender_name = input("Please enter your name: ")
				print("You lended the book succesfully ! Thank you !")
				self.lended_dict.update({book_name: lender_name})
				self.availabe_book_list.remove(book_name)
				self.display_menue()
			
	#upload book
	def upload_book(self):
		while(1):
			name_book = input("Enter the name of book you want to upload\n(or enter to go back to the main menue): ")
			if name_book == "q":
				self.display_menue()
			elif name_book in self.all_book_list:
				print("This name is alredy registered please enter a different name !")
				continue
			self.all_book_list.append(name_book)
			self.availabe_book_list.append(name_book)
			print("Your book has been published succesfully !")
			self.display_menue()
		
	#return method
	def return_book(self):
		while(1):
			returned_book = input("Enter the book name you want to return\n(or enter q to go back to the main menue): ")
			if returned_book == "q":
				self.display_menue()
			elif returned_book not in self.lended_dict.keys():
				print("Please enter the book name correctly !")
				continue
			else:
				print(f"Thank you {self.lended_dict[returned_book]} for returning the book ")
				print("Your book has been received succesfully !")
				self.display_menue()

#uses
golib = Library("My Library", ["a", "b", "c"])
golib.display_menue()
			


		
	
		
		
		
		