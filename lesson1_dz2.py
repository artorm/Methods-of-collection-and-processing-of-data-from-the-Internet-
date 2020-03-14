from pprint import pprint
import requests
import json

main_link='https://sandbox-api.brewerydb.com/v2/'

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

pprint(main_link)
browse ='browse/style/details/id/110'
Key = '2f1ceac59565e023266cb96e5ec181db'
requests.get(f'{main_link}')

params = {
   'browse': browse,
   'Key': Key
 }
response = requests.get(main_link, params=params)

pprint(response)
data = json.loads(response.text)
print(data)

### Пример не очень удачен так как сайт бесплатно отдает только API для теста.


### Вариант 2
### Нашел сайт для подбора брошеных животных. petfinder.com
### Прочитал про api и авторизацию, сайт использует  OAuth. Получил CLIENT_ID, CLIENT_SECRET.
### Долго бился что бы получить токин через postman, так и не получилось, реализовал этот запрос через командную строку
### получил токин. Однако дальше стопор, как мне перевести эти запросы в python код я пока так и не понял.
### Наброски ниже, через командную строку я легко получаю доступ но через питон только 403 ошибку.
main_link2 ='https://api.petfinder.com/v2/oauth2/token'
pprint(main_link2)
#params2 = {
 #   'CLIENT_ID': '45RNmfFj2pAwqlOUUbwzmGNDNGU2c2tXDXdCixZy1hoG3kutlb',
 #   'CLIENT_SECRET': 'Y2mkEeq0zIxXpPGGSxcko5NKIRgZjwoTqhdu28jd' }
Authorization = {'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI0NVJObWZGajJwQXdxbE9VVWJ3em1HTkROR1UyYzJ0WERYZENpeFp5MWhvRzNrdXRsYiIsImp0aSI6IjJlZGM5MTU4NDA4ZGY3Y2JiYWM3M2RlYzNiMWZmNWZkMDdmNzY5YTUxYjljYWFhNjQ5N2Q0NTcyNDg2OThjYjNlZWJlOTUzY2JhOWExODZhIiwiaWF0IjoxNTg0MjA5MjA0LCJuYmYiOjE1ODQyMDkyMDQsImV4cCI6MTU4NDIxMjgwNCwic3ViIjoiIiwic2NvcGVzIjpbXX0.pHVmNTB0VQH1xnMVhlqMfSuqGvxQKz4DXBuB-gdMOpiwg4cDjaVqBkXRbLzdGkueEUskkyL1KO_irdxvp9mlrWzbJCYpJuCqQ4Jljh24szDifliFoi9KvtoLOeT_z6f7fmasiodAzZuN77-adnE9yAD3vrDXyejr1AjWLmbK2PwaB4G30z0JgxLoAZgCzqxUMscmv74Qa5ysQfU-oYpI1Z8UiAcd47qZEMCwasUinUiqsgNGe5O0EAEMCbSWJThSsI2bhobIXw3eVjoiu2Cl98FyMamvrXNS4qOMXe6DVhbA6AUdvwh7f9D9uaCS3Zw2IQfKESYOh3BUc223WG6F0g'}
response = requests.get(f'{Authorization}, {main_link2}')
#response=requests.get(f'{main_link2}', params=params2)
pprint(response)

