class Bank:
    def __init__(self,acNo,acName,branchName):
        print("Welcome to our Bank")
        self.accountNumber = acNo
        self.accountName = acName
        self.brachName = branchName
        self.amount = 5000


    def withdraw(self,amount):
        self.amount = int(self.amount - amount)
        return self.amount

    def deposit(self,amount):
        self.amount = int(self.amount + amount)
        return self.amount

    def checkBalance(self):
        print("Your bank balance is Rs",self.amount)
        return None
person1 = Bank("31232020","Mahudoom Naian","SBI")
person1.checkBalance()
print(person1.deposit(2000))
print(person1.withdraw(5000))
