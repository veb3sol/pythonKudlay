# Урок 16.
# Методы для работы со списками

l = [1,2,3,"hello", ["test", 10], 'word', True]
names = ["Ivanov", "Petrov", "Sidorov"]
print(l[3][0])  # h
print(l[4][0])  # test
print(l[0:3])  # [1, 2, 3]
# Списки - изменяемые последовательности
l[2] = "Privet"

print(len(l))   # 7 - длина последовательности
l[:2] = [10,15]
print(l)        #[10, 15, 'Privet', 'hello', ['test', 10], 'word', True]

# list.append(x) - добавляет эл в конец списка
l.append(55)
print(l)        #[10, 15, 'Privet', 'hello', ['test', 10], 'word', True, 55]

# list.extend(L) - добавляет в конец все эл списка L
L = [77,88,99]
l.extend(L)
print(l)        #[10, 15, 'Privet', 'hello', ['test', 10], 'word', True, 55, 77, 88, 99]
# также списки можно складывать
l2 = ['sss', 13]
l += l2
print(l)

# l.insert(i, x) - вставляет на i - ый элемент значение x
l.insert(1, 100)
print(l)        #[10, 100, 15, 'Privet', 'hello', ['test', 10], 'word', True, 55, 77, 88, 99]

# list.remove(x) -  удаляет первый x в списке, ошибка - если такого нету
l.remove(15)
print(l)    #[10, 100, 'Privet', 'hello', ['test', 10], 'word', True, 55, 77, 88, 99]

# list.pop([i])  -- удалит i элемент и вернет его, если индекс не указать - последний удалит
t = l.pop(3)
print(t)        #hello - удаленный 3 элемент

# list.index(x, [start, [end]]) - вернет положение 1 элемента x в диапазоне
r = l.index(55, 5)
print(r)        #6 - позиция

# list.count(x) - вернет кол x в списке
e = l.count(77)
print(e)    #1 - елемент такой в списке

# list.sort([key=функция], [reverse=False]) - сортирует список на основе функции
h = ['as', 'ad', 'aa']
h.sort()
print(h)        #['aa', 'ad', 'as']  -- в алфавитном порядке

# list.reverse() - разворачивает список
l.reverse()
print(l)

# list.copy() - вернет копию списка
lc = l.copy()
l[0] = 0
print(l, lc)    # это разные списки

# list.clear() - очищает список
l.clear()
print(l)    # пустой список


