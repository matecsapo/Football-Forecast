CLIENT_ID = 'i2cta5pwoTbutnWT0m9Z8g'
SECRET_KEY = 'cVMc4BUuT1gy4-Ot5olgTFcVT2m47g'

import requests

auth = requests.auth.HTTPBasicAuth (CLIENT_ID, SECRET_KEY)
data = {
    'grant_type': 'password',
    'username': 'Football_Forecast',
    'password': 'leledoba22'
}
headers = {'User-Agent': 'MyAPI/0.0.1'}
res = requests.post ('https://www.reddit.com/api/v1/access_token',
                     auth=auth, data=data, headers=headers)
TOKEN = res.json()['access_token']
headers['Authorization'] = f'bearer {TOKEN}'

res = requests.get('https://oauth.reddit.com/r/python/hot', headers=headers)
res.json()
for post in res.json()['data']['children']:
    print(post['data']['title'])