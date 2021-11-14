import json
import hashlib

url = "https://en.wikipedia.org/"
file_in = 'files/countries.json'
file_out = 'files/countries.txt'

print('Задание 1')
class MyIterator:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.cursor = None

    def __iter__(self):
        self.cursor = self.start - 1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == self.end:
            raise StopIteration
        return line[self.cursor]['name']['official']


with open(file_in, encoding="UTF-8")as f:
    line = json.load(f)

countrys = MyIterator(0, len(line))
country = [i.replace(' ', '_') for i in countrys]

country_out = []
#  список

for i in country:
    http = url + "wiki/" + i.replace("'", ("")).replace('(', '').replace(')', '')
    #  Получаем ссылку в Википедии, удаляем скобки
    out = f'{i} - {http}'
    country_out.append(out)

with open(file_out, 'w', encoding='UTF-8') as f1:
    for i in country_out:
        f1.write(i+'\n')
    print("Список стран со ссылками на Википедию записан в файл countries.txt \n")


#  Генератор, который принимает путь к файлу.
print('Задание 2')
print('Список хешированных строк из файла со странами:\n')


def generator_h(file):

    with open(file, encoding='UTF-8') as f2:
        line = (i.strip() for i in f2.readlines())
        for i in line:
            i_hash = hashlib.md5(i.encode())
            yield i_hash.hexdigest()
            # При вызове функции-генератора возвращает хеш строки

g = generator_h(file_out)
for i in g:
    #  Пошаговый хэш строк
    print(i)