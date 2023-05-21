













#Домашняя работа №4
#Задача1

list_1 = list()
k = int(input('введите кол-во элементов множества 1= '))
for i in range(k):
    n = int(input())
    list_1.append(n)
    print(set(list_1))
list_2 = list()
r = int(input('введите кол-во элементов множества 2= '))
for i in range(r):
    m = int(input())
    list_2.append(m)
    print(set(list_2))
A = set(list_1)
B = set(list_2)
C = A.intersection(B)
print(f'выдать все числа, которые встречаются в А и В, то есть пересечение множеств: {C}')

#Задача №2
