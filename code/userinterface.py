from code.messages import *

class UserInterface(object):
    
    _instance = None
    _sectionCounter = 1;
    
    LINE_LENGTH = 79
    FILL_CHARACTER = '-'
    HORIZONTAL_LINE = FILL_CHARACTER * LINE_LENGTH + '\n'
     
    
    def __init__(self):
        if UserInterface._instance != None:
            raise Exception("This class is a singleton!")
        else:
            UserInterface._instance = self
       
    @staticmethod
    def getInstance():
        if UserInterface._instance == None:
            UserInterface._instance = UserInterface();
        return UserInterface._instance
     
    def PrintTitle(self, title):
        self.PrintSeparator()
        print(title.center(self.LINE_LENGTH ,' ').upper()) 
        print('')
        
    def PrintSeparator(self):
        print('*' * self.LINE_LENGTH)
  
    def PrintSection(self, section):      
        sectionCountStr = '(' + str(self._sectionCounter) + ')'
        
        if len(section) <= self.LINE_LENGTH - 2:
            formatedTitle = section.upper().center(self.LINE_LENGTH \
                                                 - len(sectionCountStr),
                                                 self.FILL_CHARACTER)
            print('\n\n' + sectionCountStr + formatedTitle + '\n')
        else:
            print(self.HORIZONTAL_LINE +
                  sectionCountStr + ' ' +
                  section.upper() + '\n' +
                  self.HORIZONTAL_LINE)
        
        self._sectionCounter += 1
       
    def AskYesOrNo(self, question):
        userInput=""
        print('')
        while (userInput!=YES and userInput!=NO):
            userInput = input(question + ' ' + YES + '/' + NO + ': >> ').lower()
        return userInput
    
    #def AskInput(self, question):
    #    return input(question)

