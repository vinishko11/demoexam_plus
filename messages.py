from PySide6.QtWidgets import *


def info_message(text):
    message = QMessageBox()
    message.setText(text)
    message.setIcon(QMessageBox.Icon.Information)
    message.setStandardButtons(QMessageBox.StandardButton.Yes)
    message.setWindowTitle('Мозаика')
    message.exec()

def war_message(text):
    message = QMessageBox()
    message.setText(text)
    message.setIcon(QMessageBox.Icon.Warning)
    message.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    message.setWindowTitle('Мозаика')
    res = message.exec()
    return res < 20000

def crit_message(text):
    message = QMessageBox()
    message.setText(text)
    message.setIcon(QMessageBox.Icon.Critical)
    message.setStandardButtons(QMessageBox.StandardButton.Yes)
    message.setWindowTitle('Мозаика')
    message.exec()