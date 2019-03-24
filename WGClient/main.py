# Принцип работы
# В модели хранятся данные добавленных хостов
# При запуске обмена происходит: Очистка сервера, Добавление всего списка из модели на сервер
# При получении ответа, чистится модель и заполняется данными сервера
#
import sys

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, pyqtSlot

import qml_qrc
from wg.HostModel import HostModel
import wg.Request as request
import wg.GlobalParams as GP

# в qml 4 кнопки
class WG(QObject):
    def __init__(self):
        QObject.__init__(self)
        
    # обновляем отображения списка
    @pyqtSlot()
    def updateModel(self):
        pyWarHostModel.updateModel(request.updateModel())
    
    # Обвновляем информацию на сервере
    @pyqtSlot(str, str)
    def updateServer(self, hostserver, keyserver):
        GP.host = hostserver
        GP.key = keyserver

        request.clearServer()
        request.updateServer(pyWarHostModel.hostList)

    # Добавляем хост в список
    @pyqtSlot(str, str, str, str, str)
    def addItem(self, hostname, user, username, type, password):
        pyWarHostModel.addItem(hostname, user, username, type, password)

    # Удаляем хост из списка
    @pyqtSlot(str)
    def deleteItem(self, id):
        pyWarHostModel.deleteItem(id)


if __name__ == "__main__":
    global app

    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    pyWarClient = WG()
    pyWarHostModel = HostModel()

    engine.rootContext().setContextProperty("pyWarClient", pyWarClient)
    engine.rootContext().setContextProperty("pyWarHostModel", pyWarHostModel)

    engine.load("qrc:/qml/main.qml")

    engine.quit.connect(app.quit)
    sys.exit(app.exec_())
