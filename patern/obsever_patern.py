from time import sleep

class CentralBankPublisher:
    def __init__(self,):
          # Bank Role
          self.__rates = {
               'EUR_USD': None,
               'USD_EUR': None,
          }
          # OBSERVER ROLE
        #   self.__subscribers = ["Construction Materials Store", "Auto Service 'Victory'"]
          self.__subscribers = []

    def subscribe(self, subscriber):
         self.__subscribers.append(subscriber)

    def notifySubscribers(self):
         for subscriber in self.__subscribers:
              subscriber.update() 

    # HW2: add the unsubscribe (subscriber) method
    def unsubscribe(self, subscriber):
         self.__subscribers.remove(subscriber)   

    def setRate(self, form_currency, to_currency, rate):
        # HW1: use  form_currency, to_currency, -> to set the value
        self.__rates[f'{form_currency}_{to_currency}'] = rate
        ## !!! CODE THAT NOTIFIES !!!
        # self.__rates['EUR_USD'] = rate
        #                       ^
        #                      HERE
        self.notifySubscribers()

    def __str__(self):
        return f'BANK RATES:\n {self.__rates}\n {self.__subscribers}'
                                                    #   ^
                                                    #  list -- __str__ --> for -->repr()
class Subscriber:

    def __init__(self, name):
        self.name = name
    # obj ---> str()
    def __str__(self):
        return f'Company: {self.name}'
    # obj ---> repr()
    def __repr__(self):
        return self.__str__()
    
    def update(self):
        print(f'{self.name} COT THE NOTIFICATION !')
##################################################################################
cb = CentralBankPublisher()
cb.subscribe(Subscriber('Construction Materials Store'))
cb.subscribe(Subscriber('Auto Service \'Victory\''))
# cb.unsubscribe('Auto Service \'Victory\'')  # unsubsribe from the list self.__subscribers = []
cb.setRate('EUR', 'USD', 1.2)
sleep(2)    #timer 2sec.
cb.setRate('USD', 'EUR', 1.1)
print(cb)        
