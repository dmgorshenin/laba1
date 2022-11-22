import sys
import os
from _writer import write_annotation
from _copy_to_another_dir import copying_images_to_another
from _copying_with_random_number import copying_to_random
from _iterator import Iterator
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.path_csv = ""

    def initUI(self):

        QToolTip.setFont(QFont("SansSerif", 10))

        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("Cats vs Dogs")
        self.setWindowIcon(QIcon("resourse_image/icon.png"))

        btn_first = QPushButton("Create annotation from dataset", self)
        btn_first.resize(btn_first.sizeHint())
        btn_first.move(30, 30)
        btn_first.clicked.connect(self.on_click_dataset)

        btn_second = QPushButton(
            "Copying to another directory and create annotation", self)
        btn_second.resize(btn_second.sizeHint())
        btn_second.move(30, 60)
        btn_second.clicked.connect(self.on_click_another)

        btn_third = QPushButton(
            "Copying to new directory with random number and create annotation", self)
        btn_third.resize(btn_third.sizeHint())
        btn_third.move(30, 90)
        btn_third.clicked.connect(self.on_click_random)

        btn_image_cat = QPushButton("Show the cat", self)
        btn_image_cat.resize(btn_image_cat.sizeHint())
        btn_image_cat.move(30, 200)
        btn_image_cat.clicked.connect(self.on_click_next_cat)

        btn_image_dog = QPushButton("Show the dog", self)
        btn_image_dog.resize(btn_image_dog.sizeHint())
        btn_image_dog.move(30, 230)
        btn_image_dog.clicked.connect(self.on_click_next_dog)

        self.show()

    def on_click_dataset(self):
        dataset_path = QFileDialog.getExistingDirectory(
            self, 'Select Folder')
        
        if os.path.exists(dataset_path+"/cat") and os.path.exists(dataset_path+"/dog"):
            path_csvfile_dataset = QFileDialog.getOpenFileName(
                self, 'Select folder to save csvfile',None,"CSV (*.csv, *.xlsx)")[0]
            
            self.path_csv = write_annotation(
                dataset_path, path_csvfile_dataset)
            print(self.path_csv)

    def on_click_another(self):
        dataset_path = QFileDialog.getExistingDirectory(
            self, 'Select Folder')
        
        if os.path.exists(dataset_path+"/cat") and os.path.exists(dataset_path+"/dog"):
            path_another_dataset = QFileDialog.getExistingDirectory(
                self, 'Select folder to save another directory')
            
            self.path_csv = copying_images_to_another(
                dataset_path, path_another_dataset)
            print(self.path_csv)

    def on_click_random(self):
        dataset_path = QFileDialog.getExistingDirectory(
            self, 'Select Folder')
        
        if os.path.exists(dataset_path+"/cat") and os.path.exists(dataset_path+"/dog"):
            path_random_dataset = QFileDialog.getExistingDirectory(
                self, 'Select folder to save random directory')
            
            self.path_csv = copying_to_random(
                dataset_path, path_random_dataset)
            print(self.path_csv)

    def on_click_next_cat(self):
        if self.path_csv == "":
            fname = QFileDialog.getOpenFileName(
                self, "Open csvfile", None, "CSV (*.csv, *.xlsx)")[0]
           
            if not fname:
                return
            
            self.path_csv = fname
       
        self.show_image("cat")

    def on_click_next_dog(self):
        if self.path_csv == "":
            fname = QFileDialog.getOpenFileName(
                self, "Open csvfile", None, "CSV (*.csv, *.xlsx)")[0]
           
            if not fname:
                return
           
            self.path_csv = fname
        
        self.show_image("dog")

    def show_image(self, class_name):
        iter = Iterator(self.path_csv, class_name)
        flag = False
        while(True):
            
            self.dialog = QMessageBox()
            self.dialog.addButton(
                f"Next {class_name}", QMessageBox.AcceptRole)
            self.dialog.addButton("Stop", QMessageBox.RejectRole)
            self.dialog.setText("Choose what to do")
            self.dialog.exec_()
            
            if self.dialog.clickedButton().text() == f"Next {class_name}":
                image=iter.__iter__()
                
                if not flag:
                    self.image_window = NextImage(image, class_name, self)
                    self.image_window.show()
                    flag = True
                
                else:
                    self.image_window.change_image(image)

                iter.__next__()

            if self.dialog.clickedButton().text() == "Stop":
                self.image_window.close()
                break


class NextImage(QtWidgets.QWidget):
    def __init__(self, path, class_name, parent=None) -> None:
        super().__init__(parent, QtCore.Qt.Window)
        self.path_image = path
        self.class_name = class_name
        self.build()

    def build(self):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap(self.path_image)

        self.lbl = QLabel(self)
        self.lbl.setPixmap(pixmap)

        hbox.addWidget(self.lbl)
        self.setLayout(hbox)

        self.move(800, 100)
        self.setWindowTitle(self.class_name)

    def change_image(self, path_image):
        self.lbl.setPixmap(QPixmap(path_image))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
