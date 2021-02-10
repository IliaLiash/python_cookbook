from statistics import mean
import random
print('СПИСОК КЛЮЧЕВЫХ СЛОВ')
print('----------ЗАДАЧА 1 x, y = p----------')
'''
Задача
У вас есть кортеж из N элементов или последовательность, которую вы хотите распаковать в коллекцию из N переменных.
ИСПОЛЬЗУЕМ РАСПАКОВКУ ПО ЭЛЕМЕНТАМ
'''

p = (4, 5)
x, y = p
print(x, y)

data = ['Alphabet', 'Microsoft', 8, (2021, 8, 8)]
name_1, name_2, price, date = data
print(name_1, name_2, price, date)

name_1, name_2, price, (year, month, date) = data
print(year, month, date)
print('При несовпадении количества элементов будет выдана ошибка')

print('----------ЗАДАЧА 2 *middle----------')
'''
Задача
Вам нужно распаковать N элементов из итерируемого объекта, но этот объект может содержать
больше N элементов,что вызывает исключение «too many values to unpack»
ИСПОЛЬЗУЕМ ****'''

grades = [5, 4, 8, 9, 12, 10, 9, 11]
def drop_first_last(grades):
    first, *middle, last = grades   #Оставляем только первый и последний элементы, а остальные в список
    return mean(grades)
print(drop_first_last(grades))

record = ('Dave', 'dave@example.com', '058-343231121', '058-32893193')
name, email, *phone_numbers = record    #Переменные со звездочкой всегда будут списком
print(name)
print(phone_numbers)

print('----------ЗАДАЧА 4 heapq, nlargest----------')
'''
Задача 4
Вы хотите создать список N максимальных или минимальных элементов коллекции.
'''
import heapq
nums = [random.randint(0, 100) for i in range(10)]
print(heapq.nlargest(3, nums))  #Возвращает список
print(heapq.nsmallest(3, nums)) #Возврщает список
print(heapq.nlargest(3, nums)[0])  #Обращение к элементу

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
        ]

cheap = heapq.nsmallest(3, portfolio, key=lambda x:x['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda x:x['price'])
print(cheap, expensive, sep='\n')

print('----------ЗАДАЧА 6 DefaultDict, append----------')
'''
Задача
Вы хотите создать словарь,который отображает ключи на более чем одно значение
(так называемый «мультисловарь», multidict).
Прим.:
e = {
'a' : {1, 2, 3},
'b' : {4, 5}
}   - этот код создает множество
'''
from collections import defaultdict
d = defaultdict(list)   #Каждому новому ключу будет присвоен тип объекта внутри ()
d['a'].append(1)
d['a'].append(2)
d['b'].append(3)
print(d)

d = defaultdict(list)
pairs = [('Google', 5), ('Microsoft', 1), ('Apple', 3)]
for key, value in pairs:    #работаем с последовательностями
    d[key].append(value)
print(d)

print('----------ЗАДАЧА 7 OrderedDict----------')
'''
Задача
Вы хотите создать словарь, который позволит контролировать порядок элементов
при итерировании по нему или при сериализации. Чтобы контролировать порядок элементов в словаре, вы можете использовать
OrderedDict из модуля collections. При итерировании он в точности сохраняет изначальный порядок добавления данных
'''
from collections import OrderedDict
d = OrderedDict()
d['number one'] = 1
d['number two'] = 2
d['What a miracle!'] = 'OrderedDict'
print(d)
for k in d:
    print(k, d[k])

print('----------ЗАДАЧА 8 Вычисления со словарями. ZIP----------')
'''
Задача
Вы хотите проводить различные вычисления (например, поиск минимального
и максимального значений, сортировку) на словаре с данными.
'''
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
    }

print(list(zip(prices.values(), prices.keys())))        #zip нужно обернуть в list, чтобы получить список
min_price = min(zip(prices.values(), prices.keys()))    #Внутри zip сначала ключ, потом значение
max_price = max(zip(prices.values(), prices.keys()))
#ZIP создает итератор
print(min_price, max_price)
print(sorted(zip(prices.values(), prices.keys())))

print('----------ЗАДАЧА 9 Поиск общих элементов в двух словарях. set, &----------')
print('Малоизвестная особенность .keys(), .items(), заключается в том, \
что они поддерживают набор операций над множествами: объединения, пересечения, разности.','\n',
'.values() не поддерживает операций над множествами, т.к. значения м.б. и не уникальными.', sep='')
'''
Задача
У вас два словаря, и вы хотите выяснить, что у них общего (одинаковые ключи,
значения и т. п.)
'''
a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
    }

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
    }

