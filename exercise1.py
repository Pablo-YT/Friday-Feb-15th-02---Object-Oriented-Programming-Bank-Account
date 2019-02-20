#Create a BankAccount class
#Every bank account should have balance and interest_rate attributes (instance variables)
#Since we want these fields to be set for every account, you'll need to add an __init__ method to your class
#At this point you should test out creating an instance of your class to make sure it works
#Define a __str__() instance method so you can print bank account objects and see a nice, meaningful string. Make sure this method returns a string, rather than printing it!
#Your class should have an instance method called deposit that accepts one amount argument and adds that amount to the total balance
#Test out your method by calling it on an instance of your class
#There should be a withdraw instance method that accepts one amount argument and subtracts it from the total balance
#Don't forget to test it out!
#Finally, there should be a gain_interest instance method that increases the total balance according to the interest rate.



class BankAccount():
	"""docstring for BankAccount"""
	def __init__(self, name, balance, interest_rate):
		self.balance = balance
		self.interest_rate = interest_rate
		self.name = name
		

	def __str__(self):
		return "{} has a balance of ${} and the interest rate for his account is {}%.".format(self.name, self.balance, self.interest_rate)

	def deposit(self, deposit_amount):
		self.deposit_amount = deposit_amount
		new_balance = self.deposit_amount + self.balance
		return "The new balance is ${}.".format(new_balance)
			
	def withdraw(self, withdraw_amount):
		self.withdraw_amount = withdraw_amount
		new_balance1 = self.balance - self.withdraw_amount 
		return "The new balance is ${}.".format(new_balance1)		

Person = (BankAccount('Josh', 3301.00, 0.01))
print(Person)
print(Person.deposit(30.00))
print(Person.withdraw(10.00))


