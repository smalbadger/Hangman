'''
Class:      HangmanDrawingBox
Author(s):  Clarissa Badger
Date:       Dec 23, 2018
Type:       FINAL
Description:
            view to draw the hangman
'''

from PySide2.QtWidgets import QGroupBox

class HangmanDrawingBox(QGroupBox):
    def __init__(self):
        super().__init__()
        self.createStyle()
        self.createElements()
        self.createLayout()
        self.createActions()
        
    def createStyle(self):
        self.setStyleSheet("background-color:blue;")
        
    def createElements(self):
        pass
    
    def createLayout(self):
        pass
    
    def createActions(self):
        pass
       
    def onLetterClickedResponse(self, response):
        pass
        
    def onReset(self):
        pass
        
