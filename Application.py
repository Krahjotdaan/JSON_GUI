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
        file_name = QtWidgets.QFileDialog.getOpenFileName(self, 'Открытие файла', '/home', '*.json')[0]
        try:
            with open(file_name, 'r') as fl:
                data = json.load(fl)
                self.setWindowTitle("JSON GUI - " + file_name)
                self.ui.data_type.setEnabled(False)
                self.ui.tree.clear()
                self.ui.table.setRowCount(0)
                self.ui.table.setColumnCount(0)
        except FileNotFoundError:
            pass
        except FileExistsError:
            QtWidgets.QMessageBox(self, "Такого файла не существует", QtWidgets.QMessageBox.StandardButton.Ok)

        try:
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
            rows = 0
            for item in data_array:
                for i in range(len(data_array)):
                    for j in range(len(keys)):
                        self.ui.table.setItem(rows, j, QtWidgets.QTableWidgetItem(str(data_array[i][j])))
                    rows += 1
        except IndexError:
            pass
        except UnboundLocalError:
            pass

        self.ui.table.cellClicked.connect(self.current_cell)
        self.ui.table.selectionModel().clearCurrentIndex()

    def current_cell(self):
        try:
            self.ui.cell_editing.setText(self.ui.table.currentItem().text())
            self.ui.key_editing.setText(self.db[0][self.ui.table.currentColumn()])
            self.ui.entry_number.setText("Запись " + str(self.ui.table.currentRow() + 1) + \
                                         " из " + str(self.ui.table.rowCount()))
        except AttributeError:
            pass

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
        self.ui.table.insertRow(self.ui.table.rowCount())
        for i in range(self.ui.table.columnCount()):       
            self.ui.table.setItem(self.ui.table.rowCount() - 1, i, QtWidgets.QTableWidgetItem("null"))

    def add_col_button_click(self):
        self.ui.table.insertColumn(self.ui.table.columnCount())
        self.db[0].append(str(self.ui.table.columnCount()))
        for i in range(self.ui.table.rowCount()):       
            self.ui.table.setItem(i, self.ui.table.columnCount() - 1, QtWidgets.QTableWidgetItem("null"))

    def delete_entry_button_click(self):
        if self.ui.table.currentRow() > -1:
            self.ui.table.removeRow(self.ui.table.currentRow())
            self.ui.table.selectionModel().clearCurrentIndex()
            self.ui.cell_editing.setText(None)
            self.ui.key_editing.setText(None)

    def delete_col_button_click(self):
        if self.ui.table.currentColumn() > -1:
            self.db[0].remove(self.db[0][self.ui.table.currentColumn()])
            self.ui.table.removeColumn(self.ui.table.currentColumn())
            self.ui.table.selectionModel().clearCurrentIndex()
            self.ui.cell_editing.setText(None)
            self.ui.key_editing.setText(None)

    def apply_button_click(self):
        try:
            self.ui.table.currentItem().setText(self.ui.cell_editing.toPlainText())
        except AttributeError:
            pass

    def apply_key_button_click(self):
        self.db[0][self.ui.table.currentColumn()] = self.ui.key_editing.text()
        self.ui.table.setHorizontalHeaderLabels(self.db[0])

    def goto_button_click(self):
        pass
    

class AboutProgram(QtWidgets.QMainWindow):
    def __init__(self):
        super(AboutProgram, self).__init__()
        self.ui = Ui_AboutProgram()
        self.ui.setupUi(self)
