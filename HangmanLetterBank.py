'''
Class:      HangmanLetterBank
Author(s):  Clarissa Badger
Date:       Dec 23, 2018
Type:       FINAL
Description:
            showing all possible letters to be guessed
'''

from PySide2.QtWidgets import *
from PySide2.QtCore import *

class HangmanLetterBank(QGroupBox):
    letterClicked = Signal(str)
    
    correctStyle =  """
                        background-color: green;
                    """
                    
    incorrectStyle ="""
                        background-color: red;
                    """
    
    def __init__(self):
        super().__init__()
        self.createStyle()
        self.createElements()
        self.createLayout()
        self.createActions()
        
    def createStyle(self):
        self.setStyleSheet("background-color: orange;")
        
    def createElements(self):
        a = ord('A')
        z = ord('Z')
        self.clicked = []
        self.letterBtnGrp = QButtonGroup()
        self.letterBtnGrp.setExclusive(True)
        
        self.letterBtns = []
        for letter in range(a,z+1):
            btn = QPushButton(chr(letter))
            self.letterBtns.append(btn)
            self.letterBtnGrp.addButton(btn)
        print("buttons made")
            
    
    def createLayout(self):
        self.mainLayout = QGridLayout()
        row = 0
        column = 0
        for i in range(len(self.letterBtns)):
            self.mainLayout.addWidget(self.letterBtns[i], row, column)
            column += 1
            if column >= 6:
                column = 0
                row += 1
                if row == 4:
                    column += 2
        self.setLayout(self.mainLayout)
        print("layout made")
    
    def createActions(self):
        self.letterBtnGrp.buttonClicked.connect(self.onLetterClick)
        
    def onLetterClick(self, btn):
        self.buttonClicked = btn
        letter = btn.text()
        if letter not in self.clicked:
            self.clicked.append(letter)
            self.letterClicked.emit(letter)
            
    def onWrongGuess(self):
        self.buttonClicked.setStyleSheet(HangmanLetterBank.incorrectStyle)
            
    def onRightGuess(self):
        self.buttonClicked.setStyleSheet(HangmanLetterBank.correctStyle)
        
    def onReset(self):
        self.buttonClicked = None
        self.clicked = []
        for btn in self.letterBtns:
            btn.setStyleSheet("")
        
