print('----------ЗАДАЧА 1 разрезание строК различными разделителями. re.split()----------')
'''
Задача
Вам нужно разделить строку на поля, но разделители (и пробелы вокруг них)
внутри строки разные.
'''
import re
text = 'asdf fjdk; afed, fjek,asdf, foo'
split_list = re.split(r'[;,\s]\s*', text)
print(split_list)

print('----------ЗАДАЧА 2 поиск строк. startswith, endswith((...)), listcomp----------')
'''
Задача
Вам нужно проверить начало или конец строки на присутствие неких текстовых
шаблонов, таких как расширения файлов, схемы URL и т. д.
'''
print('В startswith, endswith((...)) передается обязательно кортеж')

filename = 'spam.txt'
print(filename.startswith('sp'))
print(filename.endswith('.txt'))
print(filename.startswith('spq'))

filenames = [ 'Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h' ]
file_list = [i for i in filenames if i.endswith(('.c', '.h', '.py'))]      #Передаем кортеж расширений файлов
print(file_list)

from urllib.request import urlopen
def read_data(link):
    if link.startswith(('http', 'ftp')):
        return urlopen(link).read()
    else:
        with open(link, 'r') as f:
            return f.read()

print('----------ЗАДАЧА 3 поисК строК с использованием масоК оболочКи. fnmatch(), fnmatchcase(), listcomp----------')
print('fnmatch() - ниша между простым поиском и re')
from fnmatch import fnmatch, fnmatchcase
print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Data45.csv', 'Data[0-9]*'))

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
names_list = [i for i in names if fnmatch(i, '*.csv')]      #Dat*.csv, *.csv и любые другие варианты
print(names_list)

print(fnmatch('foo.txt', '*.TXT'))      #Не учитывает регистр txt, TXT
print(fnmatchcase('foo.txt', '*.TXT'))  #Ищет точное совпадение регистра

print('----------ЗАДАЧА 4 поисК совпадений и поисК теКстовых паттернов regex----------')
text = '27/12/2020'
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text):
    print('yes')

text2 = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(re.findall(datepat, text2))

print('----------ЗАДАЧА 5 поисК текста. replace(), sub()----------')
text1 = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
subs = re.sub(r'\d+/\d+/\d+', '\-,\-,\-', text1)
datepat = re.compile(r'\d+/\d+/\d+')
print(datepat.sub('\-,\-,\-', text1))
print(subs)

print('----------ЗАДАЧА 6 поисК текста без учета регистра IGNORECASE----------')
text = 'lower python, UPPER PYTHON, mixed Python'
data = re.findall('python', text, flags=re.IGNORECASE)
print(data)
data = re.sub('python', 'snake', text, flags=re.IGNORECASE)
print(data)

print('----------ЗАДАЧА 7 нежадный поиск. *, *? - нежадный поиск----------')
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))
text1 = 'Computer says "no." Phone says "yes"'
print(str_pat.findall(text1))
str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text1))

print('----------ЗАДАЧА 11 Срезание строк и символов. strip("-="), lstrip(), rstrip()----------')
s = '    how are you?   \n'
print(s.strip())
s = '----how are you?===='
print(s.lstrip('-'))
print(s.rstrip('='))
print(s.strip('-='))    #Два аргумента
s = '    how   are            you?   \n'
print(s.strip().replace(' ',''))

print('----------ЗАДАЧА 12 Чистка-переводчик. dict translate(remap)----------')
s = 'pýtĥöñ\fis\tawesome\r\n'
remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None     #Удален
}
a = s.translate(remap)
print(a)

import unicodedata
b = unicodedata.normalize('NFD', a)
b.encode('ascii', 'ignore').decode('ascii')
print(b)

print('----------ЗАДАЧА 13 Выравнивание. ljust(), rjust(), format()----------')
s = 'PYTHON IS AWESOME!'
print(s.ljust(28,'*'))
print(s.rjust(28,'*'))
print(s.center(28,'*'))

print('----------ЗАДАЧА 14 Конкатенация. join(), +, format(), sep----------')
print('join() предпочтительней +')
data = ['AAPL', 50, 91.1]
print(','.join(str(i) for i in data))

print('a', 'b', 'c', sep=':')   #Предпочтительней

print('----------ЗАДАЧА 16 Фиксированное количество колонок. textwrap----------')
s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

import textwrap
print(textwrap.fill(s,70))
print(textwrap.fill(s,20))
print(textwrap.fill(s,70, initial_indent=' '))
print(textwrap.fill(s,40, subsequent_indent=' '))




