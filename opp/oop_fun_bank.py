class Bank:
    def __init__(self, balance = 0):
        if type(balance) != int:
            raise TypeError('Only integer values accepted as balance !!!')
        self.__balance = balance

    def getBalance(self):
        return self.__balance 

    def setBalance(self, balance):
        super().__init__(balance) # HW1: use the same protection mechanism as in __init__() # but try not to dupicate the code
        self.__balance = balance        
        
    def __str__(self):
        return f'BANK : {self.__balance}'
    
class LocalBank(Bank):
    def __init__(self, locality, balance = 0):
        super().__init__(balance)   # delegation
        self.locality = locality

    def __str__(self):
        return f'Local Bank ({self.locality}) : {self.getBalance()}'   # HW2: Credit bank < bank   # + max_credit_amount  # + credit_percentage 5%
class Credit_bank(Bank):
    def __init__(self, max_credit_amount, credit_percentage):
        super().__init__(balance=0)   # delegation
        self.max_credit_amount = max_credit_amount
        self.credit_percentage = credit_percentage
        cr = int(self.max_credit_amount * (self.credit_percentage/100)+1)
        self.cr = cr

    def __str__(self):        
        return f'Credit amount is {self.max_credit_amount} and interes will be {self.credit_percentage} %, total interes per year {self.cr}. Total credit amount with interes is {self.max_credit_amount + self.cr}'
  
###################################################################
world_bank = Bank(1_000_000_000_000)

agro = LocalBank('Chisinau', 1_000_000)

credit_1 = Credit_bank(99_000, 5)

print(world_bank)
print(agro)
print(credit_1)     
