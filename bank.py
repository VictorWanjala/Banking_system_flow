# Banking system using OOP
# has a function to show user details 
# child class : bank 
# stores details about the account balance 
# stores details about the amount 
# allos for deposits, withdraw, view balance

#parent class
class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def show_details(self):
        print('personal details')
        print('')
        print('Name', self.name)
        print('Age', self.age)
        print('Gender', self.gender)

#child class
class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0
    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print('Account balance has been updated: $', self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if(self.amount > self.balance):
            print('insufficient funds | Balance available: $', self.balance)
        else:
            self.balance = self.balance - self.amount
            print('Account balance has been updated : $', self.balance)

    def view_balance(self):
        self.show_details()
        print('Account balance has been updated : $', self.balance)

jon = Bank('Jon',34,'Male')
jon.deposit(1000)
jon.withdraw(500)
jon.view_balance()







    


