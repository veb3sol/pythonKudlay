# Урок 30.
# Модули в Python

# docs.python.org/3/library     -- описание модулей python

#import os, random # импортировали 2 модуля
import os # импортировали модуль
import random # импортировали модуль
#import random as r # по псевдониму
from random import randint, shuffle # импорт нескольких методов
# from random import * # импорт всех методов

# print(os.getcwd()) # C:\Users\Ruslan_WORK\PycharmProjects\pythonKudlay -- получили путь к текущей папке
# print(random.random())
# print(random.randint(1,100))

ll = [1,2,3,4,5]
shuffle(ll) #[5, 3, 2, 4, 1] - перемешивает список
print(ll)

import lib

# print(lib.get_count('moloko', 'o'))     #3
# print(lib.get_len('moloko'))    #6

# функции можно помещать в переменные
f = lib.get_len
print(f('solo'))    #4

# если что то печатать в lib и при этом запустить less30 - то оно распечатается

print(__name__) #__main__ -- если запустить этот файл, а если импортировать и там запустить то имя less30