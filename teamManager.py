import csv, os

#class to store and manange existing team
class TeamManager:
    def __init__(self):
        if os.path.exists('currentTeam.csv'):
            self.reader = csv.reader(open('currentTeam.csv', encoding='utf-8'), delimiter=',', quotechar='|') #open file
            self.reader.__next__()
            print("\nExisting team:")
            while(self.getLine()):
                self.numPlayers += 1
        else:
            self.numPlayers = 0
            self.writer = csv.writer(open('currentTeam.csv', mode='w', newline='\n', encoding='utf-8'), delimiter=',') #create new file
            self.writer.writerow(['id', 'first_name', 'surname', 'cost', 'team', 'position'])

    def getNumPlayers(self):
        return self.numPlayers
    
    def getLine(self):
        try:
            line = self.reader.__next__() #read next line
            print(line)
            return line
        except:
            return False
        
    def openPlayerFile(self):
        self.writer = csv.writer(open('currentTeam.csv', mode='w', newline='\n', encoding='utf-8'), delimiter=',') #create new file

    def findPlayer(self):
        pass

    def writeLine(self, line): #write passed data to new file
        self.writer.writerow(line)
    
    