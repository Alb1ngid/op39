#принципы ООП
# class: atr,methad,dmethod



def a(b,c):...

a(1,2)
a(1,2)
a(3,2)
a(5,2)

# суперкласс родительский класс
class Game:
   высота=100
   ширина=100
   # магический метод для собвственных аргументов
   def __init__(self,name):
      self.name=name

   def __len__(self):
     return len(self.name)

   def __str__(self):
      return self.name

   def run(self):
      print(self.name, 'is run')
game=Game('starwars')
game1=Game('starwars')
game2=Game('starwars')
game3=Game('starwars')
game4=Game('starwars')
game5=Game('starwars')
game6=Game('starwars')
# print(game)
# print(len(game))
# game.run()
# game1.stop()
p='12345'
# принципы ооп 3-4 НАСЛЕДОВАНИЕ Полиморфизм
# полиморфизм это изменение поведения унаследованных методов.аргументов

# Дочерний класс
class Game2(Game):
   def __init__(self,name,age):
      Game.__init__(self,name)
      # super().__init__(name)
      self.age=age
   def stop(self):
      print(self.name,' stop')
      # DRY
   def run(self):
      super().run()
      self.stop()


game22=Game2('flappybird',29)
# game22.run()
print(game22)