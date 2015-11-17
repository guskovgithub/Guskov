# coding: utf-8
# license: GPLv3
from gameunit import *


class Hero(Attacker):
     def __init__(self,name): 
        self._experience = 0
        self._health = 100
        self._name = name
        self._attack = 50 

     def attack(self, target):
        target._health -= self._attack
        self._experience += self._attack


     def gameOver(self):
          pass
  

#FIXME:
"""В этом файле должен быть описан класс героя, унаследованный от Attacker
Герой должен иметь 100 поинтов здоровья, атаку 50, опыт 0, имя, задаваемое в конструкторе
Метод attack должен получать атрибут target и уменьшать его здоровье на величину атаки.

"""
