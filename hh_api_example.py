import requests
import pprint

''''
Глава 12.4 
API HH
'''
URL = 'https://api.hh.ru/vacancies'

''''
Зделаем запрос, где требуются навыки знания на языке питон
'''
params = {'text' : 'Python',
          'page' : 1}
result = requests.get(URL, params = params).json()


'''' Выведем результат '''
pprint.pprint(result)




# '''' Посмотрим методы и содержимое'''
# print(dir(result))


''''
В полученой инфо:
'pages': 100, - количество страниц 100
'per_page': 20 - 20 оезюме на каждую страницу
'found': 8624

'''

# ''''
# Что бы найти количество, необходимо вывести по ключу (result['found'])
# '''
# pprint.pprint(result['found'])



# ''''Допустим мы хоти найти разработчиков Python в какой то конкретной компании'''
# params = {'text' : 'NAME:(Python OR C++) AND (MAIL OR YANDEX)'}
# result = requests.get(URL, params = params).json()
# pprint.pprint(result['found'])
#
# ''' Посмотрим на вакансии'''
# pprint.pprint(result['items'])



# ''''Допустим мы хоти найти разработчиков Python в какой то конкретной компании'''
# params = {'text' : 'NAME:(python or C++) and (mail or yandex)'}
# result = requests.get(URL, params = params).json()
# pprint.pprint(result['found'])
#
#
#
# ''' Общая инфо '''
# # pprint.pprint(result['items'])
#
# ''' Посмотрим на вакансии'''
# pprint.pprint(result)