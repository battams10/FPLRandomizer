from enum import Enum

class index(Enum):
     InputTeam = 1
     GetTransfer = 2
     ManageChips = 3
     GetStarting11 = 4
     GetCaptain = 5
     Exit = 6

#interface
class UIComponent:
    def getInitText(self):
        pass

    def output(self, line):
        print(line)

    def takeInput(self):
        userIn = input("")
        return userIn

    def processInput(self):
        pass

class Index(UIComponent):
    def getInitText(self):
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

    def getInitText(self):
        return "Input Team \nEnter player " + str(self.playerNumber) + " or press 6 to return to main menu"

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
    def getInitText(self):
        pass

    def output(self, line):
        super().output(line)

    def takeInput(self):
        return super().takeInput()

    def processInput(self, line):
        pass