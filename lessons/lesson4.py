# наследование полиморфизм инкапсуляция обстракция
# super()
# инкапсуляция это создание единого механизма в одном коде
# уровни доступа публичный _защищенный, __скрытый

class BankAccount:
    def __init__(self, name, money, key):
        self.name = name
        self._money = money
        self.__key = key

    # сеттер геттер

    # property
    def sett_moneyKeys(self,a):
        self._money += a

    def getMoney(self):
        print(self._money)

    def __str__(self):
        return f'{self._money},{self.name},{self.__key}'

beka = BankAccount('beka', 100, '20606200300681')
# beka._money = 1000000
# beka._BankAccount__key = 'werty'
#
# print(beka)
# print(dir(beka))

# print(beka)
# beka.sett_moneyKeys(1000)
# print(beka)
beka.getMoney()
beka.sett_moneyKeys(1000)
beka.getMoney()
print(BankAccount.mro())