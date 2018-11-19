# -*- coding: utf-8 -*-
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import design  # Это наш конвертированный файл дизайна
import os
import SelectTrueLinks as Srl

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.batton.clicked.connect(self.browse_folder)
        self.pushButton.clicked.connect(self.addExc)
        self.pushButton_2.clicked.connect(self.delExc)
        self.exceptions=[]
        print(self.listWidget_2.currentItem())
        try:
            f=open('exc.txt', 'r')
            for line in f:
                line=line[:-1]
                self.exceptions.append(line)
            for x in self.exceptions:
                self.listWidget_2.addItem(x)            
        except:
            print('file error')
        
        
    def delExc(self):
        try:
            row=self.listWidget_2.currentRow()
            item=self.listWidget_2.item(row)
            currentItem=item.text()        
            newExcep=[]
            for exception in self.exceptions:
                if exception!=currentItem:
                    newExcep.append(exception)    
                else:
                    continue
            f=self.excFile()
            self.listWidget_2.clear()
            self.exceptions=newExcep
            for x in newExcep:
                self.listWidget_2.addItem(x)
                f.write(x + '\n')
        except:
            print('Error: No selected items')
            
            
    def excFile(self):
        f=open('exc.txt', 'w')  
        return f
    def addExc(self):
        f=self.excFile()        
        q=self.lineEdit_2.text()
        if '' or ' ' in q:
            print('Error: Spase detected')
        else:
            self.exceptions.append(q)              
        self.lineEdit_2.clear()
        self.listWidget_2.clear()
        for x in self.exceptions:
            self.listWidget_2.addItem(x)
            f.write(x + '\n')
        

    def browse_folder(self):
        self.listWidget.clear()  # На случай, если в списке уже есть элементы
        q=self.lineEdit
        page=q.text()
        # открыть диалог выбора директории и установить значение переменной
        # равной пути к выбранной директории
        select=Srl.select(page)
        links=Srl.findLinks(page, select, self.exceptions)
         # не продолжать выполнение, если пользователь не выбрал директорию
        for file_name in links:  # для каждого файла в директории
            self.listWidget.addItem(file_name)   # добавить файл в listWidget               

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()