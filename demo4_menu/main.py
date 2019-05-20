# -*- coding: utf-8 -*-

import sys 	
from PyQt5.QtWidgets import QApplication , QMainWindow, QWidget , QFileDialog 
from Ui_menu import Ui_MainWindow  

class MainForm( QMainWindow , Ui_MainWindow):  
	def __init__(self):  
		super(MainForm,self).__init__()  
		self.setupUi(self) 
		# 菜单的点击事件，当点击关闭菜单时连接槽函数 close()     
		self.action_3.triggered.connect(self.close)  
		# 菜单的点击事件，当点击打开菜单时连接槽函数 openMsg()     
		self.action.triggered.connect(self.openMsg)    

	def openMsg(self):  
		file,ok= QFileDialog.getOpenFileName(self,"打开","~","All Files (*);;Text Files (*.txt)") 
		# 在状态栏显示文件地址  		
		self.statusbar.showMessage(file)                   
    
if __name__=="__main__":  
	app = QApplication(sys.argv)  
	win = MainForm()  
	win.show()  
	sys.exit(app.exec_()) 