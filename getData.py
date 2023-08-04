import csv

class getData: #test of reading player data
    def __init__(self, fileName1, fileName2):
        self.fileName1 = fileName1
        self.fileName2 = fileName2

        self.reader1 = csv.reader(open(fileName1, encoding='utf-8'), delimiter=',', quotechar='|') #open file
        self.reader1.__next__()

        self.reader2 = csv.reader(open(fileName2, encoding='utf-8'), delimiter=',', quotechar='|') #open file
        self.reader2.__next__()

        self.writer = csv.writer(open('playerData.csv', mode='w', newline='\n', encoding='utf-8'), delimiter=',') #create new file
        self.writer.writerow(['id', 'first_name', 'surname', 'cost', 'team', 'position'])

    def getLine1(self):
        try:
            line = self.reader1.__next__() #read next line
            newline = [line[0], line[1], line[17], line[18]] #first, sur, cost, pos
            print(newline)
            return newline
        except:
            return None
        
        
    def getLine2(self):  
        try:  
            line = self.reader2.__next__()
            newline = [line[42], line[50], line[74], line[86]] #id, cost, team, webname
            print(newline)
            return newline
        except:
            return None
        
    def writeLine(self, line): #write passed data to new file
        self.writer.writerow([line[0], line[1], line[2], line[3], line[4], line[5]])

    def mergeLines(self, line1, line2):
        mergedline = [line2[0], line1[0], line1[1], line2[1], line2[2], line1[3]]
        return mergedline

    def main(self):
        while(True):
            line1 = self.getLine1()
            if (line1 == None):
                break
            line2 = self.getLine2()
            if (line2 == None):
                break

            line = self.mergeLines(line1, line2)
            self.writeLine(line)
            print(line)

GD = getData("Fantasy-Premier-League/data/2023-24/cleaned_players.csv", 
             "Fantasy-Premier-League/data/2023-24/players_raw.csv")

if __name__ == "__main__":
    GD.main()