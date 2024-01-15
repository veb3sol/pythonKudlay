from random import randint

while True:
    ch = randint(1,10)
    print(ch)
    t = False
    for i in range(1, 7):
        c = int(input(f'угадай число от 1 до 10, осталось {8-i}'))
        if c == ch:
            print(f'победа, ты угадал с {i} попытки')
            t = True
            break
        else:
            print(f'неправильно, попыток все меньше')
    if t == True:
        y = int(input(f'Ты победил, давай сыграем еще! если ДА, тогда нажми 1, если НЕТ - 0'))
        if y == 1:
            print('Ура! Играем снова!')
        elif y == 0:
            print('Не хочешь играть, ну и не надо')
            break
        else:
            print('Ты ввел какой-то бред, я не хочу с тобой играть, пока')
            break
    else:
        y2 = int(input(f'Ты проиграл, давай сыграем еще! если ДА, тогда нажми 1, если НЕТ - 0'))
        if y2 == 1:
            print('Ура! Играем снова!')
        elif y2 == 0:
            print('Не хочешь играть, ну и не надо')
            break
        else:
            print('Ты ввел какой-то бред, я не хочу с тобой играть, пока')
            break