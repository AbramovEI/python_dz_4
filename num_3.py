# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

print('Введите количеств элементов списка = ')
n = int(input())
list1 = list()
print()
for i in range (n):
    k = int(input())
    list1.append(k)
print(list1)


list2 = []
for i in range (len(list1)):
    if list1[i] not in list2:
        list2.append(list1[i])
        
print()
print(list2)

