
#задача1
N = int(input('введите количество элементов в массиве ='))
list_n = list(range(1,N+1))
print(list_n)
x = int(input('введите число x='))
print(list_n.count(x))
#задача2
N = int(input('введите количество элементов в массиве ='))
list_n = list(range(1,N+1))
print(list_n)
x = int(input('введите число x='))
number=[abs(list_n[i]-x) for i in range(len(list_n))]
print(list_n[number.index(min(number))])