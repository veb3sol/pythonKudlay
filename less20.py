# Урок 20.
# Кортежи

# Кортеж(tuple) - неизменяемый список

# 1 способ создания кортежа
t1 = (1,2,3)
print(type(t1))     #<class 'tuple'>

# 2 способ создания кортежа - упаковка кортежа
t2 = 4,5,6
print(t2, type(t2)) #(4, 5, 6) <class 'tuple'>

# 3 способ создания кортежа  -- через конструктор
t3 = tuple((1,4,7))  # tuple - принимает 1 аргумент
print(t3)       # (1, 4, 7)

# пустой кортеж или кортеж с 1 элементом
t4 = ()  # пустой кортеж
t5 = (1,)
print(t5, type(t5))     #(1,) <class 'tuple'>

# 4 способ создания
t6 = tuple('hello')
print(t6)       #('h', 'e', 'l', 'l', 'o')
print(t6[1])    # e - обращение такое же как и в списках

# размер кортежа меньше чем размер списка
ss = [11,22,33]
cc = (11,22,33)
print(ss.__sizeof__())  #32 байта
print(cc.__sizeof__())  #24 байта

# Операции над кортежами
tt1 = tuple("Hello")
tt2 = tuple(" wordl")
tt3 = tt1 + tt2     #('H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'd', 'l') - cсложили 2 кортежа
print(tt3)

# длина кортежа
print(len(tt3))     # 11

# доступные методы над кортежами
print(tt3.count('l'))   # 3 таких элемента в кортеже, если нету то 0
#print(tt3.index('o'))   # 4 позиция - первая o в кортеже, если нету - то ошибка

# что бы не получить ошибку при определении индекса символа которого нету в кортеже
if 'a' in tt3:
    print(tt3.index('a'))
else:
    print('No')

# перебор кортежа
for i in tt3:
    if i == ' ':
        continue
    print(i, end = ' ')     #H e l l o w o r d l
print(' ')
# в кортеже могут быть списки - а они изменяемые
z = (10, 11, [44, 55, 66], ['aaa', 'sss', 'ddd'])
print(z, id(z))     #(10, 11, [44, 55, 66], ['aaa', 'sss', 'ddd']) 22683152
z[3][0] = 'ggg'
print(z, id(z))     #(10, 11, [44, 55, 66], ['ggg', 'sss', 'ddd']) 22683152
z[3][0] = 'retro'
print(z, id(z))     #(10, 11, [44, 55, 66], ['retro', 'sss', 'ddd']) 25047640  - эл вложенного списка перезаписался
z[3].append('sara')
print(z, id(z))     #(10, 11, [44, 55, 66], ['retro', 'sss', 'ddd', 'sara']) 24392280 - добавили в вложенный список

# распаковка кортежа
r = (1,2,3,)
x, y, z = r
print(x, y, z)  #1 2 3

# поменять местами значения
n = 10
m = 20
print(n, m) #10 20
n, m = m, n
print(n, m) #20 10