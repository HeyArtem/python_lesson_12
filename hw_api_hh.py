import requests
import pprint

'''
ДЗ к главе 12 работа с API

Код принимает название города и профессию
Выдает среднюю зарплату и самые основные навыки с указанием % встречаемости






LIGHT:

Используя HH API, рассчитать среднюю зарплату в Москве по запросу "Python"

PRO:

Составить список релевантных навыков по вакансиям Python-разработчик. Алгоритм решения примерно следующий:

1) получаем список вакансий;

2) очищаем тексты описания вакансий и требования вакансий;

3) составляем список релевантных навыков (python, django, sql и т.д.);

4) считаем частоту появления ключевых слов в текстах вакансий;

5) выводим ТОП-10 навыков и процент их встречаемости пользователю.

Желательно сделать сервис универсальным относительно запросов и списка навыков. Проверить для других запросов вакансий и навыков.


Релевантность означает способность информации соответствовать потребностям пользователя.
Релевантный - способность соответствовать чему-либо, быть существенным, важным, уместным


Язык запросов на HH: https://hh.ru/article/1175
'''


url = 'https://api.hh.ru/vacancies'

def f_vacancies(page, search):
    '''Зарплата на одной странице'''
    salary = []
    params = {'text': f'{search}', 'page': page}
    vacancies = requests.get(url, params=params).json()
    for item in vacancies['items']:
        start, stop = 0, 0
        if item['salary'] and item['salary']['currency'] == 'RUR':
            if item['salary']['from'] and item['salary']['to']:
                start = int(item['salary']['from'])
                stop = int(item['salary']['to'])
            elif item['salary']['from'] and not item['salary']['to']:
                start = int(item['salary']['from'])
                stop = start
            elif not item['salary']['from'] and item['salary']['to']:
                stop = int(item['salary']['to'])
                start = stop
        if (start + stop) / 2 > 0:
            salary.append((start + stop) / 2)
    return salary

def f_snippet(page, search):
    '''Навыки на одной странице'''
    snippet = [] # здесь сохраняю навыки от соискателя
    params = {'text': f'{search}', 'page': page}
    vacancies = requests.get(url, params=params).json()
    for item in vacancies['items']:
        if item['snippet']['requirement']:
            snippet.append(item['snippet']['requirement'])
    return snippet


search = input('Введите вакансию и город: ')
data = search.split()
search = ' AND '.join(data)
params = {'text': f'{search}'}
pages = requests.get(url, params=params).json()['pages']

# Зарплата
vacancies = []
for page in range(pages):
     vacancies.extend(f_vacancies(page, search))
if len(vacancies):
     print('Средняя зарплата в рублях: ', sum(vacancies) / len(vacancies))
else:
     print('Нет данных!')

# Навыки
req = [] # список слов
for page in range(pages):
    for char in f_snippet(page, search):
        req.extend(char.split())
print('Навыки первичный грязный список:',req)

sym = [',', '.', ';', ':', '<highlighttext>', '</highlighttext>', '/', ')', '(', 'e.g.'] # первичная грубая очистка текста
for i in range(len(req)):
    for s in sym:
        if s in req[i].lower():
            req[i] = req[i].replace(s, '')

req_resault = [item.lower() for item in req if item]

sym = ['и', 'знание', 'с', 'на', 'работы', 'приветствуется', 'в', 'and', 'автоматизации', 'разработки', 'или', 'программирования',
       'данных', 'понимание', 'умение', 'от', '-', 'знания', 'лет', 'навыки', 'языков', 'владение', 'будет',
       'написания', 'уверенное', 'уровне', 'для', 'по', 'принципов', 'из', 'плюсом', 'желательно', 'работать', 'высшее',
       '3', 'языка', 'r', 'не', 'скриптов', 'experience', 'систем', 'как', 'желание', 'года', 'базовые', 'in',
       'анализа'] # вторичная очистка
for i in range(len(req_resault)):
    for s in sym:
        if s == req_resault[i].lower():
            req_resault[i] = req_resault[i].replace(s, '')

req_resault = [item.lower() for item in req_resault if item]

my_dict = {}
for k in req_resault:
  my_dict[k] = req_resault.count(k)

resault = list(my_dict.items())
resault.sort(key=lambda x: x[1], reverse=True)
print('\n\tНавык и количесво вхождений\n',resault)

number = sum([i[1] for i in resault[:20]])

print('\n\tНавыки и % встречаемости:')
for item in resault:
    if item[1] > 75: # потому что навык Pandas был на 75 месте
        print(item[0], 100*item[1]/number) # убрать and и автоматизация, отправить на проверку
