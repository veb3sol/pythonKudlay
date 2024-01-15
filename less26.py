# Урок 26.
# Пользовательские функции. Часть 1

def Hello(name):
    print('Hello ' + name)

Hello('Boris')  #Hello Boris
Hello('Valya')  #Hello Valya

# встроенная функция sum
# sum(iterable[, start])
# iterable - обьект который поддерживает иттерацию
# start - с какого числа начинать сумировать - по умолчанию 0
a = sum([])     #0
a1 = sum([1,2,3], 10)       #16

def sum():      #это переопределение существующей встроенной функции
    pass

def get_sum(a, b):
    print(a+b)

x = 2
y = 3
get_sum(4,5)        #9
get_sum(x, y)       #5

# когда функция должна что то возращать
def get_sum1(a, b):
    return a+b

w = get_sum1(6, 5)
print(w)            #11

# если печатать то что вернула функция, которая ничего не возращает - None

