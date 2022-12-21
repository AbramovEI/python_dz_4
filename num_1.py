# Пользователь вводит число, нужно вывести чило pi с заданной точностью(БЕЗ БИБЛИОТЕК/МОДУЛЕЙ)

print('введие точность числа pi')
n = int(input())


k = 1
pi = 0
for i in range(1000000):
    if i % 2 == 0:
        pi += 4 / k
    else:
        pi -= 4 / k
    k += 2
print()
print(round(pi, n))