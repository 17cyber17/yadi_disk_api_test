import requests
from requests_oauthlib import OAuth1
headers = {'Authorization': 'AgAAAAARY09qAADLWzX1TShKB0zKjjC7hLBzxt4'}
res = requests.put('https://cloud-api.yandex.net/v1/disk/resources?path=QA', headers=headers)
print(res)