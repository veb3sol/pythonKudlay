# Списки
l = [1,2,"hello",4,5,True, [5, 2.3], 5.6]
l2 = list("dawer")  # список из строки
print(l2)       #['d', 'a', 'w', 'e', 'r']
l3 = list((1,2,3)) # список с кортежа в круглых скобках
print(l3)

# генераторы списков
jj = 'werter'
l4=[ i for i in jj]
print(l4)   #['w', 'e', 'r', 't', 'e', 'r']

l5 = [ i for i in 'privet nata' if i not in ['a', ' ', 'e', 'u', 'i']]   #в генератор можно добавить условие
l6 = [ i*2 for i in 'privet nata' if i != ' ' and i != 'a']   #в генератор можно добавить условие
print(l5) #['p', 'r', 'v', 't', 'n', 't']
print(l6) # ['pp', 'rr', 'ii', 'vv', 'ee', 'tt', 'nn', 'tt']

# RANGE - ДИАПАЗОН
# range(stop) -- генерация от 0 до stop
# range(start, stop[, step])  -- генерация от start до stop с шагом step
print(list(range(5))) #[0, 1, 2, 3, 4]
print(list(range(2,5,2))) #[2, 4]

for i in range(0, 5):
    print(f'внешний - {i}')
    for j in range(0, 5):
        print(f'\t внутренний - {j}')

# дз - выввод таблицы умножения

for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i} * {j} = {i*j}', end = '\t')
    print('', sep = '\n')