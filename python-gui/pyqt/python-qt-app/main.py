from PyQt4 import QtGui
import sys

import mainwindow_design  # all design related things

import os  # for listing directory methods


class ExampleApp(QtGui.QMainWindow, mainwindow_design.Ui_MainWindow):
    def __init__(self):
        # simple reason why we use 'super' here is that it allows us to
        # access variables, methods etc in the mainwindow_design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # this is defined in mainwindow_design.py file automatically
        # it sets up layout and widgets that are defined
        self.btnBrowse.clicked.connect(self.browse_folder)  # connect function on button click

    def browse_folder(self):
        self.listWidget.clear()
        directory = QtGui.QFileDialog.getExistingDirectory(self,
                                                           "Pick a folder")
        # execute getExistingDirectory dialog and set the directory variable to be equal
        # to the user selected directory

        if directory: # if user didn't pick a directory don't continue
            for file_name in os.listdir(directory): # for all files, if any, in the directory
                self.listWidget.addItem(file_name)  # add file to the listWidget


def main():
    app = QtGui.QApplication(sys.argv)  # a new instance of QApplication
    form = ExampleApp()  # we set the form to be our ExampleApp (mainwindow_design)
    form.show()  # show the form
    app.exec_()  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function