print('Общие ключи:')
print(a.keys() & b.keys())
print('Ключи, которые есть в a, но которых нет в b:')
print(a.keys() - b.keys())
print('Находим общие пары (key,value):')
print(a.items() & b.items())
print('Создаем новый словарь, из которого удалены некоторые ключи:')
c = {key: a[key] for key in a.keys() - {'z', 'w'}}  #key: a[key] - задание ключ-значение словаря
print(c)

print('----------ЗАДАЧА 10 удаление дубликатов с сохранением порядка элементов. dedupe----------')
print('Можно использовать set(), но в этом случае будет нарушен порядок')
'''
Задача
Вы хотите исключить дублирующиеся значения из последовательности, но при
этом сохранить порядок следования оставшихся элементов.
'''

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item      #Выпускаем item
            seen.add(item)  #И добавляем его в seen

a = [1, 5, 2, 1, 9, 1, 5, 10]
res = list(dedupe(a))   #оборачиваем результат в List
print(res)

print('----------ЗАДАЧА 11 присваивание имен срезам slice(), indices()----------')
'''
Ваша программа превратилась в нечитабельную массу индексов срезов, и вы хотите все это расчистить.
'''

record = '0123456789012345678901234567890123456789012345678901234567890'
#cost = int(record[20:32]) * float(record[40:48])
SHARES = slice(30, 32)  #slice() создает объект среза, по указанным значениям
PRICE = slice(46, 48)
#STEP_SLICE = slice(10, 50, 2) #slice с шагом
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)

items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2,4)
print(items[2:4])
print(items[a])
items.append(items[a])  #append() with slice()
print(items)

'''
indices() - возвращает кортеж (start, stop, step), где все значения соответственно ограничены,
чтобы вписаться в границы и не получить IndexError
'''
s = 'Hello World'
a = slice(0, 20, 2)
for i in range(*a.indices(len(s))):
    print(s[i])

print('----------ЗАДАЧА 12 определение наиболее часто встречающихся элементов. Counter(), most_common()----------')
from collections import Counter
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
    ]

word_count = Counter(words) #Создаем словарь
top_three = word_count.most_common(3)   #Список из трех популярных элементов
print(word_count)
print(top_three)
print(word_count['look']) #Обращаемся по ключу - получаем количество вхождений

print('Малоизвестная возможность экземпляров Counter состоит в том, что они могут\
быть легко скомбинированы с использованием разнообразных математических операций +, -')

a = Counter({'eyes': 8, 'the': 5, 'look': 4, 'into': 3, 'my': 3, 'around': 2,
"you're": 1, "don't": 1, 'under': 1, 'not': 1})
b = Counter({'eyes': 1, 'looking': 1, 'are': 1, 'in': 1, 'not': 1, 'you': 1,
'my': 1, 'why': 1})
print(a + b)    #Складываем счетчики
print(a - b)    #Вычитаем счетчики

print('----------ЗАДАЧА 13 сортировКа списка словарей по общему ключу key=itemgetter()----------')
'''
Задача
У вас есть список словарей, и вы хотите отсортировать записи согласно одному
или более значениям.
'''
from operator import itemgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    ]

rows_by_fname = sorted(rows, key=itemgetter('fname'))   #Сортировка по ключу 'fname'. Оборачиваем в sorted()
rows_by_uid = sorted(rows, key=itemgetter('uid'))       #Сортировка по ключу 'uid'
print(rows_by_fname)
print(rows_by_uid)

print('itemgetter() может принимать несколько ключей:')
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname')) #Сортировка по двум ключам
print(rows_by_lfname)
print("itemgetter() может быть заменен: lambda x: x['fname']")
print(max(rows, key=itemgetter('uid'))) #Получаем максимальное значение по ключу
print("Атрибут itemgetter('в кавычках')")

print('----------ЗАДАЧА 14 сортировКа объеКтов, не поддерживающих сравнение lambda, attrgetter()----------')
class User:
    def __init__(self, user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(12), User(23), User(54)]
print('lambda:', sorted(users, key=lambda x: x.user_id))            #ИСпользование lambda для сортировки

from operator import attrgetter
print('attrgetter:', sorted(users, key=attrgetter('user_id')))      #Сортировка по значению атрибута класса
print('attrgetter также работает с несколькими полями')

print('max, attrgetter:', max(users, key=attrgetter('user_id')))    #Получаем max атрибут
print('min, attrgetter:', min(users, key=attrgetter('user_id')))    #Получаем min атрибут

print('----------ЗАДАЧА 15 группирование записей на основе полей groupby(), itemgetter()----------')
rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
        ]   #Хотим проитерировать по группам данных, объединенных общей датой

