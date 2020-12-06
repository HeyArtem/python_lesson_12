import requests
import pprint

''''
Глава 12.1 rest запросы
'''
url = 'https://www.cbr-xml-daily.ru/daily_json.js'

response = requests.get(url)
print(type(response), dir(response))

print(response.status_code)
''''
status_code - некоторое возвращаемое число, еоторое говорит, как завершился вопрос к серверу

200 - запрос прошел успешно, нет никаких проблем
404 - страница не найденеа 
вообще, все ошибки с цифры:
4 - ошибка со стороны клиента
5 - со стороны сервера

Расшифровка всех ошибок:
https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%BA%D0%BE%D0%B4%D0%BE%D0%B2_%D1%81%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D1%8F_HTTP

'''


print(response.text)
''''
Это содержимое странички
'''


params = {
    "ID": "AUD"
}
'''' Запрос с параметром, обычно в словаре '''

response = requests.get(url, params = params)
'''' Нужно передать еще один атрибут, метод get'''

print(response.status_code, response.text)

''''
У нас ни чего не прошло, т.к. надо изучать документацию каждого api(
'''