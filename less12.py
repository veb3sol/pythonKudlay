#Оператор IF
x = 0
if x:
    print('11111')
else:
    print('222222')

age = int(input('Сколько вам лет? '))
# input -- всегда возращает строку
if age < 18:
    print(f'Тебе {age} лет, ты еще мал')
elif age>=18 and age<=70:
    print(f'Тебе {age} лет, Ты подходишь')
else:
    print(f'Тебе {age} лет, Ты стар')

g = 0
if not g :
    print('111')
else:
    print('2222')

# or, and, not  -- логические операторы

time = 11
if time<12 or time>13:
    print('open')
else:
    print('close')

# тернарных операторов нету, но есть типа подобие
xx = 1
yy = -1 if xx==1 else 2
print(yy)

if 5 == '5':    # нету === поэтому == проверяет по типам!!!
    print('da')
else:
    print('net')