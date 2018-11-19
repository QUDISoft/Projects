import sys
import html2text
import requests
from design import *
from PyQt5 import QtWidgets
from bs4 import BeautifulSoup


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
        count2 = 0
        sub = 'forum'

        s = 'https://www.onliner.by/'
        p = 'https://people.onliner.by'
        a = 'https://auto.onliner.by'
        t = 'https://tech.onliner.by'
        r = 'https://realt.onliner.by'

        mini = BeautifulSoup(requests.get(s).text, "html.parser")
        mini_news = mini.findAll('span', class_="text-i")
        links_mini_news = mini.findAll('a', class_='b-teasers-2__teaser-i')

        peo = BeautifulSoup(requests.get(p).text, "html.parser")
        z_people = peo.findAll('span', class_="news-helpers_hide_mobile-small")
        people = peo.findAll('a', class_='news-tidings__stub')

        aut = BeautifulSoup(requests.get(a).text, "html.parser")
        z_auto = aut.findAll('span', class_="news-helpers_hide_mobile-small")
        auto = aut.findAll('a', class_='news-tidings__stub')

        tec = BeautifulSoup(requests.get(t).text, "html.parser")
        z_tech = tec.findAll('span', class_="news-helpers_hide_mobile-small")
        tech = tec.findAll('a', class_="news-tidings__stub")

        rea = BeautifulSoup(requests.get(r).text, "html.parser")
        z_realty = rea.findAll('span', class_="news-helpers_hide_mobile-small")
        realty = rea.findAll('a', class_="news-tidings__stub")

        for forum in links_mini_news:
            if forum.get('href').count(sub):
                count += 1

        for i in people:
            links.append(p+i.get('href'))
        for i in auto:
            links.append(a+i.get('href'))
        for i in tech:
            links.append(t+i.get('href'))
        for i in realty:
            links.append(r+i.get('href'))
        for i in links_mini_news[0:-count]:
            links.append(i.get('href'))

        for l in z_people:
            news_name.append(l.text)
        for l in z_auto:
            news_name.append(l.text)
        for l in z_tech:
            news_name.append(l.text)
        for l in z_realty:
            news_name.append(l.text)
        for l in mini_news[0:-count]:
            news_name.append(l.text)

        for y in news_name:
            count2 += 1
            self.ui.listWidget.addItem(str(count2)+". "+y)
        for y in links:
            self.news_links.append(y)

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
