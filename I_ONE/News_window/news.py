import sys, re, urllib, html2text
from urllib import request
from design import *
from PyQt5 import QtWidgets


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.newsurl = []
        self.Parse()
        self.ui.pushButton.clicked.connect(self.AllNews)

    def Parse(self):
        zagolovki = []
        links = []
        s = 'https://www.onliner.by/'
        p = 'https://people.onliner.by'
        a = 'https://auto.onliner.by'
        t = 'https://tech.onliner.by'
        r = 'https://realt.onliner.by'
        doc = urllib.request.urlopen(s).read().decode('utf-8', errors='ignore')
        peo = urllib.request.urlopen(p).read().decode('utf-8', errors='ignore')
        aut = urllib.request.urlopen(a).read().decode('utf-8', errors='ignore')
        tec = urllib.request.urlopen(t).read().decode('utf-8', errors='ignore')
        rea = urllib.request.urlopen(r).read().decode('utf-8', errors='ignore')

        mini_news = re.findall('<span class="text-i"(.+?)</span>', doc)
        people = re.findall('<a href="(.+?)class="news-tidings__stub"', peo)
        auto = re.findall('<a href="(.+?)class="news-tidings__stub"', aut)
        tech = re.findall('<a href="(.+?)class="news-tidings__stub"', tec)
        realt = re.findall('<a href="(.+?)class="news-tidings__stub"', rea)

        z_people = re.findall('<span class="news-helpers_hide_mobile-small"(.+?)</span>', peo)
        z_auto = re.findall('<span class="news-helpers_hide_mobile-small"(.+?)</span>', aut)
        z_tech = re.findall('<span class="news-helpers_hide_mobile-small"(.+?)</span>', tec)
        z_realt = re.findall('<span class="news-helpers_hide_mobile-small"(.+?)</span>', rea)
        links_mini_news = re.findall('<a href=(.+?)class="b-teasers-2__teaser-i"', doc)

        for i in people:
            links.append(p+i)
        for i in auto:
            links.append(a+i)
        for i in tech:
            links.append(t+i)
        for i in realt:
            links.append(r+i)
        for i in links_mini_news:
            links.append(i[1:])

        for l in z_people:
            zagolovki.append(l)
        for l in z_auto:
            zagolovki.append(l)
        for l in z_tech:
            zagolovki.append(l)
        for l in z_realt:
            zagolovki.append(l)
        for l in mini_news:
            zagolovki.append(l)

        for y in zagolovki:
            self.ui.listWidget.addItem(y[1:])
        for y in links:
            self.newsurl.append(y[0:-2])

    def AllNews(self):
        n = self.ui.listWidget.currentRow()
        u = self.newsurl[n]
        doc = urllib.request.urlopen(u).read().decode('UTF-8', errors='ignore')
        h = html2text.HTML2Text()
        h.ignore_links = True
        h.body_width = False
        h.ignore_images = True
        doc = h.handle(doc)
        mas = doc.split('\n')
        stroka = ''
        for x in mas:
            if (len(x) > 100):
                stroka = stroka + x + '\n\n'
        self.ui.textEdit.setText(stroka)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
