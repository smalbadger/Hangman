'''
Class:      HangmanWindow
Author(s):  Clarissa Badger
Date:       Dec 23, 2018
Type:       FINAL
Description:
            The main window for the Hangman application
'''

from PySide2.QtWidgets import QGroupBox

from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QHBoxLayout

from HangmanDrawingBox import HangmanDrawingBox
from HangmanLetterBank import HangmanLetterBank
from HangmanWordBank import HangmanWordBank

class HangmanWindow(QGroupBox):
    def __init__(self):
        super().__init__()
        self.showMaximized()
        self.createElements()
        self.createLayout()
        self.createActions()
        
    def createElements(self):
        self.drawingBox = HangmanDrawingBox()
        self.letterBank = HangmanLetterBank()
        self.wordBank = HangmanWordBank()
    
    def createLayout(self):
        self.mainLayout = QVBoxLayout()
        self.topLayout = QHBoxLayout()
        
        self.topLayout.addWidget(self.drawingBox)
        self.topLayout.addWidget(self.letterBank)
        
        self.mainLayout.addLayout(self.topLayout)
        self.mainLayout.addWidget(self.wordBank)
        
        self.setLayout(self.mainLayout)
    
    def createActions(self):
        self.letterBank.letterClicked.connect(self.wordBank.onLetterClicked)
        
        self.wordBank.wrongGuess.connect(self.letterBank.onWrongGuess)
        self.wordBank.wrongGuess.connect(self.drawingBox.onWrongGuess)
        
        self.wordBank.rightGuess.connect(self.letterBank.onRightGuess)
        self.wordBank.rightGuess.connect(self.drawingBox.onRightGuess)
        
        self.wordBank.reset.connect(self.letterBank.onReset)
        self.wordBank.reset.connect(self.drawingBox.onReset)
        
        self.drawingBox.lose.connect(self.wordBank.onLose)
