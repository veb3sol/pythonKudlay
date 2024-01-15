test = None # переменную обьявили, а значение пока не присвоили
print(test)

# множественное присваивание -- распаковка картежа
y, x = (1, 6)

# bool
my_true = True
my_false = False
print(type(my_true)) #class bool
print(type(my_false)) #class bool

# функции приведения к определенному типу данных
# str() int() float()  bool()
w = 5.6
print(w, type(w)) # 5.6 <class 'float'>
w = int(w)
print(w, type(w)) # 5 <class 'int'> -- отбросилась дробная часть