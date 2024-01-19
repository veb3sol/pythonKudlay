# Урок 18.
# Домашнее задание

# 1
s1 = [1, 2, 3]
# rez = []
# for i in s1:
#     rez.append(i*2)
rez = [x * 2 for x in s1]
print(rez)  # [2, 4, 6]

# 2
ss = [1, 2, 3]
rez2 = []
for i in ss:
    rez2.append(i ** 2)
sum = 0
for j in rez2:
    sum += j
print(sum)  # 14

# 3
time1 = 3
time2 = 6.7
time3 = 11.8
lit = 0.5

litres1 = int(time1 * lit)
litres2 = int(time2 * lit)
litres3 = int(time3 * lit)

print(litres1, litres2, litres3)  # 1 3 5

# 4
sd = "Hello word"
rr = sd.upper() if " " in sd else sd.lower()  # HELLO WORD
print(rr)
