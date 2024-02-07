# datetime - основные типы даты и времени
# datetime (модуль)-- date (класс)-- today() (метод)

from datetime import date, datetime, timedelta
import locale

# class date  -- возращает только дату
today = date.today()
print(today)    #2024-02-07 - по умолчанию - английская локаль
print(today.day) # 7
print(today.month) # 2
print(today.year) # 2024
print(today.weekday()) # 2     вс - 0, сб - 6  день недели

# class datetime -- возращает и дату и время
now = datetime.now()
now2 = datetime.today()
print(now, now2) # методы синонимы  2024-02-07 11:13:26.511012 2024-02-07 11:13:26.511013
print(now.day) #7
print(now.month) #2
print(now.year) #2024
print(now.weekday()) #2
print(now.hour) #11
print(now.minute) #21
print(now.second) #51

# получить название дня
days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
print(days[datetime.now().weekday()]) # ср

# strftime()  and strptime() -- получить дату и время используя маркеры
# https://docs.python.org/uk/3.9/library/datetime.html?highlight=time#strftime-and-strptime-behavior
now3 = datetime.now()
print(now3)  #2024-02-07 11:32:49.306516
print(now3.strftime('%a')) #Wed
print(now3.strftime('%A'))  #Wednesday

# для получения названий на русском надо использовать локаль
# locale.setlocale(locale.LC_ALL, "ru-RU.UTF-8")   -- с кодировкой
locale.setlocale(locale.LC_ALL, "ru-RU")   # без кодировки тоже все работает
now4 = datetime.now()
print(now4)  #2024-02-07 11:40:13.374951
print(now4.strftime('%a')) #Ср
print(now4.strftime('%A'))  #среда
print(f'Дата: {now4.strftime("%A %d %b %Y")}') #Дата: среда 07 фев 2024
print(f'Время: {now4.strftime("%H : %M")}') #Время: 11 : 51

print(now4.strftime("%c")) #07.02.2024 11:55:12
print(now4.strftime("%x")) #07.02.2024
print(now4.strftime("%X")) #11:55:12

# class timedelta - разница между двумя временами
now5 = datetime.today()
print(now5.strftime("%c")) #07.02.2024 12:00:41
# прибавим к нашей дате 1 день, 2 часа, 10 минут
d1 = now4 + timedelta(days = 1, hours = 2, minutes = 10)
print(d1.strftime("%c")) #08.02.2024 14:14:32

# ДЗ - разобраться с модулями    os   os.path
# рекурсия и метод walk  ????
# построить дерево с папок и файлов и вывести его в консоль с отступами