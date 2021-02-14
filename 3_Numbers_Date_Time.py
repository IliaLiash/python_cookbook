import numpy as np
import random
from datetime import datetime, date, timedelta
import calendar

print('----------ЗАДАЧА 1 Вы хотите округлить число с плавающей точкой. round()----------')
print(round(1.231, 2))
a = 16748231
print(round(a, -1), round(a, -2), round(a, -3))

print('----------ЗАДАЧА 2 Избавиться от проблем чисел float. decimal----------')
a = 4.2
b = 2.1
print(a + b == 6.3)
from decimal import Decimal

a = Decimal('4.2')
b = Decimal('2.1')
print(a + b == Decimal('6.3'))

print('----------ЗАДАЧА 4 Форматирование чисел для вывода. format(<^>)----------')
x = 1234.56789
print(format(x, '0.2f'))
print((format(x, '>10.4f')))
print(format(x, '<10.2f'))
print(format(x, '^20.1f'))

print('----------ЗАДАЧА 5 NumPy----------')
ax = np.array([1, 2, 3, 5])
ay = np.array([5, 7, 9, 4])

print(ax * 2)
print(ax + ay)
print(ax * ay)
print(np.sqrt(ax * ay))
print(np.cos(ax + ay))

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

print(a[0])
print(a[:,0])
a[1:3,1:3] += 50
print(a[1:3,1:3])
print(a)

print('----------ЗАДАЧА 6 LinAlg----------')
m = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])
print(m)
print(m.T)
v = np.matrix([[2],[3],[4]])
print(m * v)

print('----------ЗАДАЧА 7 Случайный выбор----------')
values = [1, 2, 3, 4, 5, 6]
print(random.choice(values))
print(random.choice(values))

print(random.sample(values, 2))
print(random.sample(values, 3))

random.shuffle(values)
print(values)

print(random.randint(0,20))
print(random.randint(5,16))

print(random.random())
print(random.random())

print('----------ЗАДАЧА 8 Перевод дней в секунды----------')
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c.days)
print(c.seconds)
print(c.seconds/3600)

a = datetime(2020, 12, 31)
print(a + timedelta(days=10))
b = datetime(2004, 5, 1)
c = a - b
print(c.days)   #Разница между двумя датами

now = datetime.now()
print(now)
print(now + timedelta(minutes=25))

print('----------ЗАДАЧА 9 Сколько дней до пятницы?----------')

def friday(day):
    from_date = int(datetime.strptime(day, '%d.%m.%Y').weekday())
    return 4 - from_date if (4 - from_date >= 0) else 1 + from_date

print(friday('10.01.2021'))

print('----------ЗАДАЧА 10 поисК диапазона дат для теКущего месяца----------')

def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
        _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
        end_date = start_date + timedelta(days=days_in_month)
    return (start_date, end_date)
'''
Этот рецепт работает так: сначала вычисляется дата, соответствующая первому
дню месяца. Быстрый способ сделать это – использовать метод replace() объектов
date или datetime, чтобы присвоить атрибуту days значение 1

Затем функция calendar.monthrange() используется для нахождения количества
дней в рассматриваемом месяце. Модуль calendar весьма полезен для получения
базовых данных о календарях. Функция monthrange() возвращает кортеж, который
содержит день недели и количество дней в месяце.
'''

print('----------ЗАДАЧА 11 Конвертирование строК в даты и время----------')
text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')
print(y)
'''
Метод datetime.strptime() поддерживает множество параметров форматирования,
таких как %Y для года из четырех цифр и %m для месяца из двух цифр.
'''