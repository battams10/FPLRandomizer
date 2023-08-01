import csv

class getData: #test of reading player data
    def __init__(self, fileName1, fileName2):
        self.fileName1 = fileName1
        self.fileName2 = fileName2

    def setUpDatabase(self):
        pass



GD = getData("Fantasy-Premier-League/data/2023-24/cleaned_players.csv", 
             "Fantasy-Premier-League/data/2023-24/players_raw.csv")
GD.getData()