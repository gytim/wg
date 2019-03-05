import sys

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, pyqtSlot

import qml_qrc
from wg.HostModel import HostModel
import wg.Request as request
import wg.GlobalParams as GP


class WG(QObject):
    def __init__(self):
        QObject.__init__(self)

    @pyqtSlot()
    def updateModel(self):
        pyWarHostModel.updateModel(request.updateModel())

    @pyqtSlot(str, str)
    def updateServer(self, hostserver, keyserver):
        GP.host = hostserver
        GP.key = keyserver

        request.clearServer()
        request.updateServer(pyWarHostModel.hostList)

    @pyqtSlot(str, str, str, str, str)
    def addItem(self, host, user, username, type, password):
        pyWarHostModel.addItem(host, user, username, type, password)

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
