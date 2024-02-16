# наследование полиморф инкапсуляция абстракция

# множественное наследование


class Grand: #родительский
    eat=True
    games = False

class Fat(Grand): #дочерний
    games = True
    def __init__(self,name):
        self.name=name
class Person: #суперкласс
    games=True
    def __init__(self,nickname='Vayne'):
        self.nickname=nickname

class Son(Fat,Person):
    games=False
    def __init__(self,name,nickname):
        Fat.__init__(self,name)
        Person.__init__(self,nickname)





son=Son('brus','batman')

print(son.games)
print(son.name,son.nickname)
# MRO-порядок выполнения методов
print(Son.mro())
# print(dir(son))