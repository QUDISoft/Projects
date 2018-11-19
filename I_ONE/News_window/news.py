import sys
import re
import html2text
import requests
from design import *
from PyQt5 import QtWidgets


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.news_links = []
        self.parsing()
        self.ui.pushButton.clicked.connect(self.text_news)

    def parsing(self):
        news_name = []
        links = []
        count = 0
        sub = 'forum'

        s = 'https://www.onliner.by/'
        p = 'https://people.onliner.by'
        a = 'https://auto.onliner.by'
        t = 'https://tech.onliner.by'
        r = 'https://realt.onliner.by'

        doc = requests.get(s).text
        peo = requests.get(p).text
        aut = requests.get(a).text
        tec = requests.get(t).text
        rea = requests.get(r).text

        mini_news = re.findall('<span class="text-i"(.+?)</span>', doc)
        people = re.findall('<a href="(.+?)class="news-tidings__stub"', peo)
        auto = re.findall('<a href="(.+?)class="news-tidings__stub"', aut)
        tech = re.findall('<a href="(.+?)class="news-tidings__stub"', tec)
        realty = re.findall('<a href="(.+?)class="news-tidings__stub"', rea)

        z_people = re.findall('<span class="news-helpers_hide_mobile-small"(.+?)</span>', peo)
        z_auto = re.findall('<span class="news-helpers_hide_mobile-small"(.+?)</span>', aut)
        z_tech = re.findall('<span class="news-helpers_hide_mobile-small"(.+?)</span>', tec)
        z_realty = re.findall('<span class="news-helpers_hide_mobile-small"(.+?)</span>', rea)
        links_mini_news = re.findall('<a href=(.+?)class="b-teasers-2__teaser-i"', doc)

        for forum in links_mini_news:
            if forum.count(sub):
                count += 1

        for i in people:
            links.append(p+i)
        for i in auto:
            links.append(a+i)
        for i in tech:
            links.append(t+i)
        for i in realty:
            links.append(r+i)
        for i in links_mini_news[0:-count]:
            links.append(i[1:])

        for l in z_people:
            news_name.append(l)
        for l in z_auto:
            news_name.append(l)
        for l in z_tech:
            news_name.append(l)
        for l in z_realty:
            news_name.append(l)
        for l in mini_news[0:-count]:
            news_name.append(l)
        count2 = 0
        for y in news_name:
            count2 += 1
            self.ui.listWidget.addItem(str(count2)+". "+y[1:])
        for y in links:
            self.news_links.append(y[0:-2])

    def text_news(self):
        n = self.ui.listWidget.currentRow()
        u = self.news_links[n]
        doc = requests.get(u).text
        h = html2text.HTML2Text()
        h.ignore_links = True
        h.body_width = False
        h.ignore_images = True
        doc = h.handle(doc)
        mas = doc.split('\n')
        text = ''
        for x in mas:
            if len(x) > 100:
                text = text + x + '\n\n'
        self.ui.textEdit.setText(text)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my_app = MyWin()
    my_app.show()
    sys.exit(app.exec_())
