# https://build-system.fman.io/pyqt5-tutorial

import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox

class UiApplication():
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.__init_widget()

    def __init_widget(self):
        self.widget = QWidget()
        self.widget.resize(300, 300)
        self.widget.setWindowTitle('JP App')

    def dialog(self):
        self.mbox = QMessageBox()
        self.mbox.setText(f'Random Wiki Page: ')
        self.mbox.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.mbox.exec()

if __name__ == '__main__':
    app = UiApplication()

    label = QLabel(app.widget)
    label.setText('Label tekstje')
    label.move(100, 130)
    label.show()

    btn = QPushButton(app.widget)
    btn.setText('open msgbox')
    btn.move(110, 150)
    btn.show()
    btn.clicked.connect(app.dialog)

    app.widget.show()
    sys.exit(app.app.exec())