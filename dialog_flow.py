import apiai
import json

''''
Глава 12.3
Создаем и интегрируем бота

 Создайте аккаунт Google
Artem  Artem

Artem.ArtemAIU@gmail.com

Пароль: *ArtArt*
AIzaSyCRgZUnmxjkCNubieJViqn0Ebts3and8Mk

https://dialogflow.cloud.google.com/#/newAgent

'''
token = AIzaSyCRgZUnmxjkCNubieJViqn0Ebts3and8Mk

apiai.ApiAI(token).text_request()
request.lang ='ru'

message = input('Введите сообщение:')
request.guery = message
responseJson = json.loads(request.getresponse().read().decode('utf-8'))
print(responseJson)