'''
Class:      HangmanWordBank
Author(s):  Clarissa Badger
Date:       Dec 23, 2018
Type:       FINAL
Description:
            showing the word to be guessed
'''

'''
from PySide2.QtWidgets import QGroupBox
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QHBoxLayout
'''
from PySide2.QtWidgets import *

from PySide2.QtCore import *

class HangmanWordBank(QGroupBox):
    letterContainedResponse = Signal(bool)
    reset = Signal()
    
    def __init__(self):
        super().__init__()
        self.createStyle()
        self.setWord("Clarissa Badger")
        self.createElements()
        self.createLayout()
        self.createActions()
        
    def createStyle(self):
        styleStr = """
                    background-color: green;
                   """
        self.setStyleSheet(styleStr)
        
    def createElements(self):
        self.randomBtn = QPushButton("RANDOM")
        self.wordField = QLineEdit()
        self.changeBtn = QPushButton("CHANGE")
    
        self.spaces = []
        for c in self.word:
            text = "_"
            if c == " ":
                text=" "
            w = QLabel(text)
            w.setStyleSheet("""text-align: center; 
                               font-size:  200px;
                            """)
            
            w.setAlignment(Qt.AlignCenter)
            self.spaces.append(w)
            
    
    def createLayout(self):
        self.mainLayout = QVBoxLayout()
        self.controlLayout = QHBoxLayout()
        self.letterLayout = QHBoxLayout()
        
        self.controlLayout.addWidget(self.randomBtn)
        self.controlLayout.addStretch(1)
        self.controlLayout.addWidget(self.wordField)
        self.controlLayout.addWidget(self.changeBtn)
        
        for widget in self.spaces:
            self.letterLayout.addWidget(widget)
            
        self.mainLayout.addLayout(self.controlLayout)
        self.mainLayout.addLayout(self.letterLayout)
        
        self.setLayout(self.mainLayout)
    
    def createActions(self):
        self.changeBtn.clicked.connect(self.onChangeWord)
        self.reset.connect(self.onReset)
    
    def onChangeWord(self):
        word = self.wordField.text()
        self.wordField.setText("")
        self.setWord(word)
        self.reset.emit()
    
    def setWord(self, newWord):
        self.word = newWord.upper()
        
    def onReset(self):
        for widget in self.spaces: 
            widget.setParent(None)
        
        self.spaces = []
        for c in self.word:
            text = "_"
            if c == " ":
                text=" "
            w = QLabel(text)
            w.setStyleSheet("""text-align: center; 
                               font-size:  200px;
                            """)
            
            w.setAlignment(Qt.AlignCenter)
            self.spaces.append(w)
        
        for widget in self.spaces:
            self.letterLayout.addWidget(widget)
        
    def onLetterClicked(self, letter):
        if letter in self.word:
            #show letters in word
            #emit signal with True value
            for i in range(len(self.word)):
                if letter == self.word[i]:
                    self.spaces[i].setText(letter)
            self.letterContainedResponse.emit(True)
            
        else:
            #emit signal with False value to change color of letter button
            #AND draw stick figure
            self.letterContainedResponse.emit(False)
            
