from PyQt5 import QtWidgets
from MainWindow import *


class Application(QtWidgets.QMainWindow):
    def __init__(self):
        super(Application, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def new_file_click(self):
        pass

    def open_file_click(self):
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
        pass

    def about_program_click(self):
        pass

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
    