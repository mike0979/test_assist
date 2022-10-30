import sys
from PyQt5.QtWidgets import QApplication, QWidget
from untitled import Ui_Form

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget()
    ui = Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())