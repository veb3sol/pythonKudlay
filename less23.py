# Урок 23.
# Словари

# словари - неупорядоченная коллекция с доступом по ключу -- как в js обьекты
d = {}      #пустой словарь
print(type(d))      #<class 'dict'>

produkt = {'title': 'Sony', 'price': 100}       # ключи в кавычках
produkt2 = dict(title='iPhone', price = 200)    # используя конструктор

# преобразование списка в словарь
users = [
    ['petr@ukr.net', 'Petr'],
    ['nika@ukr.net', 'Nika'],
    ['lora@ukr.net', 'Lora'],
]

d_users = dict(users)
print(d_users)          #{'petr@ukr.net': 'Petr', 'nika@ukr.net': 'Nika', 'lora@ukr.net': 'Lora'}
# так же можно и с кортежами

# создание словаря из ключей
produkt3 = dict.fromkeys(['price1', 'price2', 'price3'], 20)
print(produkt3)             #{'price1': 20, 'price2': 20, 'price3': 20}. если не указать значение то None

# создание словарей генератором
nums = { i: i+10 for i in range(1, 10)}
print(nums)     #{1: 11, 2: 12, 3: 13, 4: 14, 5: 15, 6: 16, 7: 17, 8: 18, 9: 19}

# получение данных из словаря
print(produkt['title'])     #Sony - если нету то ошибка
print(produkt.get('title'))     #Sony - усли нету то None
print(produkt.get('title', ''))     #Sony - усли нету то Пустая сторока

# перебор словаря
for key in produkt:
    print(key)      #вывод ключа
    print(produkt[key])     # вывод значения

print(produkt.items())      # dict_items([('title', 'Sony'), ('price', 100)])

for key, value in produkt.items():
    print(key)  #вывод ключа
    print(value)    # вывод значения


