# RealData provider
from random import randint

# data[0]

class _Proxy:
    def __getitem__(self,index):
        data = []
        while len(data) < 10000000:
            data.append(randint(100, 10000))
        return data[index]

def getData():
    return _Proxy()