import requests
import json

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

name = input('Введите аккаунт (необходимо писать латинскими буквами): ')
repos = '/repos'

main_link='https://api.github.com/users/'+name+repos

response = requests.get(main_link)
data = json.loads(response.text)

for key in data:
    print(f'Cписок репазиториев {key["name"],key["full_name"] }')