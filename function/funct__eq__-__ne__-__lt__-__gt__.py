class Clock:
    __DAY = 86400  # numar in secunde pentru 1 zi 24h

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Must be integer')
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60           # sec.    
        m = (self.seconds // 60) % 60   # min.    
        h = (self.seconds // 3600) % 60 # sec.
        return f'{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}'
    @classmethod
    def __get_formated(cls, x):
        return str(x).rjust(2, '0')
    
    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TabError('The right Operand must be type integer or Clock ')
        
        return other if isinstance(other, int) else other.seconds
    # metoda analizeaza daca sunt egale val
    def __eq__(self, other):
        sc = self.__verify_data(other)
        return self.seconds == sc
    # metoda analizeaza daca e mai mic
    def __lt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds < sc
    # metoda daca e mai mare, analizeaza
    def __gt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds > sc
    # metoda ce diferentiaza, analizeaza
    def __le__(self, other):
        sc = self.__verify_data(other)
        return self.seconds <= sc

    
c1 = Clock(1000)    
c2 = Clock(2000)
print(c1 == c2)    
print(c1 < c2)    
print(c1 > c2)    
print(c1 <= c2)    