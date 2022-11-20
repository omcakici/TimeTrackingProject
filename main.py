from time import time
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFormLayout
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QFont
from PyQt5.uic import loadUi
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QLineEdit, QLabel
from PyQt5.QtCore import Qt

from PyQt5.uic import loadUi
import tkinter as tk
from tkinter import simpledialog

import io, json, re

class LoginSingupUI(QDialog):
    def __init__(self):
        super(LoginSingupUI, self).__init__()
        
        loadUi("./UI/login.ui",self)
        
        self.loginButton.clicked.connect(self.go_main_menu_via_login)
        self.signUpButton.clicked.connect(self.go_main_menu_via_signup)
        self.errorTextSignUp.setVisible(False)
        self.errorTextLogin.setVisible(False)

    # Define a function for
    # for validating an Email
    def is_valid_email(self, email):
        # Make a regular expression
        # for validating an Email
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        # pass the regular expression
        # and the string into the fullmatch() method
        if(re.fullmatch(regex, email)):
            return False
        else:
            return True
    
    def check_value(self, data, val):
        return any(user['Email']==val for user in data['UsersInfo'])

    def go_main_menu_via_login(self):
        with open('userInformation.json', 'r') as f_in:
            data_read = json.load(f_in) 

        if(self.check_value(data_read, self.emailInputLogin.text())==False or self.is_valid_email(self.emailInputLogin.text())):
            UI = LoginSingupUI() # This line determines which screen you will load
            UI.errorTextLogin.setVisible(True)
            widget.addWidget(UI)
            widget.setCurrentIndex(widget.currentIndex()+1)
        else:
            main_menu = MainMenuUI()
            widget.addWidget(main_menu)
            widget.setCurrentIndex(widget.currentIndex()+1)
    
    def go_main_menu_via_signup(self):
        # function to add to JSON
        def write_json(new_data, filename='userInformation.json'):
            with open(filename,'r+') as file:
                # First we load existing data into a dict.
                file_data = json.load(file)
                # Join new_data with file_data inside emp_details
                file_data["UsersInfo"].append(new_data)
                # Sets file's current position at offset.
                file.seek(0)
                # convert back to json.
                json.dump(file_data, file, indent = 4)
        
            # python object to be appended
          
        data_write = {
            'Name': self.nameInputSignUp.text(),
            'Email': self.emailInputSignUp.text()
        }

        with open('userInformation.json', 'r') as f_in:
            data_read = json.load(f_in)
        
        if(self.check_value(data_read, self.emailInputSignUp.text()) or self.is_valid_email(self.emailInputSignUp.text())):
            UI = LoginSingupUI() # This line determines which screen you will load
            UI.errorTextSignUp.setVisible(True)
            widget.addWidget(UI)
            widget.setCurrentIndex(widget.currentIndex()+1)
        else:
            write_json(data_write)
            # # Write JSON file

            main_menu = MainMenuUI()
            widget.addWidget(main_menu)
            widget.setCurrentIndex(widget.currentIndex()+1)

class MainMenuUI(QDialog):
    def __init__(self):
        super(MainMenuUI,self).__init__()
        loadUi("./UI/mainMenu.ui",self)

        self.startPomodoroButton.clicked.connect(self.go_pomodoro_ui)
    
    def go_pomodoro_ui(self):
        pomodoro_ui = PomodoroUI()
        widget.addWidget(pomodoro_ui)
        widget.setCurrentIndex(widget.currentIndex()+1)

class PomodoroUI(QDialog):
    def __init__(self):
        super(PomodoroUI,self).__init__()
        loadUi("./UI/pomodoro.ui",self)

        self.goToMainMenuButton.clicked.connect(self.go_main_menu)
    
    def go_main_menu(self):
        main_menu = MainMenuUI()
        widget.addWidget(main_menu)
        widget.setCurrentIndex(widget.currentIndex()+1)

class ShortBreakUI(QDialog):
    def __init__(self):
        super(ShortBreakUI,self).__init__()
        loadUi("./UI/shortBreak.ui",self)

class LongBreakUI(QDialog):
    def __init__(self):
        super(LongBreakUI,self).__init__()
        loadUi("./UI/longBreak.ui",self)


app = QApplication(sys.argv)
UI = LoginSingupUI() # This line determines which screen you will load at first

# You can also try one of other screens to see them.
    # UI = MainMenuUI()
    # UI = PomodoroUI()
    # UI = ShortBreakUI()
    # UI = LongBreakUI()

widget = QtWidgets.QStackedWidget()
widget.addWidget(UI)
widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.setWindowTitle("Time Tracking App")
widget.show()
sys.exit(app.exec_())
