c = 'C:\d\new.txt'   # \n -- перенос строки
print(c)

c1 = r"C:\d\new.txt"   # r -- обьявляем строку сырой и переноса строки нету
print(c1)

# конкатенация строк
s = 'aaa' 'ssss'
print(s) #aaassss
a1 = 'ffff'
a2 = 'xxxx'
a3 = a1+a2

name = 'Vasya'
age = 26
print('my name is '+name+"I'm "+str(age))

#умножение строк
print("rer "*3)  #rer rer rer

st = 'Приветик'
print(st[0:5])  #Приве
# st[-1]    - последний символ
# st[X:Y:Z] X - начало, Y - конец, Z - шаг
# st[2:] -  от 2 до конца строки
# st[:4] -  от начала до 4 эл строки
# st[::-1] -  строка наоборот
