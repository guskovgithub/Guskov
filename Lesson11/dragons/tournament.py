# coding: utf-8
# license: GPLv3
from enemies import *
from hero import *
from random import shuffle

def annoying_input_int(message =''):
    answer = None
    while answer == None:
        try:
            answer = int(input(message))
        except ValueError:
            print('Вы ввели недопустимые символы')
    return answer


def game_tournament(hero, enemy_list):
    for enemy in enemy_list:
     if isinstance(enemy, Dragon):
         print('Вышел', enemy._color, 'дракон!')
         while enemy.is_alive() and hero.is_alive():
             print('Вопрос:', enemy.question())
             answer = annoying_input_int('Ответ:')

             if enemy.check_answer(answer):
                hero.attack(enemy)
                print('Верно! \n** дракон кричит от боли **')
             else:
                enemy.attack(hero)
                print('Ошибка! \n** вам нанесён удар... **')
         if enemy.is_alive():
            break
         print('Дракон', enemy._color, 'повержен!\n')


     elif isinstance(enemy, Troll):
         print('Вышел', enemy._color, 'троль!')
         while enemy.is_alive() and hero.is_alive():
             print('Вопрос:', enemy.question())
             answer = annoying_input_int('Ответ:')

             if enemy.check_answer(answer):
                hero.attack(enemy)
                print('Верно! \n** троль кричит от боли **')
             else:
                enemy.attack(hero)
                print('Ошибка! \n** вам нанесён удар... **')
         if enemy.is_alive():
            break
         print('троль', enemy._color, 'повержен!\n')



    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт:', hero._experience)
    else:
        print('К сожалению, Вы проиграли...')

def start_game():

    try:
        print('Добро пожаловать в арифметико-ролевую игру с драконами  и возможно троллями!')
        print('Представьтесь, пожалуйста: ', end = '')
        hero = Hero(input())

        dragon_number = 3
        troll_number = 3
        enemy_list = generate_dragon_list(dragon_number) + generate_troll_list(troll_number)
       
        shuffle(enemy_list)
        #print(enemy_list)
        #assert(len(enemy_list) == 6)
        print('У Вас на пути', dragon_number + troll_number, 'врагов!')
        game_tournament(hero, enemy_list)

    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')
