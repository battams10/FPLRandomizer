import time
import requests, json
from pprint import pprint
from constants import *
from loginAuth import *

class APIQuery:
    def __init__(self):
        self.base_url = 'https://fantasy.premierleague.com/api/' 
        r = requests.get(self.base_url+'bootstrap-static/').json() 
        #pprint(r, indent=2, depth=1, compact=True)

    def getTeam(self):
        auth = LoginAuth()

        url = self.base_url + "my-team/" + MANAGER_ID + "/"
        response = ''
        while response == '':
            try:
                response = requests.get(url)
            except:
                time.sleep(5)
        if response.status_code != 200:
            raise Exception("Response was code " + str(response.status_code))
        data = json.loads(response.text)
        print(data)

    def getPlayers(self):
        player_id = 1
        #url = self.base_url + "element-summary/" + str(player_id) + "/"
        url = self.base_url + 'bootstrap-static/'

        #response = requests.get(url)
        #while response.status_code == 200:
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception("Response was code " + str(response.status_code))
        data = json.loads(response.text)
        #print(data)
        player_id += 1
        url = self.base_url + 'bootstrap-static/'
        
        print(data['elements'][0]['first_name'])
        print(data['elements'][0]['second_name'])
        print(data['elements'][0]['now_cost'])
        print(data['elements'][0]['team'])
        print(data['elements'][0]['element_type'])
        

q = APIQuery()
q.getTeam()
#q.getPlayers()
