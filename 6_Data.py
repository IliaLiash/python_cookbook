import csv
import pandas as pd
print('----------ЗАДАЧА 1 CSV.----------')
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    # next - заголовки таблицы csv
    headers = next(f_csv)
    print(headers)
    for row in f_csv:
        # Выводит списки
        print(row)

from collections import  namedtuple
with open ('stocks.csv') as f:
    f_csv = csv.reader(f)
    headigns = next(f_csv)
    Row = namedtuple('Row', headigns)       #Используем именованные кортежи. Удобнее - вместо индексов будут имена колонок
    for r in f_csv:
        print(Row(*r))

with open('stocks.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print(row)

with open('stocks.csv') as f:              #Запись из одного файла в другой
    f_csv = csv.reader(f)
    with open('stocks_two.csv', 'w') as g:
        for row in f_csv:
            g_csv = csv.writer(g)
            g_csv.writerow(row)
            print(row)

print('----------ЗАДАЧА 2 JSON. json.dumps(), json.loads()----------')
# Превращение структур Python в JSON
import json
data = {
    'name' : 'ACME',
    'shares' : 100,
    'price': 548.18
}

# Запись
with open ('data.json', 'w') as f:
    json.dump(data, f)

# Чтение
with open('data.json', 'r') as f:
    data = json.load(f)
    print(data)

from collections import OrderedDict
# Обязательны двойные кавычки
s = '{"name": "ACME", "shares": 50, "price": 490.1}'
data = json.loads(s, object_pairs_hook=OrderedDict)
print(data)

# Делаем dump в JSON с сортировкой ключей
print(json.dumps(data, sort_keys=True))

print('----------ЗАДАЧА 3 БД.----------')
# Стандарнтное представление строк данных - последовательность кортежей
stocks = [
    ('GOOG', 100, 251),
    ('AAPL', 40, 284.75),
    ('FB', 25, 214.24),
    ('HPQ', 72, 141.2)
]

# Коннектим БД
import sqlite3
db = sqlite3.connect('database.db')
# Создаем курсор
c = db.cursor()
#c.execute('create table portfolio (symbol char, shares integer, price real)')
#db.commit()
# Вставляем последовательность строк в БД
c.executemany('insert into portfolio values(?,?,?)', stocks)
# Выполняем запросы
for row in db.execute('select * from portfolio'):
    print(row)
# Выполняем другой запрос. Передача min_price в кортеже
min_price = 250
for row in db.execute('select * from portfolio where price >= ?', (min_price,)):
    print('----', row)

print('----------ЗАДАЧА 4 Pandas.----------')
titanic = pd.read_csv('test.csv')
#print(titanic)
columns = ' '.join([str(elem) for elem in titanic.columns])
print(columns)
# Получение диапазона значенмй
print(titanic['Pclass'].unique())
# Фильтрование данных
first_class = titanic[titanic['Pclass'] ==  1]
print(first_class)
print(len(first_class))
# Самые возрастные пассажиры
olds = titanic['Age'].sort_values(ascending=False).head(10)
print(olds)