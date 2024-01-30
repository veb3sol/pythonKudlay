# Урок 24.
# Методы словаря

# dict.clear()    -- очищает словарь
# dict().copy()       -- возращает копию словаря
# dict.get(key[, default]) -- возращает значение ключа, если такого ключа нету - default (по умолч None)
# dict.items()    -- возращает пары (ключ, значение)
# dict.keys()     -- возращает ключи в словаре
# dict.pop(key[, default ])     -- удаляет ключ и возращает значение, если ключа нет - default(по умолч - исключение)
# dict.popitem() - удаляет и возращает пару(ключ, значение), если словарь пуст - бросает исключение
# dict.setdefault(key[, default])   -- возращает значение ключа, если нету - создает такой ключ со значением default(None)
# dict.update([other])  -- обновляет словарь, добавляя пары (ключ, значение) из other
# dict.values()  -- возращает значения в словаре

produkt = {'title': 'Sony', 'price': 100}

#print(produkt.items())  #dict_items([('title', 'Sony'), ('price', 100)]) - список кортежей ключ-значение
#print(produkt.keys())  #dict_keys(['title', 'price']) - список ключей

#print(produkt.pop('title')) # удалит запись по ключу, вернет значение ключа. если такого ключа нету - ошибка
#print(produkt.pop('title', 'no')) # если такого ключа нету - no
#print(produkt) #{'price': 100}

#print(produkt.popitem()) # убирает любую запись???
#print(produkt)  #{'title': 'Sony'}  - осталась одна запись

#print(produkt.setdefault('title'))  #Sony  и словарь не поменялся
#print(produkt.setdefault('title2'))  #такого ключа нету, он создался в словаре со значением None
#print(produkt.setdefault('title3', 'test'))  #такого ключа нету, он создался в словаре со значением test

produkt.update({'tema': 'babki'})
print(produkt)      # {'title': 'Sony', 'price': 100, 'tema': 'babki'} - добавился ключ-значение
produkt.update({'price': 200})   #{'title': 'Sony', 'price': 100, 'tema': 'babki'}

produkt.update({'price':200})
print(produkt)      #{'title': 'Sony', 'price': 200, 'tema': 'babki'}   - перезаписался

print(produkt.values())     #dict_values(['Sony', 200, 'babki']) -- список значений