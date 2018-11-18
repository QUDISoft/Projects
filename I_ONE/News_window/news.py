import sys, re, urllib, html2text
from urllib import request
from design import *
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.newsurl=[]
        self.Parse()
        self.ui.pushButton.clicked.connect(self.AllNews)

    def Parse(self):
        s = 'https://www.onliner.by'
        doc = urllib.request.urlopen(s).read().decode('utf-8', errors='ignore')
        links = re.findall('<a href=(.+?)class="b-teasers-2__teaser-i"', doc)
        zagolovki = re.findall('<span class="text-i"(.+?)</span>', doc)

        for y in zagolovki:
            self.ui.listWidget.addItem(y[1:])
        for x in links:

            self.newsurl.append(x[1:-1])

    def AllNews(self):
        n=self.ui.listWidget.currentRow()
        u=self.newsurl[n]
        doc=urllib.request.urlopen(u).read().decode('UTF-8', errors='ignore')
        h=html2text.HTML2Text()
        h.ignore_links = True
        h.body_width = False
        h.ignore_images = True
        doc = h.handle(doc)
        mas = doc.split('\n')
        stroka=''
        for x in mas:
            if(len(x)>100):
                stroka=stroka+x+'\n\n'
        self.ui.textEdit.setText(stroka)
        
        
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
