#Циклы For и While

i = 1
while i<=10:
    print(i, end = ' ')
    i+=1

# print(*objs, sep=' ', end='\n', file=sys.stdout, flush=False)

print("vasco", 'fut') #vasco fut
print("vasco", 'fut', sep = '!') #vasco!fut

s="asqert fhfhlhl"
for l in s:
    if l == ' ':
        continue        #пропускает текущую итерацию и переходит к следующей
    print(f'"{l}"', end = ' ')   #"a" "s" "q" "e" "r" "t" "f" "h" "f" "h" "l" "h" "l"

d = 'sdfg xcvb'
for j in d:
    if j == ' ':
        break       #выход с цыкла
    print(j, end = ' ')
else:                                   #сработает когда не сработает break
    print('В строке нету пробелов')     # без braek срабатывает всегда вконце цыкла

i2=100
while i2<150:
    print(i2)
    i2+=1
else:
    print('aaaa')  # сработает когда цыкл закончился