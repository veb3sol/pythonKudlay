# Форматирование строк
name = "Jone"
age = 25
print("My name is " + name + " I'm " + str(age))

# Способы форматирования строк
# 1 способ -- именованные маркеры
print('My %(n)s is name I\'m %(a)d' % {'n': name, 'a': age})
# 2 способ -- позиционные маркеры
print('My %s is name I\'m %d' % (name, age))
print('Title: %s, price: %f' % ("Sony", 50))  # Title: Sony, price: 50.000000
print('Title: %s, price: %.2f' % ("Sony", 50))  # Title: Sony, price: 50.00

# 3 способ -- FORMAT -- появился в python3
print('My name is {}. I\'m {}'.format(name, age))
print('My {1} name is {0}. I\'m {1}'.format(name, age))  # My 25 name is Jone. I'm 25
print('My name is {n}. I\'m {a}'.format(n = name, a = age))  # My name is Jone. I'm 25

# 4 способ -- F-strings
print(f'My name is {name}. I\'m {age}')
print(f'5+2={5 + 2}')  # 5+2=7
