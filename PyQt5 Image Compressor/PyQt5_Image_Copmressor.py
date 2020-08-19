#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import PIL
from PIL import Image
import os

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Image Compress'
        self.left = 700
        self.top = 250
        self.statusBar().showMessage("Welcome to Compressor")
        self.statusBar().setObjectName("bar")
        self.width = 400
        self.height = 600
        self.image_width = 0
        self.setFixedSize(self.width,self.height)
        with open("D:\\College section\\Language practice\\Python Practice\\PyQt5 Image Compressor\\tamp.css", "r") as f:
            stylesheet = f.read()
        self.setStyleSheet(stylesheet)
        self.setObjectName("window")
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        #first window first box...............................First Frame..................................................................
        
        self.first_frame = QFrame(self)
        self.first_frame.setObjectName("one")
        self.first_frame.move(50,125)
        self.first_frame.mousePressEvent = self.second_window_one
        
        self.first_frame_head = QLabel(self.first_frame)
        self.first_frame_head.setObjectName("ht")
        self.first_frame_head.setText("Single Image Compressor")
        self.first_frame_head.move(38,20)
        
        self.first_frame_para = QLabel(self.first_frame)
        self.first_frame_para.setObjectName("pt")
        self.first_frame_para.setText("Click here to compress Single Image")
        self.first_frame_para.move(45,70)
        
        
        
    
        #first window second box................................Second Window...............................................................
        
        self.second_frame = QFrame(self)
        self.second_frame.setObjectName("one")
        self.second_frame.move(50,300)
        self.second_frame.mousePressEvent = self.second_window_two
        
        self.second_frame_head = QLabel(self.second_frame)
        self.second_frame_head.setObjectName("ht")
        self.second_frame_head.setText("Multiple Image Compressor")
        self.second_frame_head.move(32,20)
        
        self.second_frame_para = QLabel(self.second_frame)
        self.second_frame_para.setObjectName("pt")
        self.second_frame_para.setText("Click here to compress Multiple Image")
        self.second_frame_para.move(35,70)
        
        
        #secondo window (first box clicked frame).................Third Frame..............................................................
        
        self.third_frame = QFrame(self)
        self.third_frame.setObjectName("two")
        self.third_frame.move(50,125)
        self.third_frame.setVisible(False)
        
        self.third_frame_rich = QLabel(self.third_frame)
        self.third_frame_rich.setObjectName("rt")
        self.third_frame_rich.move(20,10)
        self.third_frame_rich.setTextFormat(Qt.RichText)
        self.third_frame_rich.setText("&#8592")
        self.third_frame_rich.mousePressEvent = self.arrow_event_one
        
        self.third_frame_head = QLabel(self.third_frame)
        self.third_frame_head.setObjectName("ht_1")
        self.third_frame_head.setText("Compressor")
        self.third_frame_head.move(110,10)
        
        self.third_frame_text = QLabel(self.third_frame)
        self.third_frame_text.setObjectName("pt")
        self.third_frame_text.move(30,50)
        self.third_frame_text.setText("Choose Image")
        
        self.third_frame_box_one = QLineEdit(self.third_frame)
        self.third_frame_box_one.move(65,70)
        self.third_frame_box_one.setObjectName("box_one")
        
        self.third_frame_button_1 = QPushButton(self.third_frame)
        self.third_frame_button_1.setObjectName("button")
        self.third_frame_button_1.setText("...")
        self.third_frame_button_1.move(250,70)
        self.third_frame_button_1.clicked.connect(self.openFileNameDialog)
        
        
        
        
        self.third_frame_text_two = QLabel(self.third_frame)
        self.third_frame_text_two.setObjectName("pt")
        self.third_frame_text_two.move(30,100)
        self.third_frame_text_two.setText("Image Quality")
        
        self.third_frame_box_two = QLineEdit(self.third_frame)
        self.third_frame_box_two.move(65,120)
        self.third_frame_box_two.setObjectName("box_two")
        
        self.third_frame_combo_1 = QComboBox(self.third_frame)
        self.third_frame_combo_1.addItem("High")
        
        self.third_frame_combo_1.addItem("Low")
        self.third_frame_combo_1.currentIndexChanged.connect(self.comboQuality_1)
        self.third_frame_combo_1.move(190,120)
        
        self.third_frame_button_2 = QPushButton(self.third_frame)
        self.third_frame_button_2.setText("Compress")
        self.third_frame_button_2.setObjectName("main_button")
        self.third_frame_button_2.move(105,180)
        self.third_frame_button_2.clicked.connect(self.resize_pic)
        
        
        
        
        
        
        
        #second window (second box clicked frame).....................Fourth window..........................................................
     
        
        self.fourth_frame = QFrame(self)
        self.fourth_frame.setObjectName("two")
        self.fourth_frame.move(50,125)
        self.fourth_frame.setVisible(False)
        
        self.fourth_frame_rich = QLabel(self.fourth_frame)
        self.fourth_frame_rich.setObjectName("rt")
        self.fourth_frame_rich.move(20,10)
        self.fourth_frame_rich.setTextFormat(Qt.RichText)
        self.fourth_frame_rich.setText("&#8592")
        self.fourth_frame_rich.mousePressEvent = self.arrow_event_two
        
        self.fourth_frame_head = QLabel(self.fourth_frame)
        self.fourth_frame_head.setObjectName("ht_1")
        self.fourth_frame_head.setText("Compressor")
        self.fourth_frame_head.move(110,10)
        
        self.fourth_frame_text = QLabel(self.fourth_frame)
        self.fourth_frame_text.setObjectName("pt")
        self.fourth_frame_text.move(30,50)
        self.fourth_frame_text.setText("Choose Image Folder")
        
        self.fourth_frame_box_one = QLineEdit(self.fourth_frame)
        self.fourth_frame_box_one.move(65,70)
        self.fourth_frame_box_one.setObjectName("box_one")
        
        self.fourth_frame_button_1 = QPushButton(self.fourth_frame)
        self.fourth_frame_button_1.setObjectName("button")
        self.fourth_frame_button_1.setText("...")
        self.fourth_frame_button_1.clicked.connect(self.openSourceDirectory)
        self.fourth_frame_button_1.move(250,70)
        
        
        self.fourth_frame_text_two = QLabel(self.fourth_frame)
        self.fourth_frame_text_two.setObjectName("pt")
        self.fourth_frame_text_two.move(30,100)
        self.fourth_frame_text_two.setText("Choose Destination Folder")
        
        self.fourth_frame_box_two = QLineEdit(self.fourth_frame)
        self.fourth_frame_box_two.move(65,120)
        self.fourth_frame_box_two.setObjectName("box_one")
        
        self.fourth_frame_button_2 = QPushButton(self.fourth_frame)
        self.fourth_frame_button_2.setObjectName("button")
        self.fourth_frame_button_2.setText("...")
        self.fourth_frame_button_2.clicked.connect(self.openDestinationDirectory)
        self.fourth_frame_button_2.move(250,120)
        
        self.fourth_frame_text_three = QLabel(self.fourth_frame)
        self.fourth_frame_text_three.setObjectName("pt")
        self.fourth_frame_text_three.move(30,150)
        self.fourth_frame_text_three.setText("Image Quality")
        
        self.fourth_frame_box_three = QLineEdit(self.fourth_frame)
        self.fourth_frame_box_three.move(65,170)
        self.fourth_frame_box_three.setObjectName("box_two")
        
        
        self.fourth_frame_combo_1 = QComboBox(self.fourth_frame)
        self.fourth_frame_combo_1.addItem("Options")
        self.fourth_frame_combo_1.addItem("High")
        self.fourth_frame_combo_1.addItem("Low")
        self.fourth_frame_combo_1.move(190,170)
        self.fourth_frame_combo_1.currentIndexChanged.connect(self.comboQuality_2)
        
        self.fourth_frame_button_3 = QPushButton(self.fourth_frame)
        self.fourth_frame_button_3.setText("Compress")
        self.fourth_frame_button_3.setObjectName("main_button")
        self.fourth_frame_button_3.move(105,210)
        self.fourth_frame_button_3.clicked.connect(self.resize_dir)
        
        
        
        self.show()
        
        #calling function on clicking first window first box....................................................................
    def second_window_one(self,event):
        self.first_frame.setVisible(False)
        self.second_frame.setVisible(False)
        self.fourth_frame.setVisible(False)
        self.third_frame.setVisible(True)
        
        #calling function on clicking first window second box...................................................................
    def second_window_two(self,ent):
        self.first_frame.setVisible(False)
        self.second_frame.setVisible(False)
        self.third_frame.setVisible(False)
        self.fourth_frame.setVisible(True)
    
        #calling function on clicking second window back arrow..................................................................
    def arrow_event_one(self,event):
        self.first_frame.setVisible(True)
        self.second_frame.setVisible(True)
        self.third_frame.setVisible(False)
        self.fourth_frame.setVisible(False)
        self.statusBar().showMessage("Welcome To Compressor")
        
        #calling function on clicking second window back arrow..................................................................
    def arrow_event_two(self,event):
        self.first_frame.setVisible(True)
        self.second_frame.setVisible(True)
        self.third_frame.setVisible(False)
        self.fourth_frame.setVisible(False)
        self.statusBar().showMessage("Welcome To Compressor")
        
        
        
        
        #making button functional
    def openFileNameDialog(self):
        self.fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;jpg Files (*.jpg);;png Files (*.png)")
        self.third_frame_box_one.setText(self.fileName)
        
        try :
            img = Image.open(self.fileName)
            self.image_width = img.width
            self.third_frame_box_two.setText(str(self.image_width))
        except :
            self.statusBar().showMessage("Select Only Image")
       
        
        
            
    def openSourceDirectory(self): 
        try:
            self.folder_1 = QFileDialog.getExistingDirectory(self,"Select Source Directory")
            self.fourth_frame_box_one.setText(self.folder_1)
            files = os.listdir(self.folder_1)
            src_dir = self.folder_1+ "\\"+ files[0]
            img = Image.open(src_dir)
            self.image_width = img.size[0]
            self.fourth_frame_box_three.setText("Select Option")
        except:
            self.fourth_frame_box_one.setText("Select Source Directory")
            
        
        
        
        
    def openDestinationDirectory(self):
        self.folder_2 = QFileDialog.getExistingDirectory(self,"Select Destination Directory")
        self.fourth_frame_box_two.setText(self.folder_2) 
        
    def comboQuality_1(self):
        if self.third_frame_combo_1.currentText() == "High":
            self.third_frame_box_two.setText(str(self.image_width))
            
        
            
            
        if self.third_frame_combo_1.currentText() == "Low":
            self.third_frame_box_two.setText(str(self.image_width/4))
            
            
    def comboQuality_2(self):
        if self.fourth_frame_combo_1.currentText() == "High":
            self.fourth_frame_box_three.setText(str(self.image_width))
            
        
            
        
        if self.fourth_frame_combo_1.currentText() == "Low":
            self.fourth_frame_box_three.setText(str(self.image_width/4))
            
            
            
    def resize_pic(self):
        try :
            img = Image.open(self.fileName)
            wpercent = (self.image_width/float(img.size[0]))
            hsize = int((float(img.size[1])*float(wpercent)))
            image = img.resize((self.image_width,hsize),PIL.Image.ANTIALIAS)
            image.save(self.fileName)
            self.statusBar().showMessage("Your Image Is Compressed")
        except :
            self.statusBar().showMessage("Select only image")
    def one_by_one(self):
        img = Image.open(self.old_pic)
        wpercent = (self.image_width/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        image = img.resize((int(self.image_width),int(hsize)),PIL.Image.ANTIALIAS)
        image.save(self.new_pic)
    
    def resize_dir(self):
        try:
            files = os.listdir(self.folder_1)
            for file in files:
                self.old_pic = self.folder_1 + "\\" + file
                self.new_pic = self.folder_2 + "\\" + file
                self.one_by_one()
            self.statusBar().showMessage("Images Compressed")
        except:
            self.fourth_frame_box_two.setText("Select Destination Directory")
            
            
        

            
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
    
    
    
    
    
    
    
    
    



# In[ ]:





# In[ ]:




