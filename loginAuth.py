import requests
from constants import *

class LoginAuth:
    def __init__(self):
        session = requests.session()

        url = 'https://users.premierleague.com/accounts/login/'

        payload = {
        'password': '',
        'login': 'battams10@googlemail.com',
        'redirect_uri': 'https://fantasy.premierleague.com/a/login/',
        'app': 'plfpl-web'
        }
        session.post(url, data=payload)
        print(session.cookies.items())