from itertools import groupby
rows = sorted(rows, key=itemgetter('date')) #Сначала выполняем сортировку - ОБЯЗАТЕЛЬНО
for date, items in groupby(rows, key=itemgetter('date')):   #Итерируем в группах. Указываем date, затем items
    print(date) #Печатаем по чему группируем, т.е. дату
    for i in items:
        print(i)    #Печатаем сами элементы
print('groupby() проверяет только последовательные элементы!')

'''
Важным предварительным шагом является сортировка данных по интересующему полю.
Поскольку groupby() проверяет только последовательные элементы,
без предварительной сортировки группировка записей выполнена не будет.
'''

print('Решение через defaultdict:')
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)
for i in rows_by_date['07/01/2012']:
    print(i)


print('----------ЗАДАЧА 16 фильтрование listcomp, gencomp, compress----------')
'''
Задача
У вас есть данные внутри последовательности, и вы хотите извлечь значения или
сократить последовательность по какому-либо критерию
'''

mylist = [-3, -4, 1, 2, 4, 5, 7, 8, 11, 25]
print([i for i in mylist if i > 0]) #listcomp
print([i for i in mylist if i < 0])
print([i**2 for i in mylist if i < 0])

pos = (i for i in mylist if i > 0)  #gencomp
for element in pos:
    print(element)

clip_neg = [i if i > 0 else 0 for i in mylist]  #listcomp с условие
print(clip_neg)

print('Применение результато фильтрования compress')
from itertools import compress
addresses = [
        '5412 N CLARK',
        '5148 N CLARK',
        '5800 E 58TH',
        '2122 N CLARK',
        '5645 N RAVENSWOOD',
        '1060 W ADDISON',
        '4801 N BROADWAY',
        '1039 W GRANVILLE',
        ]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
more5 = [i > 5 for i in counts] #Фильтруем последовательность - создаем последовательнотсь булевых значений
print(more5)
print(list(compress(addresses, more5)))

print('----------ЗАДАЧА 17 извлечение подмножества из словаря, dictcomp----------')
'''
Задача
Вы хотите создать словарь, который будет подмножеством другого словаря.
'''
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
    }

p1 = {key: value for key, value in prices.items() if value > 200}
tech_names = ['AAPL', 'IBM', 'FB']
p2 = {key: value for key, value in prices.items() if key in tech_names}
print(p1)
print(p2)

print('----------ЗАДАЧА 18 отображение имен на последовательность элементов, namedtuple----------')
'''
Задача
Заменить доступ по позиции доступом по имени 
'''
from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined']) #Создаем "класс" namedtupe. 'Subscriber' - имя
sub = Subscriber('example@example.com', '21.03.2020')
print(sub.addr)
print(sub.joined)

Stock = namedtuple('Stock', ['name', 'price'])
def cost(records):          #На вход будут подаваться записи вида [('AAPL', 500), ('FB', 450)]
    total = 0
    for rec in records:
        s = Stock(*rec)     #Оборачиваем запись в namedtupe
        total += s.price
    return total
print(cost([('AAPL', 500), ('FB', 450)]))   #950

print('----------ЗАДАЧА 19 преобразование и свертка данных, sum(gencomp), max(gencomp)----------')
'''
Задача
Вам нужно выполнить функцию сокращения (т. е. sum(), min(), max()), но сначала
необходимо преобразовать или отфильтровать данные.
'''

nums = [1, 2, 3, 4, 5]
s = sum(x*x for x in nums)
print(s)

s = ('AAPL', 50, 8)
print(','.join(str(x) for x in s))

portfolio = [
    {'name':'GOOG', 'shares': 50},
    {'name':'YHOO', 'shares': 75},
    {'name':'AOL', 'shares': 20},
    {'name':'SCOX', 'shares': 65}
    ]
print('Похожие варианты, с разным выводом: ')
print(min(x['shares'] for x in portfolio))
print(min(portfolio, key=lambda x: x['shares']))

print('----------ЗАДАЧА 20 объединение нескольких отображений в одно, ChainMap----------')
'''
Задача
У вас есть много словарей или отображений, которые вы хотите логически объединить в одно отображение
'''
print('ChainMap принимает несколько отображений и делает их логически единым целым')
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

from collections import ChainMap
c = ChainMap(a,b)   #Связываем два словаря логически
print(c['x'])   #Из a
print(c['y'])   #Из b
print(c['z'])   #Из b
print(list(c.keys()))
print(list(c.values()))

print('В случае появления одинаковых ключей будут использованы значения из первого словаря')
print('В качестве альтернативы ChainMap можно использовать .update()')