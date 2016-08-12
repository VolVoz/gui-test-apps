import sys
from PyQt4.QtGui import QApplication, QWidget, QPushButton, QMessageBox


def window():
    app = QApplication(sys.argv)  # init app
    widget = QWidget()  # init widget for out app
    widget.setWindowTitle("PyQt Dialog")

    button = QPushButton(widget)  # put new button on our widget
    button.setText("Say Hello")  # text on button
    button.clicked.connect(showdialog)  # connect function on button click

    widget.show()  # run widget
    app.exec_()


def showdialog():
    msg = QMessageBox()  # init message box
    msg.setIcon(QMessageBox.Information)  # select message description
    msg.setText("Hello World")
    msg.setInformativeText("This is additional information")
    msg.exec_()

if __name__ == '__main__':
    window()
