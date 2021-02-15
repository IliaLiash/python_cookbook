import os
from functools import partial

print('----------ЗАДАЧА 1 Заменяем плохие символы. errors----------')
f = open('sample.txt', 'rt', encoding='ascii', errors='replace')    #Заменить нечитаемые символы
g = open('sample.txt', 'rt', encoding='utf-8', errors='ignore')     #Игнорировать

print('----------ЗАДАЧА 2 перенаправление вывода в Файл----------')
with open('sample.txt', 'at') as f:
    print('Hello World!', file=f)

print('----------ЗАДАЧА 3 join, sep, end----------')
row = ('ACME', 50, 51.5)
print(','.join(str(i) for i in row))

print('----------ЗАДАЧА 4 чтение и запись бинарных данных----------')
'''
Вам нужно прочесть или записать бинарные данные, такие как содержимое картинок, звуковых файлов и т. п.
'''
with open ('sample.bin', 'wb') as f:
    f.write(b'Hello World!')

with open('sample.bin', 'rb') as f:
    data = f.read()

b = b'Hello World!'
for i in b:
    print(i)

print('----------ЗАДАЧА 5 запись в Файл, Которого еще нет. xt, xb----------')
'''
Вы хотите записать данные в файл, но только в том случае, если его еще нет в файловой системе.
'''
#with open('somefile', 'xt') as f:
#    f.write('Hello\n')

if not os.path.exists('somefile'):      #Альтернативное решение
    with open('somefile', 'wt') as f:
        f.write('Hello\n')
else:
    print('File already exists!')

print('----------ЗАДАЧА 6 Итерирование по записям фмксмпрванного размера. RECORD_SIZE, iter() и functools.partial()----------')
RECORD_SIZE = 4     #Итерируемся по длине из 4-х символов
with open('sample_one.txt', 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')   #Пороговое значение b'' – то, что будет возвращено при попытке чтения файла, когда будет достигнут его конец.
    for r in records:
        print(r)

print('----------ЗАДАЧА 7 Пути и файлы. os----------')
import os
path = 'C:\\Users\\user\Desktop\PycharmProjects\PythonCookBook\sample_one.txt'
# Получение последнего компонента пути
print(os.path.basename(path))       #sample_one.txt.csv
# Получение имени каталога
print(os.path.dirname(path))        #C:\Users\user\Desktop\PycharmProjects\PythonCookBook
# Соединение компонентов пути
print(os.path.join('tmp', 'data', 'folder_1', os.path.basename(path)))     #tmp\data\sample_one.txt.csv
# Раскрытие домашнего каталога пользователя
print(os.path.expanduser(path))             #C:\Users\user\Desktop\PycharmProjects\PythonCookBook\sample_one.txt
# Отделение расширения файла
print(os.path.splitext(path))               #('C:\\Users\\user\\Desktop\\PycharmProjects\\PythonCookBook\\sample_one', '.txt')

print('----------ЗАДАЧА 8 Проверка существования файла. os.path.exists()----------')
path = 'C:\\Users\\user\\Desktop\PycharmProjects\PythonCookBook'
print(os.path.exists(path))
print(os.path.isfile(path))
print(os.path.isdir(path))
print(os.path.getsize(path))

print('----------ЗАДАЧА 9 Получение содержимого каталога. os.listdir()----------')
names = os.listdir(path)
print(names)

#Получить все обычные файлы
names = [name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]
print(names)

#Получить все каталоги
dirnames = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
print(dirnames)

#Получение всех файлов с указанным расширением
pyfiles = [name for name in os.listdir(path) if name.endswith('.py')]
print(pyfiles)

from fnmatch import fnmatch
pyfiles_1 = [name for name in os.listdir(path) if fnmatch(name, '*.py')]
print(pyfiles_1)