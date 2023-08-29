import os, sys, json
from PyQt5 import QtWidgets
from Application import *


def main():
    app = QtWidgets.QApplication([])
    application = Application()
    application.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
    application.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
