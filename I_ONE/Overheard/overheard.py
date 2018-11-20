import requests, bs4
import Overheard_d
from PyQt5 import QtWidgets
import sys
import html2text


class MyWin(QtWidgets.QMainWindow, Overheard_d.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.parsing)
        self.comboBox.addItems(['Разное', 'Смешное', 'Пошлое', 'Страшное', 'Мистика', 'Ебанько', 'Бомжи', 'Пьянь', 'Странное', 'Провал'])

    def parsing(self):
        index = self.comboBox.currentIndex()

        url = ['https://ideer.ru', 'https://ideer.ru/secrets/smex', 'https://ideer.ru/secrets/poshloe',
               'https://ideer.ru/secrets/strax', 'https://ideer.ru/secrets/Mistika', 'https://ideer.ru/secrets/eban',
               'https://ideer.ru/secrets/bomj', 'https://ideer.ru/secrets/alco', 'https://ideer.ru/secrets/strannoe',
               'https://ideer.ru/secrets/fail']

        page = requests.get(url[index])
        doc = page.text
        h = html2text.HTML2Text()
        h.ignore_links = True
        h.body_width = False
        h.ignore_images = True
        doc = h.handle(doc)
        mas = doc.split('\n')
        text = ''
        count = 0
        for x in mas:
            if len(x) > 190:
                count += 1
                text = text + str(count) + '. ' + x + '\n\n'

        self.textEdit.setText(text)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my_app = MyWin()
    my_app.show()
    sys.exit(app.exec_())
