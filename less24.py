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

produkt.update({'tema': 'babki'})
print(produkt)      # {'title': 'Sony', 'price': 100, 'tema': 'babki'} - добавился ключ-значение

produkt.update({'price':200})
print(produkt)      #{'title': 'Sony', 'price': 200, 'tema': 'babki'}   - перезаписался