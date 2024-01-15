# Урок 30.
# Модули в Python

# docs.python.org/3/library     -- описание модулей python

#import os, random # импортировали 2 модуля
import os # импортировали модуль
#import random # импортировали модуль
#import random as r # по псевдониму
# from random import randint, shuffle # импорт нескольких методов
# from random import * # импорт всех методов

import lib

# print(lib.get_count('moloko', 'o'))     #3
# print(lib.get_len('moloko'))    #6

# функции можно помещать в переменные
f = lib.get_len
print(f('solo'))    #4