# Урок 28.
# Пользовательские функции. Часть 3

# документирование функции
def sumka(a, b):
    """
    Возвращает сумму аргументов.

    :param a: первый операнд
    :type a: int
    :param b: второй операнд
    :type b: int
    :return: a+b
    """
    return a + b


print(sumka(45, 78))

# Области видимости (scope)
# переменные определенные в функции - локальные
# переменные определенные вне функции - глобальные

a = 5  # глобальная переменная

# def tyro():
# print(a) #переменная гловальная доступна только на чтение
# a +=1  -- ошибка, глобальную переменную можем только читать
# a = 10
# a +=1       # локальная переменная, она никак не связана с глобальной а

# tyro()

b1 = 7


def serw():
    global b1
    b1 += 1


print(b1)  # 7
serw()
print(b1)  # 8

ll = [1, '2', 3]


def f2(l):
    def get_mas(x):
        return int(x) * 2

    return [get_mas(i) for i in l]


print(f2(ll))  # [2, 4, 6]


# ДЗ
# 1. Написать функцию, которая определит есть ли в списке число - номер индекса под которым находится "odd"

def odd_ball(sl, ll):
    ind = ll.index(sl)
    if ind in ll:
        return True
    else:
        return False


lol1 = ["event", 4, "event", 7, "event", 55, "event", 6, "event", 10, "odd", 3, "event"]
lol2 = ["event", 4, "event", 7, "event", 55, "event", 6, "event", 9, "odd", 3, "event"]
lol3 = ["event", 10, "odd", 2, "event"]

print(odd_ball('odd', lol1))
print(odd_ball('odd', lol2))
print(odd_ball('odd', lol3))


# print(odd_ball(["event", 4, "event", 7, "event", 55, "event", 6, "event", 10, "odd", 3, "event"])) # True
# print(odd_ball(["event", 4, "event", 7, "event", 55, "event", 6, "event", 9, "odd", 3, "event"]))   #False
# print(odd_ball(["event", 10, "odd", 3, "event"]))   #True

#  2. написать функцию, аргумент которой - последнее число в последовательности
# функ вернет суму всех эл последовательности, кратных 3 или 5

def ff(a):
    ee = [i for i in range(1, a + 1) if i % 3 == 0 or i % 5 == 0]
    return sum(ee)


print(ff(5))  # 8
print(ff(2))  # 0


def ff1(a):
    return sum([i for i in range(0, a + 1) if i % 3 == 0 or i % 5 == 0])

print(ff1(10))  # 33

# 3 дан список имен, сделать новый список, в котором имена с первого списка, но только те, которые с 4 букв

names = ["Валя", "Руслан", "Витя", "Валера", "Катя", "Соня", "Иванко"]

def namess(s):
    return [i for i in s if len(i) == 4]

print(namess(names))