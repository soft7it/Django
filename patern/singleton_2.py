class DataBase:
##########   SINGLETON ################################    
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        DataBase.__instance = None
##########   SINGLETON ################################
    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'connect with DataBase: {self.user}, {self.psw}, {self.port}')

    def close(self):
        print('shut down connect with DataBase')        

    def read(self):
        return 'data from DataBase'
    
    def write(self, data):
        print(f'records in DataBase {data}')

db = DataBase('root', '1234', 80)        
db2 = DataBase('root2', '56789', 50)

db.connect()
db2.connect()
## CONCLUZIE SINGLE TON: el emite aceeasi valoare pentru unu, nu diferit
# incearca sa faci :
print(id(db), id(db2))
# observi aceeasi adresa id la memorie, nu sau schimbat!!!!
# exemplu https://www.youtube.com/watch?v=-xoT6rntpK0&list=PLA0M1Bcd0w8zPwP7t-FgwONhZOHt9rz9E&index=5
