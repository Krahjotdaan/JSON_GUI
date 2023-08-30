import os, sys, json
from PyQt5 import QtWidgets
from MainWindow import *
from AboutProgram import *


class Application(QtWidgets.QMainWindow):
    def __init__(self):
        super(Application, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def new_file_click(self):
        pass

    def open_file_click(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName(self, 'Открытие файла', '/home', '*.json')[0]
        with open(file_name, 'r') as fl:
            data = json.load(fl)
            data_array = []
            for x in data:
                data_array.append([list(x.keys()), list(x.values())])
        
            top = QtWidgets.QTreeWidgetItem(self.ui.tree)
            self.ui.tree.addTopLevelItem(top)
            top.setText(0, fl.name)
            for k in range(len(data_array[0][0])):
                item = QtWidgets.QTreeWidgetItem(top)
                item.setText(0, data_array[0][0][k])
                if isinstance(data_array[0][1][k], int) or isinstance(data_array[0][1][k], float):
                    item.setText(1, "Number")
                elif isinstance(data_array[0][1][k], str):
                    item.setText(1, "String")
                elif isinstance(data_array[0][1][k], dict):
                    item.setText(1, "Object")
                elif isinstance(data_array[0][1][k], list):
                    item.setText(1, "Array")
                elif isinstance(data_array[0][1][k], bool):
                    item.setText(1, "Boolean")
                elif isinstance(data_array[0][1][k], None):
                    item.setText(1, "Null")

    def save_file_click(self):
        pass

    def close_file_click(self):
        pass

    def undo_click(self):
        pass

    def redo_click(self):
        pass

    def exit_click(self):
        sys.exit()

    def about_program_click(self):
        self.about_program = AboutProgram()
        self.about_program.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        self.about_program.show()

    def add_entry_button_click(self):
        pass

    def add_col_button_click(self):
        pass

    def delete_entry_button_click(self):
        pass

    def delete_col_button_click(self):
        pass

    def apply_button_click(self):
        pass

    def goto_button_click(self):
        pass
    

class AboutProgram(QtWidgets.QMainWindow):
    def __init__(self):
        super(AboutProgram, self).__init__()
        self.ui = Ui_AboutProgram()
        self.ui.setupUi(self)
