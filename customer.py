from atm_card import ATMCard

class Customer: 
    def __init__(self,id,CustPin=422022,CustBalance=1000000):
        self.id = id 
        self.pin = CustPin
        self.balance = CustBalance 
    def checkId(self): 
        return self.id 
    def checkPin(self):
        return self.pin
    def checkBalance(self):
        return self.balance 
    def withdrawBalance(self, nominal):
        self.balance -= nominal
    def depositBalance(self, nominal):
        self.balance += nominal
