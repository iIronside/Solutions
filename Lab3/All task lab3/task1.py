# Задан простой класс Fraction для представления дробей
# Дополнить класс таким образом, чтобы выполнялся следующий код


class Fraction(object):

    def __init__(self, num, den):  # метод init вызывается при создании
        self.__num = num  # self текущий экземпляр, аналог this
        self.__den = den
        self.reduce()

    def __str__(self):
        return "%d/%d" % (self.__num, self.__den)

    def reduce(self):
        g = Fraction.gcd(self.__num, self.__den)
        self.__num /= g
        self.__den /= g

    def __neg__(self):  # -
        return Fraction(-self.__num, self.__den)

    def __invert__(self):  # ~
        self.__num, self.__den = self.__den, self.__num
        return Fraction(self.__num, self.__den)

    def __pow__(self, p):  # **2
        self.__num = pow(p, self.__num)
        self.__den = pow(p, self.__den)
        return Fraction(self.__num, self.__den)

    def __int__(self):
        buf = int(self.__num/self.__den)  # ?????????????
        return buf

    def __float__(self):   # ?????????????
        buf = self.__num/self.__den
        return buf

    @staticmethod
    def gcd(n, m):
        if m == 0:
            return n
        else:
            return Fraction.gcd(m, n % m)

frac = Fraction(7,2)
print(-frac)
print(~frac)
#print(frac**2)
print(float(frac))
print(int(frac))
