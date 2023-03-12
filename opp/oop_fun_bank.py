class Bank:
    def __init__(self, balance = 0):
        if type(balance) != int:
            raise TypeError('Only integer values accepted as balance !!!')
        self.__balance = balance

    def getBalance(self):
        return self.__balance 

    def setBalance(self, balance):
        self.__balance = balance

    def __str__(self):
        return f'BANK : {self.__balance}'
    
class LocalBank(Bank):
    def __init__(self, locality, balance = 0):
        super().__init__(balance)   # delegation
        self.locality = locality

    def __str__(self):
        return f'Local Bank ({self.locality}) : {self.getBalance}'

###################################################################
world_bank = Bank(1_000_000_000_000)

agro = LocalBank('Chisinau', 1_000_000)

print(world_bank)
print(agro)
               
    