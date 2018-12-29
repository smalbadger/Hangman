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

import random

class HangmanWordBank(QGroupBox):
    wrongGuess = Signal()
    rightGuess = Signal()
    reset = Signal()
    win = Signal()
    setDefinition = Signal(str)
    
    def __init__(self):
        super().__init__()
        self.hideChars = True
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
        self.messageField = QLabel("Message Field")
        self.messageField.setStyleSheet("""text-align: center; 
                                           font-size:  200px;
                                        """)
        self.messageField.hide()
        
    
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
            
        self.lowerLayout = QHBoxLayout()
        self.lowerLayout.addStretch()
        self.lowerLayout.addWidget(self.messageField)
        self.lowerLayout.addStretch()
            
        self.mainLayout.addLayout(self.controlLayout)
        self.mainLayout.addLayout(self.letterLayout)
        self.mainLayout.addLayout(self.lowerLayout)
        
        self.setLayout(self.mainLayout)
    
    def createActions(self):
        self.changeBtn.clicked.connect(self.onChangeWord)
        self.reset.connect(self.onReset)
        self.rightGuess.connect(self.onRightGuess)
        self.randomBtn.clicked.connect(self.onRandom)
    
    def onChangeWord(self):
        self.messageField.hide()
        word = self.wordField.text()
        self.wordField.setText("")
        self.setWord(word)
        self.reset.emit()
    
    def setWord(self, newWord):
        self.word = newWord.upper()
        print(self.word)
       
    #slot 
    def onReset(self):
        for widget in self.spaces: 
            widget.setParent(None)
        
        self.spaces = []
        for c in self.word:
            text = "_"
            if c == " ":
                text=" "
            if self.hideChars == False:
                text = c
            w = QLabel(text)
            w.setStyleSheet("""text-align: center; 
                               font-size:  200px;
                            """)
            
            w.setAlignment(Qt.AlignCenter)
            self.spaces.append(w)
        
        for widget in self.spaces:
            self.letterLayout.addWidget(widget)
            
        self.hideChars = True
       
    #slot
    def onLetterClicked(self, letter):
        if letter in self.word:
            #show letters in word
            #emit signal with True value
            for i in range(len(self.word)):
                if letter == self.word[i]:
                    self.spaces[i].setText(letter)
            self.rightGuess.emit()
            
        else:
            #emit signal with False value to change color of letter button
            #AND draw stick figure
            self.wrongGuess.emit()
            
    #slot
    def onRightGuess(self):
        won = self.checkForWin()
        if won == True:
            self.win.emit()
            #self.setWord("you win!")
            self.messageField.setText("You Win!")
            self.messageField.show()
            self.hideChars = False
            self.onReset()
        
    def checkForWin(self):
        for letterWidget in self.spaces:
            text = letterWidget.text()
            if text == "_":
                return False
        return True
                
    #slot   
    def onLose(self):
        #self.setWord("you lose!")
        self.messageField.setText("You Lose!")
        self.messageField.show()
        self.hideChars = False
        self.onReset()
        
    #slot
    def onRandom(self):
        #select random word from dictionary
        self.messageField.hide() 
        word = '-'
        while not self.wordIsValid(word):
            print(word)
            f = open('dictionary.csv')
            word = self.randomLine(f).strip()
            f.close()
        
        w = word.split(",")[0]
        d = word.split(",")[1].strip()
        
        #word should be valid now
        self.setWord(w)
        self.setDefinition.emit(d)
        
        self.reset.emit()

    def randomLine(self, afile):
        line = next(afile)
        for num, aline in enumerate(afile, 2):
          if random.randrange(num): continue
          line = aline
        return line
        
        
    def wordIsValid(self, word):
        a = ord('a')
        z = ord('z')
        A = ord('A')
        Z = ord('Z')
        space = ord(' ')
        comma = ord(',')
        
        if word.count(',') != 1:
            return False
        
        for character in word:
            ascii = ord(character)
            if ascii >= a and ascii <= z:
                continue
            elif ascii >= A and ascii <= Z:
                continue
            elif ascii == space:
                continue
            elif ascii == comma:
                continue
            else:
                return False
        return True
                
