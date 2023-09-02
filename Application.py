import os, sys, json
from PyQt5 import QtWidgets
from MainWindow import *
from AboutProgram import *


class Application(QtWidgets.QMainWindow):
    def __init__(self):
        super(Application, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = []

    def new_file_click(self):
        pass

    def open_file_click(self):
        self.ui.data_type.isEnabled = False
        file_name = QtWidgets.QFileDialog.getOpenFileName(self, 'Открытие файла', '/home', '*.json')[0]
        with open(file_name, 'r') as fl:
            data = json.load(fl)
            keys = list(data[0].keys())
            self.db.append(keys)
            data_array = []
            for x in data:
                data_array.append(list(x.values()))
                self.db.append(list(x.values()))

            top = QtWidgets.QTreeWidgetItem(self.ui.tree)
            self.ui.tree.addTopLevelItem(top)
            top.setText(0, fl.name)
            for i in range(len(keys)):
                item = QtWidgets.QTreeWidgetItem(top)
                item.setText(0, keys[i])
                if isinstance(data_array[0][i], int) or isinstance(data_array[0][i], float):
                    item.setText(1, "number")
                elif isinstance(data_array[0][i], str):
                    item.setText(1, "string")
                elif isinstance(data_array[0][i], dict):
                    item.setText(1, "object")
                elif isinstance(data_array[0][i], list):
                    item.setText(1, "array")
                elif isinstance(data_array[0][i], bool):
                    item.setText(1, "boolean")
                elif isinstance(data_array[0][i], None):
                    item.setText(1, "null")
            
            self.ui.table.setColumnCount(len(keys))
            self.ui.table.setRowCount(len(data_array))
            self.ui.table.setHorizontalHeaderLabels(keys)
            row = 0
            for item in data_array:
                for i in range(len(data_array)):
                    for j in range(len(keys)):
                        self.ui.table.setItem(row, j, QtWidgets.QTableWidgetItem(str(data_array[i][j])))
                    row += 1

            self.ui.table.cellClicked.connect(self.current_cell)

    def current_cell(self):
        self.ui.cell_editing.setText(self.ui.table.currentItem().text())

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
        self.ui.table.currentItem().setText(self.ui.cell_editing.toPlainText())

    def goto_button_click(self):
        pass
    

class AboutProgram(QtWidgets.QMainWindow):
    def __init__(self):
        super(AboutProgram, self).__init__()
        self.ui = Ui_AboutProgram()
        self.ui.setupUi(self)
