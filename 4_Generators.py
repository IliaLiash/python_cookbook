import itertools
print('----------ЗАДАЧА 1 Свой генератор----------')

def frange(start, stop, step):
    x = start
    while x < stop:
        yield x
        x += step

for i in frange(1, 9, 0.25):    #Вот такое обращение к генератору
    print(i)

print(list(frange(1, 9, 0.25))) #Или такое

a = [1, 2, 3, 4]

for i in reversed(a):   #Аналогично можно сделать и с файлом
    print(i)

print('----------ЗАДАЧА 2 Получение среза итератора----------')

def count(n):
    while True:
        yield n
        n += 1

c = count(0)
for i in itertools.islice(c, 10, 20):
    print(i)

print('----------ЗАДАЧА 3 Итерирование по всем возможным комбинациям. permutations()----------')

items = [1, 2, 3, 4]
for i in itertools.permutations(items):
    print(i)
print('----------')
for i in itertools.combinations(items, 3):
    print(i)

print('----------ЗАДАЧА 4 Итерирование индекс-значение. enumerate()----------')

a = ['a', 'b', 'c', 'd']
for ind, val in enumerate(a, 2):
    print(ind, val)

print('----------ЗАДАЧА 6 Итерирование по нескольким последовательностям. zip(), zip_longest()----------')
print('----------zip() - когда нужны пары----------')


xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]

for x, y in zip(xpts, ypts):
    print(x, y)

a = [1, 2, 3]
b = ['a', 'b', 'c', 'd', 'e', 'f']

for i in itertools.zip_longest(a, b, fillvalue='AAA'):
    print(i)

d = dict(zip(xpts, ypts))
print(d)

zip_list = list(zip(xpts, ypts))
print(zip_list)

print('----------ЗАДАЧА 7 Итерирование по разным контейнерам. chain()----------')
a = [1, 2, 3]
b = ['a', 'b', 'c', 'd', 'e', 'f']

for i in itertools.chain(a,b):
    print(i)

print('----------ЗАДАЧА 8 Превращение вложенной последовательности в плоскую. yiled from----------')
from collections import Iterable

def flatten(items):
    for i in items:
        if isinstance(i, Iterable):
            yield from flatten(i)   #Осуществляем рекурсивный вызов с yiled from
        else:
            yield i

items = [1, 2, [3, 4, [5, 5 , [7, 9]]]]
print(list(flatten(items)))             #Результат генератора нужно оборачивать в list

print('----------ЗАДАЧА 9 Итерирование по слитым объектам. heapq.merge()----------')
import heapq

a = [1, 4, 5, 10]
b = [2, 5, 11, 20]

for i in heapq.merge(a,b):
    print(i)