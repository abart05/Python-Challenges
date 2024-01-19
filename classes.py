class bank_account:
    def __init__(self, name, balance, account_type, interest_rate):
        self.name = name
        self.balance = balance
        self.account_type = account_type
        self.interest_rate = interest_rate
    def show_info(self):
        print("Name: ", self.name)
        print("Balance: ", self.balance)
        print("Account Type: ", self.account_type)
        print("Interest Rate: ", self.interest_rate)
    def get_name(self):
        print(self.name)
    def set_name(self,name):
        self.name = name
    def get_balance(self):
        print(self.balance)
    def set_balance(self, balance):
        self.balance = balance
    def set_deposit(self, balance):
        self.balance += balance
    def set_withdraw(self, balance):
        self.balance -= balance
        
andy_b = bank_account("Andy", 1000, "Savings", 4)
phil_h = bank_account("Phil", 3000, "Current", 3)
nicola_b = bank_account("Nicola", 0, "Savings", 5)
 

nicola_b.show_info()
nicola_b.set_deposit(350)
nicola_b.show_info()


# andy_b.show_info()
# andy_b.get_balance()
# andy_b.set_deposit(3000)
# andy_b.get_balance()
# andy_b.show_info()
# andy_b.set_withdraw(1500)
# andy_b.show_info()
 
 
#andy_b.show_info()
#phil_h.show_info()
#andy_b.get_name()