import sys
import os
from _writer import write_annotation
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip, QPushButton)
from PyQt5.QtGui import QIcon, QFont


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont("SansSerif", 10))
        
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton("Choose dataset folder", self)
        btn.resize(btn.sizeHint())
        btn.move(30, 30)
        btn.clicked.connect(self.on_click_dataset)
        
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("Cats vs Dogs")
        self.setWindowIcon(QIcon("resourse_image/icon.png"))
        self.show()
        
    def on_click_dataset(self):
        dataset_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        if os.path.exists(dataset_path):
            path_csvfile_dataset=QtWidgets.QFileDialog.getExistingDirectory()
            write_annotation(dataset_path,path_csvfile_dataset)
            
            
            


app = QApplication(sys.argv)
ex = Window()
sys.exit(app.exec_())

