from teamManager import *

#interface
class UIComponent:
    def onChange(self):
        pass

    def output(self, line):
        print(line)

    def takeInput(self):
        userIn = input("")
        return userIn

    def processInput(self):
        pass

class Index(UIComponent):
    def onChange(self):
        return "Select option: 1) Input Team, 2) Get Transfer, 3) Manage Chips, 4) Select Team, 5) Get Captain, 6) Exit\n"

    def output(self, line):
        super().output(line)

    def takeInput(self):
        return super().takeInput() 

    def processInput(self, line):
        if line == '1': #input team
            return 'change to inputTeam'
        elif line == '2': #get transfer
            pass
        elif line == '3': #manage chips
            return 'change to inputTeam'
        elif line == '4': #get starting 11
            pass
        elif line == '5': #get captain
            pass
        elif line == '6': #exit
            print("Exiting program")
            exit()
        else:
            print("Invalid input") 

class InputTeam(UIComponent):
    playerNumber = 0
    teamManager = TeamManager()

    def onChange(self):
        self.checkExistingTeam()
        return "Input Team \nEnter player " + str(self.playerNumber) + " or press 6 to return to main menu"

    def checkExistingTeam(self):
        self.playerNumber = self.teamManager.getNumPlayers()

    def output(self, line):
        super().output(line)

    def takeInput(self):
        return super().takeInput()

    def processInput(self, line):
        if line == '6':
            return 'change to index'
        else:
            pass #store player

class ManageChips(UIComponent):
    def onChange(self):
        pass

    def output(self, line):
        super().output(line)

    def takeInput(self):
        return super().takeInput()

    def processInput(self, line):
        pass