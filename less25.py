# Урок 25.
# Игра угадай число

ch = 6

for i in range(1,4):
    c = int(input(f'угадай число, у тебя {4 - i} попыток'))
    if c == ch:
        print('Победа!')
        break
    elif c > ch:
        print('неправильно, твое число больше')
    else:
        print('Неправильно, твое число меньше')
else:
    print('у тебя закончильсь попытки')