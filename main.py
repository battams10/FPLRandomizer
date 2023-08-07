from uiComponent import *

class Main:
    index = Index()
    inputTeam = InputTeam()
    ManageChips = ManageChips()

    def __init__(self):
        self.UI = self.index
        self.UI.output("Welcome to FPL randomizer\n")
        self.UI.output(self.UI.getInitText())

    def changeUIComp(self, uiComp):
        self.UI = uiComp
        self.UI.output("\n")
        self.UI.output(self.UI.getInitText())
        
    def main(self):
        while True:
            output = self.UI.processInput(self.UI.takeInput())
            if output == 'change to index':
                self.changeUIComp(self.index)
            elif output == 'change to inputTeam':
                self.changeUIComp(self.inputTeam)
            elif output == 'change to manageChips':
                self.changeUIComp(self.ManageChips)

prog = Main()

if __name__ == "__main__":
    prog.main()