# концепция ООП

import random,math,turtle

def a():...

a()

class Car:
    #атрибуты класса или свойства класса
    motor=True
    color='white'
    # функция внутри класса называется метод
    # конструктор класса
    def __init__(self,name,age):
        self.name=name
        self.age=age
#     магические методы
    def __str__(self):
        return (f'name is:{self.name} \n'
                f'is {self.age} years')

    def __len__(self):...
# экземпляр либо обьект класса
bmw=Car('bmw',2020)
mers=Car('benz',2023)
mers.color='black'
# print(type(mers))
# print(mers.color)
# print(bmw.motor, bmw.color)
print(bmw)
print(len(mers))
#
# p=2.1,1,'1',True,[],{},(),None
# print(type(p))
#
# o='wertyu'
# o.capitalize()
# print(o.isdigit())
# print(o)
# class float:
