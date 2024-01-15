
# дз - выввод таблицы умножения

for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i} * {j} = {i*j}', end = '\t')
    print('')


for y in [a for a in [22,33, 44, 55, 66] if a not in [44, 55]]:
    print(y)