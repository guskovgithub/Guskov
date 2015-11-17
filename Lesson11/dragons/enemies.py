# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    pass


def generate_random_enemyD():
    RandomEnemyType = choice(enemy_typesD)
    enemy = RandomEnemyType()
    return enemy

def generate_random_enemyT():
    RandomEnemyType = choice(enemy_typesT)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemyD() for i in range(enemy_number)]
    return enemy_list

def generate_troll_list(enemy_number):
    enemy_list = [generate_random_enemyT() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зелёный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest

class RedDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'красный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest

class BlackDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'черный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest

class Troll(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer

class TrollGuess(Troll):
    def __init__(self):
        self._health = 200
        self._attack = 30
        self._color = 'желтый'
    def question(self):
        x = randint(1,3)
        self.__quest = 'Угадай число от 1 до 5' 
        self.set_answer(x)
        return self.__quest


class TrollEasyNumber(Troll):
    def __init__(self):
        self._health = 200
        self._attack = 30
        self._color = 'бурый'
    def question(self):
        x = randint(1,300)
        self.__quest = 'напиши целую часть от деления ' + str(x) + ' на 3' 
        self.set_answer(x//3)
        return self.__quest

class TrollDivideNumber(Troll):
    def __init__(self):
        self._health = 200
        self._attack = 30
        self._color = 'розовый'
    def question(self):
        x = randint(1,300)
        self.__quest =  'остаток от деления ' + str(x) + ' на 2' 
        self.set_answer(x%2)
        return self.__quest


     

#FIXME здесь также должны быть описаны классы RedDragon и BlackDragon
# красный дракон учит вычитанию, а чёрный -- умножению.


enemy_typesD = [GreenDragon, RedDragon, BlackDragon]
enemy_typesT = [TrollGuess, TrollEasyNumber, TrollDivideNumber]
